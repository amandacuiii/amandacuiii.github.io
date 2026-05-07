#!/usr/bin/env python3
"""
Image optimization script to compress images for web use.
Reduces file size while maintaining visual quality.
"""

import os
from PIL import Image
import sys

def optimize_image(input_path, output_path=None, quality=85, max_size=(2000, 2000), make_square=True):
    """
    Optimize an image by cropping to square, resizing if needed, and compressing.
    
    Args:
        input_path: Path to input image
        output_path: Path to save optimized image (defaults to overwrite)
        quality: JPEG quality (1-100, default 85)
        max_size: Maximum dimensions (width, height) - will be square
        make_square: Whether to crop image to square (default True)
    """
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if necessary (removes alpha channel for JPEG)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Crop to square (center crop)
            if make_square:
                width, height = img.size
                if width != height:
                    # Calculate the size of the square (use the smaller dimension)
                    size = min(width, height)
                    # Calculate the center crop box
                    left = (width - size) // 2
                    top = (height - size) // 2
                    right = left + size
                    bottom = top + size
                    # Crop to square
                    img = img.crop((left, top, right, bottom))
            
            # Resize to max_size (which should be square)
            if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save optimized image
            if output_path is None:
                output_path = input_path
            
            # Save with optimization
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # Get file sizes
            original_size = os.path.getsize(input_path)
            new_size = os.path.getsize(output_path)
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"✓ {input_path}")
            print(f"  {original_size / 1024 / 1024:.2f}MB → {new_size / 1024 / 1024:.2f}MB ({reduction:.1f}% reduction)")
            print(f"  Size: {img.size[0]}x{img.size[1]}px")
            
            return True
    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")
        return False

def optimize_directory(directory, quality=85, max_size=(2000, 2000), create_backup=False, make_square=True):
    """
    Optimize all images in a directory.
    
    Args:
        directory: Directory to process
        quality: JPEG quality (1-100)
        max_size: Maximum dimensions
        create_backup: Whether to create backup directory
    """
    image_extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG')
    
    if create_backup:
        backup_dir = os.path.join(directory, 'original_images_backup')
        if not os.path.exists(backup_dir):
            print(f"Creating backup directory: {backup_dir}")
            os.makedirs(backup_dir)
    
    processed = 0
    skipped = 0
    
    for root, dirs, files in os.walk(directory):
        # Skip backup directories
        if 'original_images_backup' in root:
            continue
            
        for file in files:
            if file.lower().endswith(image_extensions):
                file_path = os.path.join(root, file)
                
                # Skip if already in backup
                if 'original_images_backup' in file_path:
                    continue
                
                # Create backup if requested
                if create_backup:
                    rel_path = os.path.relpath(file_path, directory)
                    backup_path = os.path.join(backup_dir, rel_path)
                    backup_dir_path = os.path.dirname(backup_path)
                    if not os.path.exists(backup_dir_path):
                        os.makedirs(backup_dir_path)
                    if not os.path.exists(backup_path):
                        import shutil
                        shutil.copy2(file_path, backup_path)
                
                # Optimize image
                if optimize_image(file_path, quality=quality, max_size=max_size, make_square=make_square):
                    processed += 1
                else:
                    skipped += 1
    
    print(f"\n✓ Processed: {processed} images")
    if skipped > 0:
        print(f"✗ Skipped: {skipped} images")

if __name__ == '__main__':
    # Optimize pottery images (smaller for gallery, square)
    pottery_dir = 'photos/Pottery pics'
    if os.path.exists(pottery_dir):
        print("Optimizing pottery images...")
        print("Gallery images: square 800x800px, quality 75")
        optimize_directory(pottery_dir, quality=75, max_size=(800, 800), create_backup=True, make_square=True)
    
    # Optimize other photos (larger for background, square)
    other_dirs = ['photos/Sony shots', 'photos/Photos of me']
    for photo_dir in other_dirs:
        if os.path.exists(photo_dir):
            print(f"\nOptimizing {photo_dir}...")
            print("Background images: square 1500x1500px, quality 80")
            optimize_directory(photo_dir, quality=80, max_size=(1500, 1500), create_backup=True, make_square=True)
    
    print("\n✓ Image optimization complete!")
    print("Original images backed up in 'original_images_backup' directories")


# Website Customization Guide

## 🎨 Changing Colors

### Primary Color Scheme
The website uses a custom color scheme defined in the Tailwind config. To change the colors, edit this section in `index.html`:

```html
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    'primary': '#2563eb',      // Main blue color
                    'secondary': '#64748b',    // Gray text color
                    'accent': '#f59e0b'        // Orange accent color
                }
            }
        }
    }
</script>
```

### Color Examples:
- **Blue Theme**: `'primary': '#2563eb'` (current)
- **Purple Theme**: `'primary': '#8b5cf6'`
- **Green Theme**: `'primary': '#10b981'`
- **Pink Theme**: `'primary': '#ec4899'`
- **Orange Theme**: `'primary': '#f97316'`

### Gradient Colors
To change gradient colors, look for these classes and replace them:
- `from-blue-50 to-indigo-100` → `from-purple-50 to-pink-100`
- `from-primary to-purple-600` → `from-primary to-pink-600`
- `bg-gradient-to-br from-blue-100 to-purple-100` → `bg-gradient-to-br from-green-100 to-blue-100`

## 📸 Adding Your Photos

### 1. Hero Section Photo
Replace the placeholder avatar:

```html
<!-- Find this section in the Hero -->
<div class="w-32 h-32 mx-auto mb-6 rounded-full bg-gradient-to-br from-primary to-purple-600 flex items-center justify-center">
    <i class="fas fa-user text-4xl text-white"></i>  <!-- Replace this -->
</div>
```

**Replace with:**
```html
<div class="w-32 h-32 mx-auto mb-6 rounded-full overflow-hidden shadow-2xl">
    <img src="your-photo.jpg" alt="Your Name" class="w-full h-full object-cover">
</div>
```

### 2. About Me Section Photo
Replace the placeholder image:

```html
<!-- Find this section in About Me -->
<div class="aspect-square bg-gradient-to-br from-gray-200 to-gray-300 rounded-2xl flex items-center justify-center">
    <i class="fas fa-image text-6xl text-gray-400"></i>  <!-- Replace this -->
</div>
```

**Replace with:**
```html
<div class="aspect-square rounded-2xl overflow-hidden shadow-lg">
    <img src="about-photo.jpg" alt="About [Your Name]" class="w-full h-full object-cover">
</div>
```

### 3. Portfolio Items Photos
Replace the gradient backgrounds with your actual photos:

```html
<!-- Example: Wedding Photography -->
<div class="aspect-video bg-gradient-to-br from-amber-100 to-orange-200 flex items-center justify-center relative overflow-hidden">
    <i class="fas fa-camera text-4xl text-amber-600"></i>  <!-- Replace this -->
</div>
```

**Replace with:**
```html
<div class="aspect-video relative overflow-hidden">
    <img src="wedding-photo.jpg" alt="Wedding Photography" class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-black/20 hover:bg-black/40 transition-colors duration-300 flex items-center justify-center">
        <i class="fas fa-search-plus text-white text-2xl"></i>
    </div>
</div>
```

### 4. Creating a Photos Folder
1. Create a `photos` folder in your website directory
2. Add your photos there (recommended sizes):
   - Hero photo: 300x300px (square)
   - About photo: 600x600px (square)
   - Portfolio photos: 800x600px (4:3 ratio)

### 5. Photo Optimization Tips
- Use JPEG for photos, PNG for graphics with transparency
- Compress images for web (aim for under 500KB each)
- Use tools like TinyPNG or ImageOptim to compress
- Consider using WebP format for better compression

## 🎯 Quick Color Change Examples

### Purple Theme
```javascript
colors: {
    'primary': '#8b5cf6',      // Purple
    'secondary': '#6b7280',    // Gray
    'accent': '#f59e0b'        // Orange
}
```

### Green Theme
```javascript
colors: {
    'primary': '#10b981',      // Green
    'secondary': '#6b7280',    // Gray
    'accent': '#f59e0b'        // Orange
}
```

### Pink Theme
```javascript
colors: {
    'primary': '#ec4899',      // Pink
    'secondary': '#6b7280',    // Gray
    'accent': '#f59e0b'        // Orange
}
```

## 📁 File Structure
```
personal-website/
├── index.html
├── README.md
├── CUSTOMIZATION_GUIDE.md
└── photos/                    # Create this folder
    ├── hero-photo.jpg
    ├── about-photo.jpg
    ├── wedding-photo.jpg
    ├── portrait-photo.jpg
    ├── documentary-photo.jpg
    ├── pottery-photo1.jpg
    └── pottery-photo2.jpg
```

## 🔧 Step-by-Step Photo Replacement

### Step 1: Prepare Your Photos
1. Resize photos to recommended dimensions
2. Compress them for web use
3. Save them in a `photos` folder

### Step 2: Update HTML
1. Open `index.html` in a text editor
2. Find the placeholder icons (`<i class="fas fa-..."></i>`)
3. Replace with `<img>` tags pointing to your photos

### Step 3: Test
1. Save the file
2. Refresh your browser
3. Check that photos load correctly

## 🎨 Advanced Customization

### Custom CSS Classes
You can add custom CSS in the `<style>` section:

```html
<style>
    .custom-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .custom-shadow {
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }
</style>
```

### Changing Background Colors
Replace background classes:
- `bg-gray-50` → `bg-blue-50`
- `bg-white` → `bg-gray-100`
- `bg-gradient-to-br from-blue-50 to-indigo-100` → `bg-gradient-to-br from-purple-50 to-pink-100`

## 🚀 Quick Start Checklist

- [ ] Choose your color scheme
- [ ] Update the Tailwind config colors
- [ ] Create a `photos` folder
- [ ] Add your hero photo
- [ ] Add your about photo
- [ ] Add portfolio photos
- [ ] Update all photo references in HTML
- [ ] Test the website
- [ ] Compress images if needed

## 📞 Need Help?
If you need assistance with any of these changes, feel free to ask for specific help with:
- Color scheme suggestions
- Photo sizing and optimization
- HTML editing
- Testing your changes

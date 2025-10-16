# Quick Changes Guide

## 🎨 Change Colors (3 Easy Steps)

### Step 1: Find This Code (around line 12-20)
```html
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    'primary': '#2563eb',      // ← Change this color
                    'secondary': '#64748b',    // ← Change this color  
                    'accent': '#f59e0b'        // ← Change this color
                }
            }
        }
    }
</script>
```

### Step 2: Replace Colors
**Current (Blue Theme):**
- Primary: `#2563eb` (blue)
- Secondary: `#64748b` (gray)
- Accent: `#f59e0b` (orange)

**Purple Theme:**
- Primary: `#8b5cf6` (purple)
- Secondary: `#6b7280` (gray)
- Accent: `#f59e0b` (orange)

**Green Theme:**
- Primary: `#10b981` (green)
- Secondary: `#6b7280` (gray)
- Accent: `#f59e0b` (orange)

### Step 3: Save and Refresh
Save the file and refresh your browser to see the changes!

## 📸 Add Your Photos (4 Easy Steps)

### Step 1: Create Photos Folder
I've already created a `photos` folder for you. Add your photos there.

### Step 2: Replace Hero Photo
**Find this code (around line 240):**
```html
<div class="w-32 h-32 mx-auto mb-6 rounded-full bg-gradient-to-br from-primary to-purple-600 flex items-center justify-center">
    <i class="fas fa-user text-4xl text-white"></i>
</div>
```

**Replace with:**
```html
<div class="w-32 h-32 mx-auto mb-6 rounded-full overflow-hidden shadow-2xl">
    <img src="photos/your-hero-photo.jpg" alt="Your Name" class="w-full h-full object-cover">
</div>
```

### Step 3: Replace About Photo
**Find this code (around line 295):**
```html
<div class="aspect-square bg-gradient-to-br from-gray-200 to-gray-300 rounded-2xl flex items-center justify-center">
    <i class="fas fa-image text-6xl text-gray-400"></i>
</div>
```

**Replace with:**
```html
<div class="aspect-square rounded-2xl overflow-hidden shadow-lg">
    <img src="photos/your-about-photo.jpg" alt="About [Your Name]" class="w-full h-full object-cover">
</div>
```

### Step 4: Replace Portfolio Photos
**Find any portfolio item like this:**
```html
<div class="aspect-video bg-gradient-to-br from-amber-100 to-orange-200 flex items-center justify-center relative overflow-hidden">
    <i class="fas fa-camera text-4xl text-amber-600"></i>
</div>
```

**Replace with:**
```html
<div class="aspect-video relative overflow-hidden">
    <img src="photos/wedding-photo.jpg" alt="Wedding Photography" class="w-full h-full object-cover">
    <div class="absolute inset-0 bg-black/20 hover:bg-black/40 transition-colors duration-300 flex items-center justify-center">
        <i class="fas fa-search-plus text-white text-2xl"></i>
    </div>
</div>
```

## 📏 Photo Sizes
- **Hero photo**: 300x300 pixels (square)
- **About photo**: 600x600 pixels (square)  
- **Portfolio photos**: 800x600 pixels (4:3 ratio)

## 🎯 Color Code Reference
- Blue: `#2563eb`
- Purple: `#8b5cf6`
- Green: `#10b981`
- Pink: `#ec4899`
- Orange: `#f97316`
- Red: `#ef4444`
- Teal: `#14b8a6`
- Indigo: `#6366f1`

## ✅ Quick Checklist
- [ ] Choose your colors and update the config
- [ ] Add your photos to the `photos` folder
- [ ] Replace hero photo placeholder
- [ ] Replace about photo placeholder
- [ ] Replace portfolio photo placeholders
- [ ] Save and test your changes

That's it! Your website will look completely personalized with your colors and photos.

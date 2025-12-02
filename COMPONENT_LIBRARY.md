# Modern Component Library & Best Practices

## Quick Reference

This document provides ready-to-use component examples and best practices for the modernized doc@door UI.

## Table of Contents
1. [Layout Components](#layout-components)
2. [Form Components](#form-components)
3. [Button Components](#button-components)
4. [Card Components](#card-components)
5. [Table Components](#table-components)
6. [Alert & Status](#alert--status)
7. [Modal Components](#modal-components)
8. [Navigation Components](#navigation-components)
9. [Best Practices](#best-practices)

---

## Layout Components

### Container Layout
```html
<div class="container mx-auto px-4 lg:px-8 py-8">
    <!-- Full-width content with padding -->
</div>
```

### Grid Layout (2 Columns)
```html
<div class="grid md:grid-cols-2 gap-6">
    <div>Column 1</div>
    <div>Column 2</div>
</div>
```

### Grid Layout (3 Columns)
```html
<div class="grid md:grid-cols-3 lg:grid-cols-4 gap-6">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

### Flex Layout (Horizontal)
```html
<div class="flex items-center justify-between gap-4">
    <div>Left</div>
    <div>Right</div>
</div>
```

### Flex Layout (Vertical)
```html
<div class="flex flex-col gap-3">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

### Hero Section
```html
<div class="bg-gradient-to-r from-primary-600 to-blue-600 rounded-lg p-8 text-white mb-8">
    <h1 class="text-3xl font-bold mb-2">Welcome</h1>
    <p class="text-primary-100">Subtitle text goes here</p>
</div>
```

---

## Form Components

### Form Group
```html
<div class="form-group">
    <label for="email" class="form-label">Email Address</label>
    <input 
        type="email" 
        id="email" 
        class="form-control" 
        placeholder="user@example.com"
        required
    />
</div>
```

### Select Dropdown
```html
<div class="form-group">
    <label for="role" class="form-label">Role</label>
    <select id="role" class="form-control">
        <option value="">Select a role</option>
        <option value="patient">Patient</option>
        <option value="doctor">Doctor</option>
        <option value="admin">Administrator</option>
    </select>
</div>
```

### Textarea
```html
<div class="form-group">
    <label for="message" class="form-label">Message</label>
    <textarea 
        id="message" 
        class="form-control"
        rows="4"
        placeholder="Enter your message..."
    ></textarea>
</div>
```

### File Input
```html
<div class="form-group">
    <label for="file" class="form-label">Upload File</label>
    <input 
        type="file" 
        id="file" 
        class="form-control"
        accept=".pdf,.doc,.docx"
    />
    <p class="text-xs text-gray-500 mt-1">Accepted: PDF, DOC, DOCX</p>
</div>
```

### Checkbox Group
```html
<div class="form-group">
    <div class="flex items-center gap-2">
        <input 
            type="checkbox" 
            id="agree" 
            class="form-control w-4 h-4"
        />
        <label for="agree" class="form-label mb-0">I agree to the terms</label>
    </div>
</div>
```

### Radio Group
```html
<div class="form-group">
    <label class="form-label">Appointment Type</label>
    <div class="space-y-2">
        <div class="flex items-center gap-2">
            <input type="radio" id="virtual" name="type" value="virtual" />
            <label for="virtual">Virtual Consultation</label>
        </div>
        <div class="flex items-center gap-2">
            <input type="radio" id="physical" name="type" value="physical" />
            <label for="physical">Physical Visit</label>
        </div>
    </div>
</div>
```

### Help Text
```html
<div class="form-group">
    <label for="password" class="form-label">Password</label>
    <input type="password" id="password" class="form-control" />
    <p class="text-xs text-gray-500 mt-1">
        Must be at least 8 characters with uppercase and numbers
    </p>
</div>
```

### Error State
```html
<div class="form-group">
    <label for="email" class="form-label">Email</label>
    <input type="email" id="email" class="form-control border-danger" />
    <p class="text-xs text-danger mt-1">
        <i class="fas fa-exclamation-circle mr-1"></i>
        Please enter a valid email address
    </p>
</div>
```

---

## Button Components

### Primary Button
```html
<a href="#" class="btn btn-primary">
    <i class="fas fa-check"></i> Confirm
</a>
```

### Secondary Button
```html
<a href="#" class="btn btn-secondary">
    <i class="fas fa-arrow-left"></i> Back
</a>
```

### Success Button
```html
<a href="#" class="btn btn-success">
    <i class="fas fa-save"></i> Save
</a>
```

### Danger Button
```html
<a href="#" class="btn btn-danger">
    <i class="fas fa-trash"></i> Delete
</a>
```

### Outline Button
```html
<a href="#" class="btn btn-outline">
    <i class="fas fa-file-download"></i> Download
</a>
```

### Small Button
```html
<a href="#" class="btn btn-sm btn-primary">
    <i class="fas fa-edit"></i>
</a>
```

### Large Button
```html
<a href="#" class="btn btn-lg btn-primary w-full">
    <i class="fas fa-sign-in-alt"></i> Sign In
</a>
```

### Disabled Button
```html
<button class="btn btn-primary" disabled>
    <i class="fas fa-spinner fa-spin"></i> Processing...
</button>
```

### Button Group
```html
<div class="flex gap-2">
    <button class="btn btn-primary">Save</button>
    <button class="btn btn-secondary">Cancel</button>
    <button class="btn btn-danger">Delete</button>
</div>
```

---

## Card Components

### Basic Card
```html
<div class="card">
    <div class="card-body">
        Content goes here
    </div>
</div>
```

### Card with Header and Footer
```html
<div class="card">
    <div class="card-header">
        <h3 class="font-semibold">Card Title</h3>
    </div>
    <div class="card-body">
        Main content goes here
    </div>
    <div class="card-footer">
        <a href="#">Learn more →</a>
    </div>
</div>
```

### Card with Gradient Background
```html
<div class="card bg-gradient-to-br from-blue-50 to-cyan-50 border-blue-200">
    <div class="card-body">
        <h4 class="font-semibold text-blue-900">Featured</h4>
        <p class="text-blue-700">Special content</p>
    </div>
</div>
```

### Stat Card
```html
<div class="card">
    <div class="card-body">
        <div class="flex items-center justify-between">
            <div>
                <p class="text-sm text-gray-600">Total Patients</p>
                <p class="text-3xl font-bold text-gray-900 mt-1">1,234</p>
            </div>
            <i class="fas fa-users text-4xl text-blue-400 opacity-20"></i>
        </div>
    </div>
</div>
```

### Action Card
```html
<a href="/appointments/">
    <div class="card hover:shadow-lg hover:border-primary-300 transition">
        <div class="card-body text-center">
            <i class="fas fa-calendar text-3xl text-primary-500 mb-2"></i>
            <p class="font-medium">Appointments</p>
            <p class="text-xs text-gray-500">View your schedule</p>
        </div>
    </div>
</a>
```

---

## Table Components

### Basic Table
```html
<div class="overflow-x-auto">
    <table class="table w-full">
        <thead>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
                <th>Column 3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data 1</td>
                <td>Data 2</td>
                <td>Data 3</td>
            </tr>
        </tbody>
    </table>
</div>
```

### Table with Actions
```html
<div class="overflow-x-auto">
    <table class="table w-full">
        <thead>
            <tr>
                <th>Name</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span class="font-medium">John Doe</span></td>
                <td><span class="badge badge-success">Active</span></td>
                <td>
                    <div class="flex gap-2">
                        <a href="#" class="btn btn-sm btn-info"><i class="fas fa-edit"></i></a>
                        <button class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></button>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</div>
```

---

## Alert & Status

### Success Alert
```html
<div class="mb-6 p-4 bg-green-50 border border-green-200 text-green-800 rounded-lg flex items-start gap-3">
    <i class="fas fa-check-circle flex-shrink-0 mt-0.5"></i>
    <div class="flex-1">Your appointment has been confirmed!</div>
    <button onclick="this.parentElement.style.display='none'" class="text-green-800 hover:text-green-900">
        <i class="fas fa-times"></i>
    </button>
</div>
```

### Error Alert
```html
<div class="mb-6 p-4 bg-red-50 border border-red-200 text-red-800 rounded-lg flex items-start gap-3">
    <i class="fas fa-exclamation-circle flex-shrink-0 mt-0.5"></i>
    <div class="flex-1">An error occurred. Please try again.</div>
    <button onclick="this.parentElement.style.display='none'" class="text-red-800 hover:text-red-900">
        <i class="fas fa-times"></i>
    </button>
</div>
```

### Warning Alert
```html
<div class="p-4 bg-yellow-50 border border-yellow-200 text-yellow-800 rounded-lg flex items-start gap-3">
    <i class="fas fa-exclamation-triangle flex-shrink-0 mt-0.5"></i>
    <div class="flex-1">Please review your information before proceeding.</div>
</div>
```

### Info Alert
```html
<div class="p-4 bg-blue-50 border border-blue-200 text-blue-800 rounded-lg flex items-start gap-3">
    <i class="fas fa-info-circle flex-shrink-0 mt-0.5"></i>
    <div class="flex-1">New features are available. Check them out!</div>
</div>
```

### Badge - Success
```html
<span class="badge badge-success">Active</span>
```

### Badge - Danger
```html
<span class="badge badge-danger">Cancelled</span>
```

### Badge - Warning
```html
<span class="badge badge-warning">Pending</span>
```

### Badge - Info
```html
<span class="badge badge-info">New</span>
```

---

## Modal Components

### Basic Modal
```html
<div id="modal" class="hidden fixed inset-0 bg-black/50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-lg max-w-md w-11/12">
        <div class="flex items-center justify-between px-6 py-4 border-b border-gray-200">
            <h3 class="text-xl font-semibold">Modal Title</h3>
            <button onclick="document.getElementById('modal').classList.add('hidden')" class="text-gray-400 hover:text-gray-900">
                <i class="fas fa-times text-xl"></i>
            </button>
        </div>
        
        <div class="px-6 py-4">
            <p>Modal content goes here</p>
        </div>
        
        <div class="px-6 py-4 border-t border-gray-200 flex gap-3">
            <button onclick="document.getElementById('modal').classList.add('hidden')" class="btn btn-secondary flex-1">
                Cancel
            </button>
            <button class="btn btn-primary flex-1">Confirm</button>
        </div>
    </div>
</div>

<!-- Open Modal Button -->
<button onclick="document.getElementById('modal').classList.remove('hidden')" class="btn btn-primary">
    Open Modal
</button>
```

### Confirmation Modal
```html
<div id="confirm-modal" class="hidden fixed inset-0 bg-black/50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-lg max-w-sm w-11/12">
        <div class="px-6 py-4 border-b border-gray-200">
            <h3 class="text-lg font-semibold flex items-center gap-2">
                <i class="fas fa-exclamation-circle text-warning"></i>
                Confirm Action
            </h3>
        </div>
        
        <div class="px-6 py-4">
            <p class="text-gray-600">Are you sure you want to delete this item? This action cannot be undone.</p>
        </div>
        
        <div class="px-6 py-4 border-t border-gray-200 flex gap-3 justify-end">
            <button onclick="document.getElementById('confirm-modal').classList.add('hidden')" class="btn btn-secondary">
                Cancel
            </button>
            <button class="btn btn-danger">Delete</button>
        </div>
    </div>
</div>
```

---

## Navigation Components

### Top Navigation
```html
<nav class="bg-white border-b border-gray-200 shadow-soft fixed top-0 left-0 right-0 z-40">
    <div class="px-8 py-3 flex items-center justify-between">
        <a href="/" class="flex items-center gap-2 text-xl font-bold text-primary-600">
            <i class="fas fa-clinic-medical"></i>
            <span>doc@door</span>
        </a>
        
        <div class="flex items-center gap-4">
            <a href="/about" class="text-gray-600 hover:text-primary-600">About</a>
            <div class="relative" x-data="{ open: false }">
                <button @click="open = !open" class="flex items-center gap-2 p-2 hover:bg-gray-100 rounded-lg">
                    <div class="w-8 h-8 rounded-full bg-primary-500 flex items-center justify-center text-white text-sm font-semibold">
                        J
                    </div>
                    <span>John</span>
                </button>
                <div @show="open" class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200" x-show="open">
                    <a href="/profile" class="block px-4 py-2 text-gray-700 hover:bg-gray-50">Profile</a>
                    <a href="/logout" class="block px-4 py-2 text-gray-700 hover:bg-gray-50">Logout</a>
                </div>
            </div>
        </div>
    </div>
</nav>
```

### Sidebar Navigation
```html
<aside class="w-64 bg-gradient-to-b from-gray-900 to-gray-800 text-white h-screen overflow-y-auto">
    <nav class="p-6 space-y-2">
        <a href="/profile" class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-700">
            <i class="fas fa-home w-5"></i>
            <span>Dashboard</span>
        </a>
        <a href="/appointments" class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-700 bg-gray-700">
            <i class="fas fa-calendar w-5"></i>
            <span>Appointments</span>
        </a>
        <a href="/messages" class="flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-gray-700">
            <i class="fas fa-envelope w-5"></i>
            <span>Messages</span>
        </a>
    </nav>
</aside>
```

### Tabs
```html
<div x-data="{ activeTab: 'all' }" class="card">
    <div class="border-b border-gray-200 flex">
        <button @click="activeTab = 'all'" :class="{ 'border-b-2 border-primary-600 text-primary-600': activeTab === 'all' }" class="px-6 py-4 font-medium text-gray-600 hover:text-gray-900 border-b-2 border-transparent">
            All
        </button>
        <button @click="activeTab = 'active'" :class="{ 'border-b-2 border-primary-600 text-primary-600': activeTab === 'active' }" class="px-6 py-4 font-medium text-gray-600 hover:text-gray-900 border-b-2 border-transparent">
            Active
        </button>
        <button @click="activeTab = 'archived'" :class="{ 'border-b-2 border-primary-600 text-primary-600': activeTab === 'archived' }" class="px-6 py-4 font-medium text-gray-600 hover:text-gray-900 border-b-2 border-transparent">
            Archived
        </button>
    </div>
    
    <div class="p-6">
        <div x-show="activeTab === 'all'">All content</div>
        <div x-show="activeTab === 'active'">Active content</div>
        <div x-show="activeTab === 'archived'">Archived content</div>
    </div>
</div>
```

---

## Best Practices

### 1. Naming Conventions
- Use descriptive class names
- Follow Tailwind utility naming
- Keep custom class names lowercase with hyphens
- Use semantic names for components

```html
<!-- Good -->
<div class="card">
    <div class="card-header">
        <h2 class="font-semibold">Title</h2>
    </div>
</div>

<!-- Bad -->
<div class="box1">
    <div class="header-section">
        <h2 class="big-text">Title</h2>
    </div>
</div>
```

### 2. Spacing Consistency
- Use the spacing scale consistently
- Group related elements with gap utilities
- Maintain visual hierarchy with spacing

```html
<!-- Good -->
<div class="space-y-4">
    <div class="card">Content 1</div>
    <div class="card">Content 2</div>
    <div class="card">Content 3</div>
</div>

<!-- Bad -->
<div>
    <div class="card" style="margin-bottom: 20px;">Content 1</div>
    <div class="card" style="margin-bottom: 15px;">Content 2</div>
    <div class="card">Content 3</div>
</div>
```

### 3. Color Usage
- Use predefined color palette
- Maintain consistent brand colors
- Follow semantic color meanings

```html
<!-- Good -->
<button class="btn btn-danger">Delete</button>
<button class="btn btn-success">Save</button>
<button class="btn btn-warning">Caution</button>

<!-- Bad -->
<button style="background-color: #FF6B6B;">Delete</button>
<button style="background-color: #51CF66;">Save</button>
<button style="background-color: #FFD93D;">Caution</button>
```

### 4. Responsive Design
- Always design mobile-first
- Use responsive prefixes correctly
- Test on actual devices

```html
<!-- Good -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    <div>Item</div>
</div>

<!-- Bad -->
<div class="grid grid-cols-3 gap-4">
    <div>Item (breaks on mobile)</div>
</div>
```

### 5. Accessibility
- Use semantic HTML
- Provide alt text for images
- Include proper ARIA labels
- Maintain good color contrast

```html
<!-- Good -->
<button class="btn btn-primary" aria-label="Save document">
    <i class="fas fa-save"></i>
</button>

<!-- Bad -->
<div onclick="save()" class="btn btn-primary">
    <i class="fas fa-save"></i>
</div>
```

### 6. Performance
- Minimize custom CSS
- Use utility classes primarily
- Lazy load images
- Cache static assets

```html
<!-- Good -->
<img src="image.jpg" alt="Description" loading="lazy" />

<!-- Bad -->
<img src="image.jpg" alt="">
```

### 7. Maintainability
- Keep templates DRY
- Use includes for repeated sections
- Document complex components
- Add comments for non-obvious code

```html
<!-- Good -->
{% include "shared/card_header.html" %}

<!-- Bad -->
<div class="card">
    <div class="card-header">
        <!-- Repeated 20 times in template -->
    </div>
</div>
```

---

**Remember:** Always prioritize clarity, maintainability, and user experience over quick solutions!

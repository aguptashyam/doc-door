# Virtual Clinic - An Integrated Care System

[![Build Status](https://github.com/mishal23/virtual-clinic/actions/workflows/django.yml/badge.svg)](https://github.com/mishal23/virtual-clinic/blob/master/.github/workflows/django.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/mishal23/virtual-clinic.svg)](https://codecov.io/gh/mishal23/virtual-clinic)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1873/badge)](https://bestpractices.coreinfrastructure.org/projects/1873)

A software to simplify the process of Health Care in hospitals to help the patients, doctor, labs, chemist.

## 🆕 Now with Modern, Responsive UI! ✨

The frontend has been completely redesigned with a modern, professional interface using:
- **Tailwind CSS** - Utility-first CSS framework
- **Alpine.js** - Lightweight JavaScript framework  
- **Responsive Design** - Works perfectly on mobile, tablet, and desktop
- **Modern Components** - Beautiful cards, buttons, forms, and layouts
- **Better UX** - Improved navigation and user experience

👉 **New to the modern UI?** Start with [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)

## 📚 Documentation

### Quick Start
- **[DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)** - Index of all UI documentation
- **[QUICK_START.md](./QUICK_START.md)** - 10-minute getting started guide

### UI & Frontend
- **[MODERN_UI_GUIDE.md](./MODERN_UI_GUIDE.md)** - Design system & components
- **[COMPONENT_LIBRARY.md](./COMPONENT_LIBRARY.md)** - Ready-to-use code examples
- **[MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md)** - Bootstrap 3 → Modern UI migration

### Project Documentation
- **[UI_MODERNIZATION_SUMMARY.md](./UI_MODERNIZATION_SUMMARY.md)** - Complete project overview
- **[docs/INSTALLATION.md](./docs/INSTALLATION.md)** - Setup instructions
- **[docs/DEPLOY.md](./docs/DEPLOY.md)** - Deployment guide

## Introduction

- Everything is well documented, please take a look at [docs](./docs) folder and new UI guides above.
- All the required UML Diagrams are also drawn.
- Steps to setup the project are mentioned [here](./docs/INSTALLATION.md)
- Steps to deploy are mentioned [here](./docs/DEPLOY.md)

## Features:

- **Common Login** for all users
- **Patient Registration**

### Admin

- Add Doctor/Lab/Chemist
- Archive Users
- Restore Archived Users
- Add/Delete Speciality/Symptoms
- Add Hospitals
- View Activity
- View System Statistics
- View/Send Messages
- Update Profile
- Change Password

### Patient

- Create Appointments
- Update Medical Information
- View Prescriptions
- View Medical Tests
- View/Send Messages
- Generate Invoice of Prescription
- Update Profile
- Change Password

### Doctor

- Consult Appointments
- View/Update/Generate Prescriptions
- View Medical Information of patients
- Update Profile
- Change Password

### Lab

- Upload Medical Tests
- View/Send Messages
- Update Profile
- Change Password

### Chemist

- Update Medicine Delivery Status(Update Prescriptions)
- View/Send Messages
- Update Profile
- Change Password

## Structure of Repository

- All the documents are in `docs` folder.
- All the UML Diagrams are in `UML Diagrams` folder.
- UI documentation files (NEW):
  - `DOCUMENTATION_INDEX.md` - Start here for UI docs
  - `QUICK_START.md` - Quick getting started guide
  - `MODERN_UI_GUIDE.md` - Design system documentation
  - `COMPONENT_LIBRARY.md` - Component examples
  - `MIGRATION_GUIDE.md` - Migration instructions
  - `UI_MODERNIZATION_SUMMARY.md` - Project summary
- In the virtualclinic folder
  - `public` folder contains all the templates (now modernized).
  - `server` folder contains the views (business logic).
  - `testing` folder contains all the tests cases.
  - `virtualclinic` folder contains Django configuration files for the project.
  - `server/static/css/modern.css` - Modern UI stylesheet (NEW)

## Technology Stack

### Backend
- **Django 4.2** - Web framework
- **Python 3.8+** - Programming language
- **PostgreSQL/MySQL** - Database

### Frontend (Modernized)
- **Tailwind CSS** - Utility-first CSS framework
- **Alpine.js** - Lightweight JavaScript
- **Font Awesome 6.4** - Icons
- **jQuery 3.7** - DOM/AJAX utilities
- **DataTables** - Advanced tables
- **Flatpickr** - Date/time picker

## Installation & Setup

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/mishal23/virtual-clinic.git
cd virtual-clinic

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

For detailed setup instructions, see [docs/INSTALLATION.md](./docs/INSTALLATION.md)

## Running the Application

```bash
# Development server
python manage.py runserver

# Open in browser
http://localhost:8000
```

## Testing

```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## UI Development

### Working with the Modern UI

1. **Read the documentation** - Start with DOCUMENTATION_INDEX.md
2. **Check existing pages** - See examples in `public/virtualclinic/`
3. **Use component library** - Reference COMPONENT_LIBRARY.md
4. **Test responsiveness** - Use browser DevTools device toolbar
5. **Follow best practices** - See guidelines in UI docs

### Customizing Colors

Edit `public/base.html` Tailwind configuration:
```html
colors: {
    primary: {
        500: '#0ea5e9',  // Sky Blue
        600: '#0284c7',
        700: '#0369a1',
    }
}
```

Also update `server/static/css/modern.css` CSS variables.

### Adding New Components

1. Create template with Tailwind utilities
2. Test on all screen sizes
3. Document in COMPONENT_LIBRARY.md
4. Reference in other pages

## Browser Support

- ✅ Chrome/Edge (Latest 2 versions)
- ✅ Firefox (Latest 2 versions)
- ✅ Safari (Latest 2 versions)
- ✅ Mobile browsers (iOS 12+, Android Chrome latest)

## Performance

- **Tailwind CSS**: ~15KB gzipped
- **Alpine.js**: ~11KB minified
- **Total Bundle**: Smaller than original Bootstrap 3

## Contributing

- The repository is open for contributions from all interested developers.
- Also, you can write by opening an Issue and also solve a current issue if possible.
- Fork this project to your Github account.
- After forking, clone the repository to local system and make the necessary changes.
- Kindly send Pull Requests with explanation as to what changes you have done.
- **New contributors**: Please read UI documentation if modifying frontend

## Feature Requests

- Incase you would like to see a feature to be implemented in this project, please open an issue, or send an email!
- I accept freelancing work to get this project developed and deployed as per your needs.

## License

- The software is under MIT License

---

**Last Updated**: December 2025  
**UI Status**: ✅ Modernized & Complete  
**Documentation**: ✅ Comprehensive

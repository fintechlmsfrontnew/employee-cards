# Employee Digital Cards System

Free hosting solution for 100+ employee profile pages using GitHub Pages.

## Features
- Individual profile pages for each employee
- Mobile-responsive design
- QR code ready links
- Professional business card layout
- Free hosting on GitHub Pages

## Quick Setup

### 1. GitHub Repository Setup
```bash
# Create new repository on GitHub
# Clone it locally
git clone https://github.com/YOUR_USERNAME/employee-cards.git
cd employee-cards
```

### 2. Add Employee Data
Edit `generate-employees.py` and add your 100 employees' data:

```python
employees = [
    {
        "name": "Employee Name",
        "designation": "Job Title",
        "company": "Company Name",
        "phone": "1234567890",
        "email": "email@company.com",
        "website": "company.com",
        "location": "City, State, Country",
        "location_link": "https://maps.google.com/?q=City+State"
    }
    # Add more employees...
]
```

### 3. Generate Pages
```bash
python generate-employees.py
```

### 4. Deploy to GitHub Pages
```bash
git add .
git commit -m "Add employee pages"
git push origin main
```

### 5. Enable GitHub Pages
1. Go to repository Settings
2. Scroll to "Pages" section
3. Source: Deploy from a branch
4. Branch: main
5. Folder: /root
6. Click Save

## File Structure
```
employee-cards/
|-- index.html              # Template
|-- generate-employees.py   # Python script
|-- directory.html          # Main directory page
|-- employees/              # Individual employee pages
|   |-- employee1.html
|   |-- employee2.html
|   |-- ...
|-- README.md              # This file
```

## URLs Structure
- Main Directory: `https://YOUR_USERNAME.github.io/employee-cards/directory.html`
- Employee Pages: `https://YOUR_USERNAME.github.io/employee-cards/employees/employee1.html`

## QR Code Generation
Use any online QR code generator with employee URLs:
- [QR Code Generator](https://www.qr-code-generator.com/)
- [QR Tiger](https://www.qrtiger.com/)

## Customization
- Edit `index.html` to change design
- Modify CSS for different colors/layout
- Add logo and branding

## Benefits
- **100% Free** - No hosting costs
- **Unlimited Pages** - Support for unlimited employees
- **Fast & Reliable** - GitHub's infrastructure
- **Easy Updates** - Simple Git workflow
- **Mobile Ready** - Responsive design

## Support
For issues or questions, check the GitHub repository or contact support.

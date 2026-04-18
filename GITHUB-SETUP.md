# GitHub Upload Process - Step by Step

## Method 1: Easy Way (GitHub Website)

### Step 1: GitHub Repository Banao
1. [github.com](https://github.com) par login karo
2. **"New"** button click karo (green color ka)
3. Repository details fill karo:
   - **Repository name:** `employee-cards`
   - **Description:** `Employee Digital Cards System`
   - **Public:** Yes (zaroori hai GitHub Pages ke liye)
   - **Add a README file:** No (hum already banaye hain)
   - **Add .gitignore:** No
   - **Choose a license:** No

### Step 2: Files Upload Karo
1. Repository banne ke baad, **"uploading an existing file"** link click karo
2. File drag & drop karo ya **"choose your files"** se select karo:
   - `index.html`
   - `directory.html`
   - `generate-employees.py`
   - `README.md`
   - `employees/` folder (poora folder)

3. **"Commit changes"** click karo

---

## Method 2: Git Command Line (Advanced)

### Step 1: Git Install Karo (agar nahi hai)
- Download: [git-scm.com](https://git-scm.com/download/win)

### Step 2: Commands Run Karo
```bash
# GitHub repository clone karo
git clone https://github.com/YOUR_USERNAME/employee-cards.git
cd employee-cards

# Sab files copy karo
# (manual copy karo current folder se repo folder mein)

# Git commands
git add .
git commit -m "Initial commit - Employee cards system"
git push origin main
```

---

## GitHub Pages Enable Karo

### Step 1: Settings mein Jao
1. Repository mein **"Settings"** tab click karo
2. Left side mein **"Pages"** option click karo

### Step 2: Pages Configure Karo
1. **"Source"** section mein:
   - **"Deploy from a branch"** select karo
   - **Branch:** `main`
   - **Folder:** `/root` (default)

2. **"Save"** button click karo

### Step 3: Wait for Deployment
- 2-5 minute wait karo
- GitHub automatically website build karega

---

## Your Website URLs

### Main Directory Page
```
https://YOUR_USERNAME.github.io/employee-cards/directory.html
```

### Individual Employee Pages
```
https://YOUR_USERNAME.github.io/employee-cards/employees/employee1.html
https://YOUR_USERNAME.github.io/employee-cards/employees/employee2.html
...
```

---

## Testing Karo

### Check Karo ki Website Working Hai
1. 5 minute baad URLs open karo
2. Mobile phone se test karo
3. QR code scan karke test karo

### Agar Error Aaye
1. GitHub Pages status check karo
2. File names check karo (lowercase hona chahiye)
3. HTML syntax check karo

---

## 100 Employees ke liye

### Data Add Karo
1. `generate-employees.py` open karo
2. Employees list mein 100 employees ka data add karo:
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
    # 99 more employees...
]
```

### Pages Generate Karo
```bash
python generate-employees.py
```

### GitHub Par Update Karo
```bash
git add .
git commit -m "Added 100 employee pages"
git push origin main
```

---

## QR Codes Generate Karo

### Online Tools Use Karo
1. [QR Code Generator](https://www.qr-code-generator.com/)
2. Har employee ke URL se QR code banao
3. Download karo aur print karo

### Example URLs for QR
```
https://YOUR_USERNAME.github.io/employee-cards/employees/employee1.html
https://YOUR_USERNAME.github.io/employee-cards/employees/employee2.html
```

---

## Troubleshooting

### Common Issues
1. **404 Error:** GitHub Pages properly enable nahi hai
2. **White Screen:** HTML file mein error hai
3. **Images not loading:** Image URLs check karo

### Solutions
1. GitHub Pages status check karo
2. HTML validate karo
3. File paths check karo

---

## Success Checklist

- [ ] GitHub repository banaya hai
- [ ] Sab files upload kiye hain
- [ ] GitHub Pages enable kiya hai
- [ ] Website properly load ho raha hai
- [ ] Mobile friendly hai
- [ ] QR codes ready hain
- [ ] 100 employees ke pages ready hain

**Total Time: 15-20 minutes**

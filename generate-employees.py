import os
import json

# Employee data - aap yahan apne 100 employees ka data dal sakte hain
employees = [
    {
        "name": "Aman Samani",
        "designation": "Product Designer",
        "company": "Fintech Smart Solutions",
        "phone": "7460061609",
        "email": "aman.samani.as@gmail.com",
        "website": "dhanwalle.com",
        "location": "PANCHSHEEL PARK NEW DELHI, DELHI, Delhi, 110017, India",
        "location_link": "https://maps.google.com/?q=PANCHSHEEL+PARK+NEW+DELHI"
    },
    {
        "name": "Rahul Sharma",
        "designation": "Software Developer",
        "company": "Fintech Smart Solutions",
        "phone": "9876543210",
        "email": "rahul.sharma@company.com",
        "website": "company.com",
        "location": "Gurgaon, Haryana, India",
        "location_link": "https://maps.google.com/?q=Gurgaon+Haryana"
    },
    {
        "name": "Priya Patel",
        "designation": "HR Manager",
        "company": "Fintech Smart Solutions",
        "phone": "9876543211",
        "email": "priya.patel@company.com",
        "website": "company.com",
        "location": "Noida, Uttar Pradesh, India",
        "location_link": "https://maps.google.com/?q=Noida+Uttar+Pradesh"
    }
]

def generate_employee_pages():
    # Read template
    with open('index.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Create employees directory
    if not os.path.exists('employees'):
        os.makedirs('employees')
    
    # Generate page for each employee
    for i, emp in enumerate(employees, 1):
        page_content = template
        
        # Replace placeholders
        page_content = page_content.replace('EMPLOYEE_NAME', emp['name'])
        page_content = page_content.replace('EMPLOYEE_DESIGNATION', emp['designation'])
        page_content = page_content.replace('COMPANY_NAME', emp['company'])
        page_content = page_content.replace('EMPLOYEE_PHONE', emp['phone'])
        page_content = page_content.replace('EMPLOYEE_EMAIL', emp['email'])
        page_content = page_content.replace('EMPLOYEE_WEBSITE', emp['website'])
        page_content = page_content.replace('EMPLOYEE_LOCATION', emp['location'])
        page_content = page_content.replace('EMPLOYEE_LOCATION_LINK', emp['location_link'])
        
        # Save employee page
        filename = f'employees/employee{i}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"Generated: {filename} for {emp['name']}")

def generate_index():
    """Generate main index page with all employee links"""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Directory</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .directory-container {
            padding: 50px 20px;
        }
        .employee-card {
            background: white;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .employee-card:hover {
            transform: translateY(-3px);
        }
        .employee-link {
            text-decoration: none;
            color: inherit;
        }
        .employee-link:hover {
            text-decoration: none;
            color: inherit;
        }
        .qr-code {
            width: 80px;
            height: 80px;
            background: #f0f0f0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="directory-container">
            <h1 class="text-center text-white mb-5">Employee Directory</h1>
            <div class="row">
"""
    
    for i, emp in enumerate(employees, 1):
        html += f"""
                <div class="col-md-6 col-lg-4">
                    <a href="employees/employee{i}.html" class="employee-link">
                        <div class="employee-card">
                            <div class="d-flex align-items-center">
                                <div class="qr-code me-3">
                                    QR Code
                                </div>
                                <div>
                                    <h5>{emp['name']}</h5>
                                    <p class="mb-0 text-muted">{emp['designation']}</p>
                                    <small class="text-muted">{emp['company']}</small>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
"""
    
    html += """
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
    
    with open('directory.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Generated: directory.html")

if __name__ == "__main__":
    generate_employee_pages()
    generate_index()
    print("\\nAll employee pages generated successfully!")
    print("Upload these files to GitHub and enable GitHub Pages.")

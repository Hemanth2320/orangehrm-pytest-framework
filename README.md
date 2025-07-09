# orangehrm-pytest-framework
Selenium with Python Pytest Hybrid Framework – OrangeHRM


# OrangeHRM Automation Project – Selenium with Python & Pytest

This is my real-time automation testing project for the OrangeHRM demo website.  
I used Selenium with Python and Pytest Hybrid Framework. This project helped me understand real-world automation framework structure.

---

##  What I Did in This Project

- Used Pytest Hybrid Framework
- Followed Page Object Model (POM) for reusable code
- Automated login and logout functionality
- Added custom logging for tracking test execution
- Took screenshots on test failure
- Generated HTML reports using pytest-html

---

## 🔧 Tools and Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Logging (Python logging module)
- HTML Reporting (pytest-html)
- CSV for test data

---

##  Project Structure

orangehrm-pytest-framework/
├── pom/ → Page classes (login, dashboard)
├── testcases/ → All test cases
├── testdata/ → CSV login data
├── utilities/ → Logger file
├── screenshots/ → Saves screenshots on failure
├── reports/ → Stores HTML reports
├── conftest.py → Sets up browser and logger
├── requirements.txt → Python dependencies
├── pytest.ini → Pytest configuration
└── README.md → Project info 


---

##  How to Run This Project

1. First install all required packages:
In terminal we use this command  pip install -r requirements.txt

Then we will run all test cases with this command:
pytest testcases/ --html=reports/report.html --self-contained-html

## Note for Recruiters
I created this project as a fresher to learn how real automation frameworks work.
I used Selenium with Python and Pytest and followed proper structure like POM, HTML report, logging, and screenshot on failure.
This project helped me understand how automation works in companies.
I did everything by myself to practice and prepare for automation testing jobs.

 ## About Me
Name: Hemanth Dwara
Location: Brodipet, Guntur, Andhra Pradesh
Email: hemanthdwara77@gmail.com
Phone: +91-7569405693
Education: B.Com (2021–2023), Hindu College, ANU University

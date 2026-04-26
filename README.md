![CI](https://github.com/SandChouan/qa-playwright-automation/actions/workflows/ci.yml/badge.svg)

QA Automation Project – Playwright, API Testing & CI/CD

This project demonstrates a complete QA automation setup including UI testing, API testing, CI/CD integration, Docker execution, and advanced reporting.

The goal is to showcase a scalable and maintainable approach to modern test automation.

Test Coverage
🔹 UI Tests (Playwright)
Login functionality (valid & invalid scenarios)
Inventory page validation
Checkout process (end-to-end flow)
🔹 API Tests (Pytest + Requests)
GET endpoints validation
Single resource validation
Response status and data validation

🧩 Architecture
Page Object Model (POM)
Modular structure
Centralized test data management (JSON)

⚙️ Tech Stack
Python
Playwright
Pytest
Requests
Docker
GitHub Actions (CI/CD)
Allure Reports

▶️ Run Tests Locally
pytest
Parallel Execution
pytest -n auto

🐳 Run with Docker
docker build -t qa-tests .
docker run qa-tests

📊 Test Reporting (Allure)
pytest --alluredir=allure-results
allure serve allure-results

🔄 CI/CD Pipeline
Automated test execution on every push
Integrated with GitHub Actions

💡 Key Highlights
End-to-end automation (UI + API)
Parallel test execution
Containerized test environment
Scalable and maintainable architecture

👩‍💻 Author

Sandrine Michele

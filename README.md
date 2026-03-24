![CI](https://github.com/SandChouan/qa-playwright-automation/actions/workflows/ci.yml/badge.svg)

QA Automation Project – Playwright, API Testing & CI/CD


Overview

This project demonstrates a complete QA automation setup including UI testing, API testing, CI/CD integration, Docker execution, and advanced reporting.

Test Coverage
🔹 UI Tests (Playwright)
Login functionality
Inventory page
Checkout process
🔹 API Tests (Pytest + Requests)
GET endpoints validation
Single resource validation


Architecture
Page Object Model (POM)
Modular structure
Centralized test data management (JSON)


⚙️ Tech Stack
Python
Playwright
Pytest
Requests
Docker
GitHub Actions
Allure Reports


Run Tests Locally
pytest

Run Tests in Parallel
pytest -n auto

Run with Docker
docker build -t qa-tests .
docker run qa-tests


Test Reporting (Allure)
pytest --alluredir=allure-results
allure serve allure-results


🔄 CI/CD Pipeline
Automated test execution on every push
GitHub Actions integration


💡 Key Highlights
End-to-end automation (UI + API)
Parallel execution
Containerized test environment
Scalable and maintainable structure


👩‍💻 Author

Sandrine Michele

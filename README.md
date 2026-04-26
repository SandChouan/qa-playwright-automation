![CI](https://github.com/SandChouan/qa-playwright-automation/actions/workflows/ci.yml/badge.svg)

#  QA Automation Project – Playwright, API Testing & CI/CD

##  Overview
This project demonstrates a complete QA automation setup including UI testing, API testing, CI/CD integration, Docker execution, and advanced reporting.

The goal of this project is to demonstrate a scalable QA automation framework that ensures reliability and fast feedback in modern software development.

---

##  Test Coverage

### 🔹 UI Tests (Playwright)
- Login functionality (valid & invalid scenarios)
- Inventory page validation
- Checkout process (end-to-end flow)

### 🔹 API Tests (Pytest + Requests)
- GET endpoints validation
- Single resource validation
- Response status and data validation

---

##  Test Strategy

The testing approach combines UI and API testing to ensure full coverage of critical user flows.

- UI tests validate end-to-end scenarios
- API tests ensure backend reliability
- Automated tests are integrated into CI/CD pipelines for continuous feedback

---

##  Architecture

- Page Object Model (POM)
- Modular structure
- Centralized test data management (JSON)

---

## ⚙️ Tech Stack

- Python
- Playwright
- Pytest
- Requests
- Docker
- GitHub Actions (CI/CD)
- Allure Reports

---

## ▶️ Run Tests 

```bash
pytest

---

## Parallel Execution
```bash
pytest -n auto

---

## 🐳 Run with Docker
```bash
docker build -t qa-tests .
docker run qa-tests

---

## 📊 Test Reporting (Allure)
```bash
pytest --alluredir=allure-results
allure serve allure-results

---

## 🔄 CI/CD Pipeline

Tests are automatically executed via GitHub Actions on every push.

## 💡 Key Highlights
End-to-end automation (UI + API)
Parallel execution
Containerized test environment
Scalable and maintainable structure

## 👩‍💻 Author

Sandrine Michele




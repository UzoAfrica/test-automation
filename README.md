
## `README.md`

```md
# Test Automation Suite – User Management System

This project contains a full-stack automated test suite for a multi-tenant User Management System. It includes:

-  API Testing
-  UI Automation (Selenium)
-  Security Testing
-  Performance Testing (Locust)
-  Reusable test data and HTML report generation

---

##  Folder Structure

```

test-automation/

├── api\_tests/             # API test cases

├── ui\_tests/              # UI workflow & responsiveness

├── security\_tests/        # XSS, SQLi, Auth bypass

├── performance\_tests/     # Load/Stress tests via Locust
├── fixtures/              # Static test data and mock responses
├── utils/                 # Data generators and reporting utils
├── config/                # Pytest & Selenium configurations
├── reports/               # Test run outputs
├── requirements.txt       # Project dependencies
├── pytest.ini             # Test execution configuration
└── TEST\_STRATEGY.md       # Full test methodology

````

---

##  Getting Started

###  Prerequisites

- Python 3.8 or higher
- Google Chrome installed
- ChromeDriver in PATH (for Selenium)
- Internet access to install dependencies

---

###  1. Install Dependencies

```bash
pip install -r requirements.txt
````

Make sure `requirements.txt` includes:

```
pytest
requests
selenium
locust
pytest-html
faker
```

---

##  How to Run Tests

###  API Tests

```bash
pytest api_tests/
```

###  UI Automation Tests

```bash
pytest ui_tests/
```


###  Security Tests

```bash
pytest security_tests/
```

###  Performance Tests with Locust

```bash
# Load test 100 users for 1 minute
locust -f performance_tests/load_test.py --headless -u 100 -r 10 -t 1m --host=http://localhost:8000
```

---

##  Test Reports

Run any test suite with HTML report generation:

```bash
pytest --html=reports/test_report.html --self-contained-html
```

All reports are saved under `/reports`.

---

##  Test Data

Reusable test data is located in `/fixtures/`:

* `test_data.json` — API request payloads
* `mock_responses.json` — fallback responses for mocking
* `security_test_data.json` — payloads for XSS/SQLi testing

---

##  Useful Commands

| Action               | Command                                    |
| -------------------- | ------------------------------------------ |
| Run all tests        | `pytest`                                   |
| Run specific file    | `pytest api_tests/test_users.py`           |
| Marked tests only    | `pytest -m regression`                     |
| Generate HTML report | `pytest --html=report.html`                |
| Run Locust load test | `locust -f performance_tests/load_test.py` |

---

##  Contributor

* **QA Engineer:** Ibezim Uzoma Joseph

---


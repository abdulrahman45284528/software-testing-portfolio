# Software Testing Portfolio

Hands-on QA portfolio demonstrating **manual testing**, **API testing**, and **test automation** using **Pytest** and **Playwright**.  
This repository is built to show practical testing skills with real artifacts (test plan, bug reports, automated tests, and project structure).

## What’s Inside

### ✅ Manual Testing (`manual_testing/`)
- Test plan
- Test scenarios / test cases
- Bug reports (with steps, expected vs actual, severity)

### ✅ API Testing (`api_testing/`)
- Postman collection(s)
- API test notes / documentation (requests, responses, validations)

### ✅ Automation – Pytest (`automation/pytest/`)
- Python unit tests using **Pytest**
- Examples: assertions, fixtures, parametrization, exceptions, skipping/xfail
- Mini project: **Shopping Cart** tests
## Latest Test Run (Pytest)

- Command: `pytest -v`
- Result: **23 passed, 3 skipped**
- Location: `automation/pytest/`


### ✅ UI Automation – Playwright (`playwright/`)
- UI automation setup using **Playwright**
- Configuration + test structure for browser testing

---

## Tools & Tech
- **Python 3.12.2**
- **Pytest**
- **Playwright**
- **Postman**
- **Git / GitHub**

---

## How to Run

### 1) Clone the repository
```bash
git clone https://github.com/abdulrahman45284528/software-testing-portfolio.git
cd software-testing-portfolio
2) Run Pytest tests
Go to the Pytest project folder:

bash
Copy code
cd automation/pytest
Install dependencies (pip install pytest):

bash
Copy code
pip install -r requirements.txt
Run all tests:

bash
Copy code
pytest -v
Run a single test file:

bash
Copy code
pytest -v tests/test_shopping_cart.py
Run one specific test:

bash
Copy code
pytest -v tests/test_shopping_cart.py::test_can_add_item_to_cart
Run tests by name pattern:

bash
Copy code
pytest -k "shopping_cart"


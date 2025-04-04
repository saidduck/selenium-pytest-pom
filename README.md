# Selenium Pytest POM Framework

This project is an automation framework for testing the login functionality of the OrangeHRM demo site using Selenium, Pytest, and the Page Object Model (POM) design pattern.

## Project Structure

```
selenium-pytest-pom
├── pages
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
├── tests
│   ├── __init__.py
│   ├── test_login.py
├── utils
│   ├── __init__.py
│   └── config.py
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/saidduck/selenium-pytest-pom.git
   cd selenium-pytest-pom
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the tests:**
   You can execute the test suite using the following command:
   ```
   pytest --html=report.html --self-contained-html
   ```

## Usage

- The framework is designed to test the login functionality of the OrangeHRM demo site.
- The `tests/test_login.py` file contains test cases for both successful and unsuccessful login attempts.
- The `pages` directory contains page object classes that encapsulate the interactions with the web pages.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
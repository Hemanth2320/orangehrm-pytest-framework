import pytest
from selenium import webdriver
from utilities.logger import setup_logger
import os

@pytest.fixture(scope="class")
def setup(request):
    logger = setup_logger()
    logger.info("Starting ChromeDriver")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.logger = logger
    yield
    logger.info("Quitting browser")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            driver = item.cls.driver
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(screenshot_path)
        except Exception as e:
            print("Screenshot error:", e)

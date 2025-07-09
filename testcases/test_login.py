import pytest
from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        self.logger.info("Test: Valid Admin Login")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        dashboard = DashboardPage(self.driver)
        assert dashboard.is_dashboard_displayed()
        self.logger.info("Login successful, Dashboard loaded")

    def test_logout(self):
        dashboard = DashboardPage(self.driver)
        dashboard.logout()
        self.logger.info("Logged out successfully")

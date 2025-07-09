from selenium.webdriver.common.by import By
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_text = By.XPATH, "//h6[text()='Dashboard']"
        self.profile_icon = By.CLASS_NAME, "oxd-userdropdown-name"
        self.logout_link = By.XPATH, "//a[text()='Logout']"

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.dashboard_text).is_displayed()

    def logout(self):
        self.driver.find_element(*self.profile_icon).click()
        self.driver.find_element(*self.logout_link).click()

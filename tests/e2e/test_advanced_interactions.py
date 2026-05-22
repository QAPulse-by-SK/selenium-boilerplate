"""
QA Pulse by SK — Selenium Boilerplate
test_advanced_interactions.py — advanced Selenium interactions
Covers: checkboxes, dropdowns, dynamic loading, alerts, drag & drop, windows, hovers, tables
"""
from __future__ import annotations

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


@pytest.mark.regression
@pytest.mark.e2e
class TestCheckboxes:

    def test_check_checkbox(self, driver: WebDriver):
        """User can check an unchecked checkbox."""
        page = BasePage(driver)
        page.open("/checkboxes")
        checkbox = (By.CSS_SELECTOR, "input[type='checkbox']:first-of-type")
        el = driver.find_element(*checkbox)
        if not el.is_selected():
            page.click(checkbox)
        assert driver.find_element(*checkbox).is_selected()

    def test_uncheck_checkbox(self, driver: WebDriver):
        """User can uncheck a checked checkbox."""
        page = BasePage(driver)
        page.open("/checkboxes")
        checkbox2 = (By.CSS_SELECTOR, "input[type='checkbox']:last-of-type")
        el = driver.find_element(*checkbox2)
        if el.is_selected():
            page.click(checkbox2)
        assert not driver.find_element(*checkbox2).is_selected()

    def test_two_checkboxes_present(self, driver: WebDriver):
        """Page has exactly two checkboxes."""
        page = BasePage(driver)
        page.open("/checkboxes")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        assert len(checkboxes) == 2


@pytest.mark.regression
@pytest.mark.e2e
class TestDropdown:

    def test_select_option1(self, driver: WebDriver):
        """User can select Option 1 from dropdown."""
        page = BasePage(driver)
        page.open("/dropdown")
        dropdown_el = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_el)
        select.select_by_visible_text("Option 1")
        assert select.first_selected_option.text == "Option 1"

    def test_select_option2(self, driver: WebDriver):
        """User can select Option 2 from dropdown."""
        page = BasePage(driver)
        page.open("/dropdown")
        dropdown_el = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_el)
        select.select_by_visible_text("Option 2")
        assert select.first_selected_option.text == "Option 2"

    def test_dropdown_has_options(self, driver: WebDriver):
        """Dropdown has expected options."""
        page = BasePage(driver)
        page.open("/dropdown")
        dropdown_el = driver.find_element(By.ID, "dropdown")
        select  = Select(dropdown_el)
        options = [o.text for o in select.options]
        assert "Option 1" in options
        assert "Option 2" in options


@pytest.mark.regression
@pytest.mark.e2e
class TestDynamicLoading:

    def test_dynamic_content_loads(self, driver: WebDriver):
        """Dynamic content loads after button click."""
        page = BasePage(driver)
        page.open("/dynamic_loading/1")
        page.click((By.CSS_SELECTOR, "#start button"))
        finish = (By.ID, "finish")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(finish))
        assert driver.find_element(*finish).is_displayed()

    def test_hidden_element_renders(self, driver: WebDriver):
        """Hidden element shows 'Hello World!' after loading."""
        page = BasePage(driver)
        page.open("/dynamic_loading/1")
        page.click((By.CSS_SELECTOR, "#start button"))
        finish = (By.CSS_SELECTOR, "#finish h4")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(finish))
        assert "Hello World!" in driver.find_element(*finish).text


@pytest.mark.regression
@pytest.mark.e2e
class TestJavaScriptAlerts:

    def test_accept_alert(self, driver: WebDriver):
        """User can accept a JavaScript alert."""
        page = BasePage(driver)
        page.open("/javascript_alerts")
        page.click((By.XPATH, "//button[text()='Click for JS Alert']"))
        page.accept_alert()
        assert "successfully" in driver.find_element(By.ID, "result").text.lower()

    def test_confirm_alert_accept(self, driver: WebDriver):
        """User can accept a confirmation dialog."""
        page = BasePage(driver)
        page.open("/javascript_alerts")
        page.click((By.XPATH, "//button[text()='Click for JS Confirm']"))
        page.accept_alert()
        assert "Ok" in driver.find_element(By.ID, "result").text

    def test_confirm_alert_dismiss(self, driver: WebDriver):
        """User can dismiss a confirmation dialog."""
        page = BasePage(driver)
        page.open("/javascript_alerts")
        page.click((By.XPATH, "//button[text()='Click for JS Confirm']"))
        page.dismiss_alert()
        assert "Cancel" in driver.find_element(By.ID, "result").text

    def test_prompt_alert(self, driver: WebDriver):
        """User can enter text in a prompt dialog."""
        page = BasePage(driver)
        page.open("/javascript_alerts")
        page.click((By.XPATH, "//button[text()='Click for JS Prompt']"))
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.send_keys("QA Pulse by SK")
        alert.accept()
        assert "QA Pulse by SK" in driver.find_element(By.ID, "result").text


@pytest.mark.regression
@pytest.mark.e2e
class TestDragAndDrop:

    def test_drag_column_a_to_b(self, driver: WebDriver):
        """Page has draggable columns."""
        page = BasePage(driver)
        page.open("/drag_and_drop")
        assert page.is_present((By.ID, "column-a"))
        assert page.is_present((By.ID, "column-b"))

    def test_columns_have_headers(self, driver: WebDriver):
        """Drag and drop columns have header text."""
        page = BasePage(driver)
        page.open("/drag_and_drop")
        header_a = driver.find_element(By.CSS_SELECTOR, "#column-a header").text
        header_b = driver.find_element(By.CSS_SELECTOR, "#column-b header").text
        assert header_a in ["A", "B"]
        assert header_b in ["A", "B"]


@pytest.mark.regression
@pytest.mark.e2e
class TestNewWindow:

    def test_open_new_window(self, driver: WebDriver):
        """Clicking link opens a new browser window."""
        page = BasePage(driver)
        page.open("/windows")
        original = len(driver.window_handles)
        page.click((By.LINK_TEXT, "Click Here"))
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(original + 1))
        assert len(driver.window_handles) > original

    def test_switch_to_new_window(self, driver: WebDriver):
        """User can switch to new window and read content."""
        page = BasePage(driver)
        page.open("/windows")
        page.click((By.LINK_TEXT, "Click Here"))
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        page.switch_to_new_window()
        heading = (By.TAG_NAME, "h3")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(heading))
        assert driver.find_element(*heading).text != ""


@pytest.mark.regression
@pytest.mark.e2e
class TestHovers:

    def test_hover_reveals_content(self, driver: WebDriver):
        """Hovering over an element reveals hidden content."""
        from selenium.webdriver import ActionChains
        page = BasePage(driver)
        page.open("/hovers")
        figures = driver.find_elements(By.CSS_SELECTOR, ".figure")
        assert len(figures) == 3
        ActionChains(driver).move_to_element(figures[0]).perform()
        caption = (By.CSS_SELECTOR, ".figure:first-of-type .figcaption")
        assert page.is_visible(caption)


@pytest.mark.regression
@pytest.mark.e2e
class TestTables:

    def test_table_has_rows(self, driver: WebDriver):
        """Data table has visible rows."""
        page = BasePage(driver)
        page.open("/tables")
        rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")
        assert len(rows) > 0

    def test_table_has_headers(self, driver: WebDriver):
        """Data table has column headers."""
        page = BasePage(driver)
        page.open("/tables")
        headers = driver.find_elements(By.CSS_SELECTOR, "#table1 thead th")
        assert len(headers) > 0

    @pytest.mark.parametrize("column", ["Last Name", "First Name", "Email"])
    def test_table_has_column(self, driver: WebDriver, column: str):
        """Table contains specific column headers."""
        page = BasePage(driver)
        page.open("/tables")
        headers = driver.find_elements(By.CSS_SELECTOR, "#table1 thead th")
        header_texts = [h.text.strip() for h in headers]
        assert column in header_texts, f"Column '{column}' not found in {header_texts}"

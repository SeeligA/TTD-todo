from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        """Special method for test prerequisites."""
        self.browser = webdriver.Chrome()

    def tearDown(self):
        """
        Special method for clean-up steps.

        Note that this method will run even in case of an exception
        and unless the exception occurs at self.setUp().
        """
        self.browser.quit()

    def test_can_start_and_retrieve_list(self):
        # User opens browser to visit website
        self.browser.get("http://localhost:8000")
        # There is a page title and title mentions "To-Do"
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # When writing "Select VCS" into a text box
        inputbox.send_keys('Select VCS')
        # and hitting ENTER
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_name('tr')
        self.assertTrue(
            any(row.text == '1: Select VCS' for row in rows),
            "New to-do item did not appear in table"
        )
        # And hitting Enter, the page updates. Now the
        # page shows "1. Select VSC" as an to-do item

        # When writing another item ("Install VCS")
        # in the text box below...
        self.fail("Finish the test!")
        # ... the list update again, now showing both items

        # Will the site remember those items? THe URL shows
        # a unique URL for the user - some text provides
        # additional details

        # WHen visiting the URl, the items are still there.


if __name__ == "__main__":
    unittest.main(warnings="ignore")

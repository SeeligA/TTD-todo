from selenium import webdriver
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
        # The page title mentions "KERN"
        self.assertIn("KERN", self.browser.title)
        self.fail("Finish the test!")
        # Enter a to-do item straight away

        # When writing "Select VCS" into a text box

        # And hitting Enter, the page updates. Now the
        # page shows "1. Select VSC" as an to-do item

        # When writing another item ("Install VCS")
        # in the text box below...

        # ... the list update again, now showing both items

        # Will the site remember those items? THe URL shows
        # a unique URL for the user - some text provides
        # additional details

        # WHen visiting the URl, the items are still there.


if __name__ == "__main__":
    unittest.main(warnings="ignore")

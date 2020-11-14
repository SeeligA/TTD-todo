from selenium import webdriver

browser = webdriver.Chrome()
# Open browser to visit website
browser.get('http://localhost:8000')
# The page title mentions "KERN"
assert 'KERN' in browser.title

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


browser.quit()

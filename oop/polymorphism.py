# Class for Chrome browser
class Chrome: #defined a class named chrome
    def run_test(self): #method inside chrome class
        print("Running test on Chrome browser...") #specific msg for chrome

# Class for Firefox browser
class Firefox:
    def run_test(self):
        print("Running test on Firefox browser...")

# Creating an objects of each class
chrome_browser = Chrome()
firefox_browser = Firefox()

# Calling run_test() methods on diffn objects
chrome_browser.run_test() #calls chrome run_test
firefox_browser.run_test()



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\NDiaz\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver

# #PERFORMANCE Caps
# caps = DesiredCapabilities.CHROME
# caps['loggingPrefs'] = {'performance': 'ALL'}

# # url3='https://app.powerbi.com/groups/me/apps/b29a0ea9-dd6d-433a-a415-bc3fecd96db8/reports/788dbea5-e2be-4b69-82a0-eec132bdb2f6/'
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=options, desired_capabilities=caps)
# time.sleep(3)
# driver.execute_script("window.open('https://app.powerbi.com/groups/me/apps/b29a0ea9-dd6d-433a-a415-bc3fecd96db8/reports/788dbea5-e2be-4b69-82a0-eec132bdb2f6/');") 
# # driver.get("https://app.powerbi.com/groups/me/apps/b29a0ea9-dd6d-433a-a415-bc3fecd96db8/reports/788dbea5-e2be-4b69-82a0-eec132bdb2f6/")
# driver.close()



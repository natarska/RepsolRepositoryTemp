from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

user = "NDiaz"

if user == "NDiaz":
    userprofile = "C:\\Users\\NDiaz\\AppData\\Local\\Google\\Chrome\\User Data"  
    pathlogpath = "selenium_logs.log"
    tracejsonpath="trace.json"  
    pathjson = "timings.json"
else:
    userprofile = "C:\\Users\\fjmercado\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
    pathlogpath = "C:\\Users\\fjmercado\\Repsol\\IAMS 1.0 - PBI Files\\PERFORMANCE\\AutomatedFramework\\NetworkLogs\\selenium_logs.log"
    tracejsonpath="C:\\Users\\fjmercado\\Repsol\\IAMS 1.0 - PBI Files\\PERFORMANCE\\AutomatedFramework\\NetworkLogs\\trace.json"
    pathjson = "C:\\Users\\fjmercado\\Repsol\\IAMS 1.0 - PBI Files\\PERFORMANCE\\AutomatedFramework\\NetworkLogs\\timings.json"


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir="+userprofile) #Path to your chrome profile https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver

#PERFORMANCE Caps
caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}
caps['chromeOptions'] = {
    "args" : ['--enable-gpu-benchmarking', '--enable-thread-composting'],
    "perfLoggingPrefs" : {
      "traceCategories": "toplevel,disabled-by-default-devtools.timeline.frame,blink.console,disabled-by-default-devtools.timeline,benchmark"
    }
  } 

# options2 = webdriver.ChromeOptions()
options.add_argument("user-data-dir="+userprofile) #Path to your chrome profile https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver



driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=options, desired_capabilities=caps, service_args=["--verbose", "--log-path="+pathlogpath] )
# driver2 = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=options, desired_capabilities=caps, service_args=["--verbose", "--log-path="+pathlogpath] )

#time.sleep(3)

#driver.get_network_conditions
#driver.get_screenshot_as_file

link = "https://app.powerbi.com/groups/me/apps/a6350816-681c-4614-bfb1-622f482db12d/reports/bffafdb8-da13-43b2-8abc-9c6c90226470/ReportSectiondc1f6a0104bd70ce61ea"

driver.switch_to_window("$(window.window_handles[-1]))") 
driver.get(link)
# driver.execute_script("window.open('"+link+"');")

driver.switch_to_window("$(window.window_handles[0]))") 
driver.get(link)

# Switch to new window
# driver.switch_to_window(driver.window_handles[-1])
# print " Twitter window should go to facebook "
# print "New window ", driver.title
# driver.get("http://facebook.com")
# print "New window ", driver.title
# driver3.execute_script("window.open('"+link+"');")



##time.sleep(10)
# timings = driver.execute_script("return window.performance.getEntries();")
# print(timings)
# with open(pathjson, 'w') as outfile:
#     json.dump(timings, outfile)


# print(driver.log_types)
# for entry in driver.get_log('performance'):
#     print(entry)

# # generate a trace file loadable in chrome://tracing   url: https://stackoverflow.com/questions/36227512/how-to-use-trace-json-written-by-chromedriver
# with open(tracejsonpath, 'w') as f:
#     f.write(json.dumps([json.loads(d['message'])['message']['params'] for d in driver.get_log('performance')]))

#time.sleep(40)
#driver.close()
#driver.quit()





# print(type(driver.get_log('performance')))

#driver.navigate().to("https://app.powerbi.com/groups/me/apps/b29a0ea9-dd6d-433a-a415-bc3fecd96db8/reports/788dbea5-e2be-4b69-82a0-eec132bdb2f6/") 



# return True if element is visible within 30 seconds, otherwise False 
# def is_visible(locator, timeout = 30): 
#     try: 
#         ui.WebDriverWait(chrome, timeout).until(EC.visibility_of_element_located((By.XPATH, locator))) 
#         return True
#     except TimeoutException: 
#         return False

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source


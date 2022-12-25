from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()


def login():
    username = driver.find_element(By.CSS_SELECTOR, 'input.gwt-TextBox.GDPVGE1BM2B')
    username.send_keys("wd-implementer")

    password = driver.find_element(By.CSS_SELECTOR, 'input.gwt-PasswordTextBox.GDPVGE1BM2B')
    password.send_keys("!l0v3WDAY")

    login = driver.find_element(By.XPATH, "//div[@class = 'GDPVGE1BLTC']/button")
    login.click()

def busqueda(tarea):
    driver.implicitly_wait(20)
    search = driver.find_element(By.XPATH, "//div[@id = 'wd-searchInput']/input")

    driver.implicitly_wait(20)
    action = ActionChains(driver)
    action.click(on_element = search)
    action.send_keys(tarea)
    action.send_keys(Keys.RETURN)
    action.perform()
    driver.implicitly_wait(20)
    task = driver.find_element(By.XPATH, "//a[text()='"+tarea+"']")
    task.click()
    
def BODetails(bo):
    driver.implicitly_wait(20)
    boDetails = driver.find_element(By.XPATH, "//input[@id = '56$235426--uid6-input']")
    action = ActionChains(driver)
    action.click(on_element = boDetails)
    action.send_keys(bo)
    action.send_keys(Keys.ENTER)

    

def submit():
    driver.implicitly_wait(10)
    submit = driver.find_element(By.XPATH, "//div[@class = 'WM-N WEAJ WB2I']")
    action = ActionChains(driver)
    action.click(on_element = submit)
    action.perform()
    submit.click()
    
def nextBtn():
    nextBtn = driver.find_element(By.XPATH, "//button[@class = 'WBGN WASO WB-N WIHN WFGN']")
    action = ActionChains(driver)
    action.click(on_element = nextBtn)
    action.perform()
    nextBtn.click()
    

#driver.set_page_load_timeout(30)
driver.implicitly_wait(20)
driver.get("https://impl.workday.com/bnb_dpt1/d/pex/home.htmld?")

login()
busqueda("Business Object details")
'''
nameEIB = driver.find_element(By.XPATH, "//input[@id = '56$341582--uid7-input']")
nameEIB.send_keys('EIB CS Test')
dir = 'Outbound'

if dir == 'Outbound':
    direccion = driver.find_element(By.XPATH, "//input[@id = 'gwt-uid-3']")
else:
    direccion = driver.find_element(By.XPATH, "//input[@id = 'gwt-uid-2']")

driver.implicitly_wait(20)
direccion.click()
driver.implicitly_wait(10)
submit()
driver.implicitly_wait(10)
nextBtn()

data = "Web Service"
selector = driver.find_element(By.XPATH, "//div[@class = 'WHF0']")
action = ActionChains(driver)
action.click(on_element = selector)
action.perform()
selector.click()

if data == 'Web Service':
    tipoData = driver.find_element(By.XPATH, "//div[@class = 'WAIR WMHR WCHR WJIR']")
    driver.implicitly_wait(10)
    tipoData.click()

'''







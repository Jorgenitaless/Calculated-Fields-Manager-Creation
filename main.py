import sys
import os
import Functions as ft
from selenium import webdriver

driver = webdriver.Chrome()
business_objects = []

ft.list_creation(business_objects)

ft.start(driver)
ft.login(driver)
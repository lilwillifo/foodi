from splinter.browser import Browser
from selenium import webdriver

browser = Browser('chrome')
browser.visit('http://localhost:8000')
browser.fill('query', 'apple')
browser.find_by_name('query').click()

if browser.is_text_present('Apple'):
    print("Yas!")
else:
    print("Naw")

browser.quit()

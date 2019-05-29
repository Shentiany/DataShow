from selenium import webdriver
import time

url = 'http://gjcxcy.bjtu.edu.cn/LXItemList.aspx'
namelist = []
browser = webdriver.Chrome()
browser.get(url)

for x in range(1524):
    names = browser.find_elements_by_xpath('//div[@class="List_Nrz FL"]/a')
    for name in names:
        namelist.append(name.text)
    next_page = browser.find_element_by_xpath('//*[contains(text(),"下一页")]')
    next_page.click()
    time.sleep(3)

with open('data.txt', 'a') as file:
    for n in namelist:
        file.write(n+'\n')

browser.close()
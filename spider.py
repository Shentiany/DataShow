from selenium import webdriver
from lxml import etree
import requests
import time
import json

def get_detail_page(page,url, xpath_of_a, xpath_of_next_page):
    browser = webdriver.Chrome()
    browser.get(url)
    href_list = []
    for _ in range(page-1):
        urls_of_detail_page = browser.find_elements_by_xpath(xpath_of_a)
        for url_of_detail_page in urls_of_detail_page:
            href = url_of_detail_page.get_attribute('href')
            href_list.append(href)
        next_page = browser.find_element_by_xpath(xpath_of_next_page)
        next_page.click()
        time.sleep(1)
    browser.close()
    return href_list

def get_detail_info(href_list):
    item = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
    }
    for href in href_list:
        response = requests.get(href, headers=headers)
        html = etree.HTML(response.text)
        item['name'] = html.xpath('normalize-space(//*[contains(text(),"项目名称")]/text())').replace('项目名称：', '')
        item['key_word']= html.xpath('normalize-space(//*[contains(text(),"关键词")]/text())').replace('项目关键词：', '')
        item['project_type'] = html.xpath('normalize-space(//*[contains(text(),"项目类型")]/text())').replace('项目类型：', '')
        item['school_name'] = html.xpath('normalize-space(//*[contains(text(),"所属学校")]/text())').replace('所属学校：', '')
        item['discipline_one'] = html.xpath('normalize-space(//*[contains(text(),"所属一级学科")]/text())').replace('所属一级学科：', '')
        item['discipline_two'] = html.xpath('normalize-space(//*[contains(text(),"所属二级学科")]/text())').replace('所属二级学科：', '')
        item['time'] = html.xpath('normalize-space(//*[contains(text(),"立项时间")]/text())').replace('立项时间：', '')
        item['money'] = html.xpath('normalize-space(//*[contains(text(),"批准经费额度")]/text())').replace('批准经费额度：', '')
        item['number_of_participants'] = int(html.xpath('count(//table[@class="table-itemstu"]//tr)-1'))
        change_item = json.dumps(item, ensure_ascii=False)
        with open('item.txt', 'a+') as file:
                file.write(change_item)

if __name__ == '__main__':

    url = 'http://gjcxcy.bjtu.edu.cn/LXItemList.aspx'
    xpath_of_a = '//div[@class="List_Nrz FL"]/a'
    xpath_of_next_page = '//*[contains(text(),"下一页")]'
    page = 1577

    href_list = get_detail_page(page, url, xpath_of_a, xpath_of_next_page)
    get_detail_info(href_list)
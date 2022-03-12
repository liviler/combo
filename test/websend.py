#引入selenium库中的 webdriver 模块
from anyio import BrokenWorkerProcess
from selenium import webdriver
import time
#打开谷歌浏览器
browser = webdriver.Edge(r'C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe')
#打开百度搜索主页
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
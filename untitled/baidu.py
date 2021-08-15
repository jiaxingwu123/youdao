from datetime import time
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
def click_locxy(dr, x, y, left_click=True):
    '''
    dr:浏览器
    x:页面x坐标
    y:页面y坐标
    left_click:True为鼠标左键点击，否则为右键点击
    '''
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前
dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
dr.maximize_window()
dr.find_element_by_id("kw").send_keys("1314Woaini!")
time.sleep(3)

click_locxy(dr,774,33)  # 鼠标左键点击， 200为x坐标， 100为y坐标

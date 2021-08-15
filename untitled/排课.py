import time
import datetime

import datetime as datetime
import selenium
from appium.webdriver.extensions.search_context import windows
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

global driver
driver=selenium.webdriver.Chrome()
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

def login(account,password,url):
    driver.get(url)
    driver.find_element_by_xpath("//*[@onclick=\"corp()\"]").click()   # 模拟鼠标点击查询按钮
    driver.find_element_by_id("corp_id_for_corpid").send_keys(account)
    driver.find_element_by_id("corp_id_for_corppw").send_keys(password)
    driver.maximize_window()
    driver.execute_script('window.scrollBy(0,500)')
    click_locxy(driver,650,435)
    #driver.find_element_by_xpath("//span[@class=\"anticon anticon-read\"]").click()

def create_Xbk(account,password,url):
    login(account,password,url)
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href=\"#/manageTeach/formalCourse\"]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[@class=\"anticon anticon-plus\"]").click()
    time.sleep(2)
    driver.find_element_by_id("courseName").send_keys("众测")
    driver.find_element_by_xpath("//input[@value=\"0\"]").click()
    driver.find_element_by_xpath("//div[@class=\"rc-virtual-list-holder-inner\"]/div/div").click()
    driver.find_element_by_xpath("//div[text()=\"3岁\"]").click()
    driver.find_element_by_xpath("//input[@value=\"2\"]").click()
    driver.find_element_by_id("deductLessonPeriod").click()
    driver.find_element_by_xpath("//div[@title=\"0.5课时\"]").click()
    time.sleep(3)
    driver.find_element_by_id("firstCharge").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@title=\"5课时\"]").click()
    driver.execute_script('window.scrollBy(0,500)')
    driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]").click()

def create_Dbk(account,password,url):
    driver.get(url)
    login(account, password, url)
    time.sleep(2)
    driver.find_element_by_xpath("//ul[@class=\"nav nav-list\"]/li[3]//span").click()
    driver.find_element_by_xpath("//a[@href=\"/view/course/list\"]").click()
    driver.find_element_by_id("keyword").send_keys("wjx")
    driver.find_element_by_xpath("//span[@class=\"input-group-btn\"]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href=\"/view/course/edit/edit?courseId=35165\"]").click()
    time.sleep(3)
    a=driver.find_element_by_xpath("//div[@class=\"col-xs-7\"]/input").text
    print(a)
    #driver.find_element_by_xpath("//button[@title=\"将当前页面的改动保存到【线下】数据库中\"]").click()

def yue_Ke(account, password, url):
    driver.get(url)
    login(account, password, url)
    driver.get("https://xiaobanke-admin.youdao.com/#/manageTeach/experienceCourse/setCourse/student?courseId=2245")
    driver.implicitly_wait(20)
    while(True):

        #driver.find_element_by_xpath("//li[@class=\"ant-pagination-next\"]").click()
        #driver.execute_script('window.scrollBy(0,600)')
        for i in range(1,11):
            print(i)

            time.sleep(2)
            driver.find_element_by_xpath("//div[@class=\"ant-collapse-item\"]["+str(i)+"]//button").click()

            time.sleep(2)
            driver.find_element_by_xpath("//span[@class=\"ant-select-selection-search\"]/input[@id=\"lessonId\"]").click()


            time.sleep(2)
            next_btn=driver.find_element_by_xpath("//div[@class=\"ant-select-item-option-content\"]")
            driver.execute_script("arguments[0].click();", next_btn)

            time.sleep(2)
            driver.find_element_by_xpath("//input[@id=\"wantedDay\"]").click()


            time.sleep(2)
            driver.find_element_by_xpath("//div[@class=\"ant-picker-footer\"]/a").click()


            driver.find_element_by_xpath("//input[@placeholder=\"开始时间\"]").click()
            driver.find_element_by_xpath("//ul[@class=\"ant-picker-time-panel-column\"][1]//div[text()=\"00\"]").click()
            driver.find_element_by_xpath("//li[@class=\"ant-picker-ok\"]").click()
            driver.find_element_by_xpath("//ul[@class=\"ant-picker-time-panel-column\"][1]//div[text()=\"00\"]").click()
            driver.find_element_by_xpath("//li[@class=\"ant-picker-ok\"]").click()
            driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]").click()
            if i==10:
                driver.find_element_by_xpath("//li[@class=\"ant-pagination-next\"]").click()



def buy_Class(list,url):
    while True:
        driver.get(url)
        driver.find_element_by_id("hd-notlogin").click()
        driver.maximize_window()
        time.sleep(4)
        click_locxy(driver, 754, 210)
        if list:
            re = list.pop()
            phone = re[0]
            password = re[1]
            print(phone)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[starts-with(@id,\"x-URS-iframe\")]"))
        driver.find_element_by_xpath("//input[@placeholder=\"请输入手机号码\"]").send_keys(phone)
        driver.find_element_by_xpath("//input[@placeholder=\"请输入密码\"]").send_keys(password)
        driver.find_element_by_id("submitBtn").click()
        time.sleep(3)
        try:
            driver.find_element_by_xpath("//div[@class=\"ct\"]").click()
            driver.find_element_by_xpath("//div[@class=\"opt\"]/a[@class=\"g-btn-green\"]").click()
            flag = True
        except:
            flag = False
        if flag:

            print("报名成功")
        else:
            print("该课程已报名")
        driver.close()
        # new_window = "window.open()"
        # driver.execute_script(new_window)

    #driver.close()
    #driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]").click()

    # time.sleep(2)
    # xpath_button_add_condition = '//tr[@data-row-key=\"587\"]/td/a'
    # move_on_to_add_condition = driver.find_element_by_xpath(xpath_button_add_condition)
    # ActionChains(driver).move_to_element(move_on_to_add_condition).perform()
    # time.sleep(2)
    # driver.find_element_by_xpath("//ul[@class=\"ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical\"]/li[2]").click()
    # driver.find_element_by_xpath("//div[@class=\"ant-modal-confirm-btns\"]/button[2]").click()
if __name__ == '__main__':
    # create_Xbk("wujiaxing","1314Woaini!","https://keosms.youdao.com/modeselect?domain=&returnurl=http://f2estatic.youdao.com/zzq/xbk4/#/403")
    #create_Dbk("wujiaxing","1314Woaini!","https://keosms.youdao.com/modeselect?returnurl=http%3A%2F%2Fcourseop1.inner.youdao.com%2F")
    # yue_Ke("wujiaxing","1314Woaini!","https://keosms.youdao.com/modeselect?domain=&returnurl=https://xiaobanke-admin.youdao.com/#/403")
    list=[[18835394235,"Wangtuo0109"],[18811791253,"Gyh802397"],[15524206427,"qwer1234"],[13546196209,"Wangtuo0109"],[18835394235,"Wangtuo0109"],
          [18811791253,"Gyh802397"],[15524206427,"qwer1234"],[18031712521,"jpkchen123@"],[15729399861,"aa123456"],[13920352077,"aa123456"],[18321717920,"aa123456"],
          [13048016364,"aa123456"],[18511400389,"wangqq318Q"],[17750961257,"cc960801"]]
    url="https://ke.youdao.com/course/detail/103030"
    buy_Class(list,url)
#driver.find_element_by_xpath("//tr[@data-row-key=\"587\"]/td/button").click()
#time.sleep(2)
#driver.find_element_by_xpath("//button[@class=\"ant-btn ant-btn-primary\"]").click()
#time.sleep(2)
#driver.find_element_by_xpath("//button[@class=\"ant-btn ant-btn-dashed ant-btn-block\"]").click()
# driver.find_element_by_id("lessonList_0_name").send_keys("第一节课")
# driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]").click()

# time.sleep(2)
# xpath_button_add_condition = '//tr[@data-row-key=\"587\"]/td/a'
# move_on_to_add_condition = driver.find_element_by_xpath(xpath_button_add_condition)
# ActionChains(driver).move_to_element(move_on_to_add_condition).perform()
# time.sleep(2)
# # driver.find_element_by_xpath("//ul[@class=\"ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical\"]/li[2]").click()
# # driver.find_element_by_xpath("//div[@class=\"ant-modal-confirm-btns\"]/button[2]").click()
# #
# driver.find_element_by_xpath("//a[@href=\"#/manageTeach/scheduleApplication\"]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//tr[@class=\"ant-table-row ant-table-row-level-0\"][1]/td/button").click()
# time.sleep(2)
# driver.find_element_by_xpath("//input[@id=\"age\"]").click()
# driver.find_element_by_xpath("//div[@class=\"rc-virtual-list-holder\"]//div[text()=\"1\"]").click()
# driver.find_element_by_xpath("//input[@id=\"foundation\"]").click()
# driver.find_element_by_xpath("//div[@class=\"ant-select-item ant-select-item-option ant-select-item-option-active\"]").click()
# # driver.find_element_by_id("wantedDay").click()
# # time.sleep(1)
# # driver.find_element_by_xpath("//div[@class=\"ant-picker-footer\"]").click()
# # driver.find_element_by_xpath("//input[@value=\"2\"]").click()
# # time.sleep(2)
# # driver.execute_script('window.scrollBy(0,5000)')
# # target = driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]")
# # driver.execute_script("arguments[0].scrollIntoView();", target)
# # time.sleep(5)
# # driver.find_element_by_xpath("//input[@placeholder=\"开始时间\"]").click()
# # driver.find_element_by_xpath("//ul[@class=\"ant-picker-time-panel-column\"][1]//div[text()=\"00\"]").click()
# # driver.find_element_by_xpath("//li[@class=\"ant-picker-ok\"]").click()
# # driver.find_element_by_xpath("//ul[@class=\"ant-picker-time-panel-column\"][1]//div[text()=\"00\"]").click()
# # driver.find_element_by_xpath("//li[@class=\"ant-picker-ok\"]").click()
# driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]").click()
# driver.get("http://f2estatic.youdao.com/zzq/xbk4/#/manageTeach/formalCourse/setCourse/arrange?courseId=582")
# time.sleep(2)
# driver.find_element_by_xpath("//tr[@class=\"ant-table-row ant-table-row-level-0\"]//input").click()
# driver.find_element_by_xpath("//div[@class=\"ant-pro-table-list-toolbar\"]//button").click()
# time.sleep(2)
# driver.find_element_by_id("name").send_keys("第一节课")
# driver.find_element_by_id("maxStudent").send_keys("3")
# driver.find_element_by_xpath("//span[@class=\"ant-radio\"]//input[@value=\"1\"]").click()
# driver.find_element_by_id("date").click()
# time.sleep(1)
# driver.find_element_by_xpath("//td[@class=\"ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today\"]").click()
# d=datetime.datetime.now()
# num = d.weekday()
# driver.find_element_by_xpath("//div[@id=\"weekday\"]//input[@value=1]").click()
#
#
# target = driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]")
# driver.execute_script("arguments[0].scrollIntoView();", target)
# time.sleep(5)
# startTime = (datetime.datetime.now()+datetime.timedelta(minutes=31)).strftime("%H:%M:%S")
# driver.find_element_by_id("timeRange").send_keys(startTime)
# time.sleep(2)
# driver.find_element_by_xpath("//ul[@class=\"ant-picker-ranges\"]//button/span").click()
# endTime = (datetime.datetime.now()+datetime.timedelta(minutes=46)).strftime("%H:%M:%S")
#
# time.sleep(3)
# driver.find_element_by_xpath("//div[@class=\"ant-col ant-col-17 ant-form-item-control\"]//input[@placeholder=\"结束时间\"]").send_keys(endTime)
# driver.find_element_by_xpath("//ul[@class=\"ant-picker-ranges\"]//button/span").click()
# driver.find_element_by_xpath("//div[@class=\"ant-modal-footer\"]/button[2]").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[@class=\"ant-modal-confirm-btns\"]/button[2]").click()

# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import ddddocr
import datetime
#定時開始搶票
startTime = datetime.datetime(2022, 6, 1, 16, 48, 0)
print('Program not starting yet...')
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('Program now starts on %s' % startTime)

class WebDriverEdge(object):

    def __init__(self):
        self.driver = self.StartWebdriver()

    def StartWebdriver(self):
        options = webdriver.EdgeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Edge(options=options)
        with open('./stealth.min.js') as f:
            js = f.read()
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })
        return driver

    def RunStart(self):
        self.driver.get("https://irs.thsrc.com.tw/IMINT/?locale=tw&info=U1cwMTEyMDgyNTIwMjIwNjAxMjAyMjA1MzAxNTUzNDYyNzI0")
        #添加cookie
        self.driver.add_cookie({
            "domain": "irs.thsrc.com.tw",
            "expirationDate": 1685580077,
            "hostOnly": "true",
            "name": "AcceptIRSCookiePolicyTime",
            "path": "/",
            "session": "false",
            "storeId": "0",
            "value": "Wed%20Jun%2001%202022%2008:41:11%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)",
            "id": "14"
        })
        self.driver.add_cookie({
            "domain": "irs.thsrc.com.tw",
            "hostOnly": "true",
            "name": "IRS-SESSION",
            "path": "/",
            "session": "true",
            "storeId": "0",
            "value": "!C+ARRZv5q+min674aBYvdQoj4grHbKqWrfJBYeaXei57uHgER7iG3l0wSrCp50ox",
            "id": "15"
        })
        self.driver.add_cookie({
            "domain": "irs.thsrc.com.tw",
            "hostOnly": "true",
            "name": "JSESSIONID",
            "path": "/IMINT",
            "session": "true",
            "storeId": "0",
            "value": "B68B5EE77DEFD8A46C46155B0091A340",
            "id": "16"
        })
        self.driver.add_cookie({
            "domain": "irs.thsrc.com.tw",
            "hostOnly": "true",
            "name": "name",
            "path": "/IMINT",
            "session": "true",
            "storeId": "0",
            "value": "value",
            "id": "17"
        })
        self.driver.add_cookie({
            "domain": "irs.thsrc.com.tw",
            "hostOnly": "true",
            "name": "THSRC-IRS",
            "path": "/",
            "session": "true",
            "storeId": "0",
            "value": "!VSAveF+NzSPA+1o8QL2Oxz3YfDiXncCpIrVblfgoopJ46V3kf2p23iO2HQwjiVzxQJb2kHHkFZmm3g==",
            "id": "18"
        })
        self.driver.get("https://irs.thsrc.com.tw/IMINT/?locale=tw&info=U1cwMTEyMDgyNTIwMjIwNjAxMjAyMjA1MzAxNTUzNDYyNzI0")
        #起點([2]南港[3]台北[4]板橋[5]桃園[6]新竹[7]苗栗[8]台中[9]彰化[10]雲林[11]嘉義[12]台南[13]左營)
        self.driver.find_element_by_xpath('//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[1]/div/select/option[2]').click()
        #終點([2]南港[3]台北[4]板橋[5]桃園[6]新竹[7]苗栗[8]台中[9]彰化[10]雲林[11]嘉義[12]台南[13]左營)
        self.driver.find_element_by_xpath('//*[@id="BookingS1Form"]/div[3]/div[1]/div/div[2]/div/select/option[13]').click()
        #日期(value_change)
        train_date_js = f'''
                var data = document.getElementsByClassName('uk-input out-date flatpickr-input')[0]
                data.value = '2022/06/05';
                '''
        self.driver.execute_script(train_date_js)
        #日期(value_change)
        train_date2_js = f'''
                var data2 = document.getElementsByClassName('uk-input')[1]
                data2.value = '6月5日 (日)';
                '''
        self.driver.execute_script(train_date2_js)
        #時間([1]00:00[2]00:30[3]05:00[5]06:00[7]07:00[9]08:00[11]09:00[13]10:00[15]11:00[17]12:00[19]13:00[21]14:00[23]15:00[25]16:00[27]17:00[29]18:00[31]19:00[33]20:00[35]21:00[37]22:00[39]23:00)
        train_time_js = f'''
                var time = document.getElementsByClassName('uk-select out-time')[0].options[11]
                time.selected = true;
                '''
        self.driver.execute_script(train_time_js)
        #取得驗證碼
        with open('b.png', 'wb') as file:
            file.write(self.driver.find_elements_by_class_name('captcha-img')[0].screenshot_as_png)

        ocr = ddddocr.DdddOcr()
        with open('b.png', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        #輸入驗證碼
        self.driver.find_element_by_xpath('//*[@id="BookingS1Form"]/div[4]/div[2]/div/input').send_keys(res.upper())
        #全票數量([1]為一張票)
        train_Adult_js = f'''
                var Adult = document.getElementsByName('ticketPanel:rows:0:ticketAmount')[0].options[2]
                Adult.selected = true;
                '''
        self.driver.execute_script(train_Adult_js)
        #大學生票數量([1]為一張票)
        train_college_js = f'''
                var college = document.getElementsByName('ticketPanel:rows:4:ticketAmount')[0].options[2]
                college.selected = true;
                '''
        self.driver.execute_script(train_college_js)
        #兒童(6-11)票數量([1]為一張票)
        train_child_js = f'''
                var child = document.getElementsByName('ticketPanel:rows:1:ticketAmount')[0].options[2]
                child.selected = true;
                '''
        self.driver.execute_script(train_child_js)
        #開始查詢
        self.driver.find_elements_by_name('SubmitButton')[0].click()
        #確認車次
        self.driver.find_elements_by_name('SubmitButton')[0].click()
        #身分證號
        self.driver.find_elements_by_name('dummyId')[0].send_keys("A131137373")
        #電話
        self.driver.find_elements_by_name('dummyPhone')[0].send_keys("0965438367")
        #電子郵件
        self.driver.find_elements_by_name('email')[0].send_keys("s95051414@gmail.com")
        #我已確認
        self.driver.find_element_by_xpath('//*[@id="BookingS3FormSP"]/section[2]/div[3]/div[1]/label/input').click()
        #確認
        #self.driver.find_elements_by_class_name('uk-button uk-button-primary uk-button-large btn-next')[0].click()


if __name__ == '__main__':
    Crawl = WebDriverEdge()
    Crawl.RunStart()
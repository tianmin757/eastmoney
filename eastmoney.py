# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:20:04 2017

@author: Administrator
"""

from selenium import webdriver
import time
import pymysql
import traceback
import random

#获取20到30的随机浮点数
randnum=random.uniform(20,30)
url="http://quote.eastmoney.com/center/list.html#20"
#url="http://quote.eastmoney.com/center/list.html#10"
#url="http://quote.eastmoney.com/center/list.html#33"

#使用firefox驱动打开网页
driver=webdriver.Firefox()
driver.get(url)

time.sleep(randnum)
driver.maximize_window()

#按随机时间进行休眠，让网页加载完全，同时防止给服务器造成过大负担
time.sleep(randnum)

#点击列表的代码链接对股票代码进行排序
driver.find_element_by_css_selector("#fixed > tbody:nth-child(1) > tr:nth-child(1) > th:nth-child(2) > a:nth-child(1)").click()
time.sleep(randnum)


#爬取所需数据   
def get_data():
    #初始化三个list，用于存放股票代码，股票名称，股票链接
    stock_id=[]
    name_list=[]
    url_list=[]
    for i in range(1,100):
        #当翻页的时候页面布局会发生变化，导致CSS无法定位，使用if语句进行判断
        if int(driver.find_element_by_css_selector(".current").text)<4 or int(driver.find_element_by_css_selector(".current").text)==97:
           #int(driver.find_element_by_css_selector(".current").text)<4 or int(driver.find_element_by_css_selector(".current").text)==63:
           #int(driver.find_element_by_css_selector(".current").text)==161:
            for j in range(1,11):
                stock_css1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(2) > a:nth-child(1)"
                stock_css2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(2) > a:nth-child(1)"
                stock_name1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(3) > a:nth-child(1)"
                stock_name2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(3) > a:nth-child(1)"
                stock1=driver.find_element_by_css_selector(stock_css1).text
                stock2=driver.find_element_by_css_selector(stock_css2).text
                url1=driver.find_element_by_css_selector(stock_css1).get_attribute("href")
                url2=driver.find_element_by_css_selector(stock_css2).get_attribute("href")
                name1=driver.find_element_by_css_selector(stock_name1).text
                name2=driver.find_element_by_css_selector(stock_name2).text
                stock_id.append(stock1)
                stock_id.append(stock2)
                url_list.append(url1)
                url_list.append(url2)
                name_list.append(name1)
                name_list.append(name2)
                print(stock_id) 
                print(url_list) 
                print(name_list) 
            #爬完一页点击下一页继续    
            driver.find_element_by_css_selector("#pagenav > a:nth-child(8)").click()
            time.sleep(randnum)
        elif int(driver.find_element_by_css_selector(".current").text)>3 and int(driver.find_element_by_css_selector(".current").text)<97:
             #int(driver.find_element_by_css_selector(".current").text)>3 and int(driver.find_element_by_css_selector(".current").text)<63:
             #int(driver.find_element_by_css_selector(".current").text)>3 and int(driver.find_element_by_css_selector(".current").text)<161:
            for j in range(1,11):
                stock_css1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(2) > a:nth-child(1)"
                stock_css2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(2) > a:nth-child(1)"
                stock_name1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(3) > a:nth-child(1)"
                stock_name2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(3) > a:nth-child(1)"
                stock1=driver.find_element_by_css_selector(stock_css1).text
                stock2=driver.find_element_by_css_selector(stock_css2).text
                url1=driver.find_element_by_css_selector(stock_css1).get_attribute("href")
                url2=driver.find_element_by_css_selector(stock_css2).get_attribute("href")
                name1=driver.find_element_by_css_selector(stock_name1).text
                name2=driver.find_element_by_css_selector(stock_name2).text
                stock_id.append(stock1)
                stock_id.append(stock2)
                url_list.append(url1)
                url_list.append(url2)
                name_list.append(name1)
                name_list.append(name2)
                print(stock_id) 
                print(url_list) 
                print(name_list) 
            driver.find_element_by_css_selector("#pagenav > a:nth-child(9)").click()
            time.sleep(randnum)    
        elif int(driver.find_element_by_css_selector(".current").text)==98:
             #int(driver.find_element_by_css_selector(".current").text)==64:
             #int(driver.find_element_by_css_selector(".current").text)==162:
            for j in range(1,11):
                stock_css1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(2) > a:nth-child(1)"
                stock_css2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(2) > a:nth-child(1)"
                stock_name1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(3) > a:nth-child(1)"
                stock_name2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(3) > a:nth-child(1)"
                stock1=driver.find_element_by_css_selector(stock_css1).text
                stock2=driver.find_element_by_css_selector(stock_css2).text
                url1=driver.find_element_by_css_selector(stock_css1).get_attribute("href")
                url2=driver.find_element_by_css_selector(stock_css2).get_attribute("href")
                name1=driver.find_element_by_css_selector(stock_name1).text
                name2=driver.find_element_by_css_selector(stock_name2).text
                stock_id.append(stock1)
                stock_id.append(stock2)
                url_list.append(url1)
                url_list.append(url2)
                name_list.append(name1)
                name_list.append(name2)
                print(stock_id) 
                print(url_list) 
                print(name_list) 
            driver.find_element_by_css_selector("#pagenav > a:nth-child(7)").click()
            time.sleep(randnum)
        else:  
            for j in range(1,11):
                try:
                    stock_css1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(2) > a:nth-child(1)"
                    stock_css2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(2) > a:nth-child(1)"
                    stock_name1="#fixed > tbody:nth-child(1) > tr:nth-child("+str(j*2)+")> td:nth-child(3) > a:nth-child(1)"
                    stock_name2="tr.bg:nth-child("+str(j*2+1)+") > td:nth-child(3) > a:nth-child(1)"
                    stock1=driver.find_element_by_css_selector(stock_css1).text
                    stock2=driver.find_element_by_css_selector(stock_css2).text
                    url1=driver.find_element_by_css_selector(stock_css1).get_attribute("href")
                    url2=driver.find_element_by_css_selector(stock_css2).get_attribute("href")
                    name1=driver.find_element_by_css_selector(stock_name1).text
                    name2=driver.find_element_by_css_selector(stock_name2).text
                    stock_id.append(stock1)
                    stock_id.append(stock2)
                    url_list.append(url1)
                    url_list.append(url2)
                    name_list.append(name1)
                    name_list.append(name2)
                    print(stock_id) 
                    print(url_list) 
                    print(name_list)
                except Exception as e:
                    print("爬完了")
            driver.find_element_by_css_selector(".disable").click()
            time.sleep(randnum)
    return stock_id,name_list,url_list

#把数据输入数据库
def chaxun():
    conn=pymysql.connect(host='localhost',
                     user='root',
                     passwd='root',
                     db='test',
                     charset='utf8')
    new_url=get_data()
    sql="insert into test.eastmoney_basic_info  values (%s,%s,%s)"
    cursor=conn.cursor()
    try:
        for i in range(0,1967):    
            cursor.execute(sql,(new_url[0][i],new_url[1][i],new_url[2][i]))
    except Exception as e:
        print("循环太多次了")
if __name__=="__main__":
    try:
        chaxun()
    except:
        traceback.print_exc()

# coding:utf-8
import re
from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
import itertools
import lxml
import numpy
import pandas
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')


#Some User Agents
hds={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


#with open("demo1.csv","w") as v:
    #writer=csv.writer(v)
    #writer.writerow(["数目","编号","标题","链接"])
    #print('生成第一行')

df=pandas.DataFrame(columns=('id','title'))

def download(url): #下载数据，传入代理数据
    try:
        req = urllib2.Request(url)
        global s
        s = urllib2.urlopen(req).read()
        soup = BeautifulSoup(s, 'lxml')

        global page_title
        page_title = soup.title
    except (urllib2.HTTPError, urllib2.URLError), e:
        print e


    print page_title.string
    return page_title.string



def save_csv():  # 将抓取到的信息存储到csv当中


        df.loc[i,['title']]=str(page_title.string)
        df.loc[i,['id']]=str(i)
        df.to_csv('demo1.csv',index=False)

        print('生成列表')




if __name__ == '__main__':
    print('***即将开始抓取***')
    num1=input('开始编号')
    num2=input('结束编号')
    for i in range(0, num2 - num1):
        page_num = i + num1
        url = 'http://www.qdaily.com/articles/' + str(page_num) + '.html'
        download(url)
        save_csv()
        print("*******************************")
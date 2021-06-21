# -*- coding: utf-8 -*-

from datetime import *
import tweepy
from selenium import webdriver
import urllib.request
from requests_oauthlib import OAuth1Session 
import requests
import tweepy
import os

#情報を取りたいジャーナルのサイトのURLを指定
url = "https://www.cell.com/cell/newarticles"
#url = "https://www.cell.com/cell-stem-cell/current"
#url = "https://www.cell.com/cancer-cell/current"
#url=  "https://www.cell.com/immunity/current"

#Seleniumパッケージ(http://www.automationtestinghub.com/download-chrome-driver/)により上記ジャーナルサイトを開く。前もってchromedriver(https://sites.google.com/chromium.org/driver/)をダウンロードして置いてください。
browser = webdriver.Chrome(executable_path ="/Users/toshihikooki/Downloads/chromedriver") #ご自身のPC上のフォルダーをchromdriverを指定
browser.get(url)
browser.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

#日付時間情報を入手
now = datetime.today() - timedelta(0,60)
ti =  str(now.year) + u"年" + str(now.month) + u"月" + str(now.day) + u"日: "

#twitter APIへのアクセス
CONSUMER_KEY = "XXXXX"# ご自身で取得してください
CONSUMER_SECRET="YYYYY"# ご自身で取得してください
ACCESS_TOKEN = "ZZZZZ" # ご自身で取得してください
ACCESS_TOKEN_SECRET = "AAAAAA" # ご自身で取得してください

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#上記ジャーナルサイトより論文のタイトルとそのURLを入手、サムネール画像も入手できるが結局解像度が悪いためコメントアウト。CSSセレクタによって論文のタイトルとURLを指定しています。
# CSSセレクタは

title = browser.find_elements_by_class_name("toc__item__title")
url =  browser.find_elements_by_css_selector("h3.toc__item__title > a ")
#vs =  browser.find_elements_by_css_selector("div.toc__item__cover.col-md-3.col-lg-2.hidden-xs.hidden-sm.hidden-md > a > img")

#各論文とそのURLをtwitterに投稿、サムネール画像も投稿できるが結局解像度が悪いためコメントアウト
i=0

for a in title:
    try :
        tit = a.text
        href=url[i].get_attribute("href")
        #img=vs[i].get_attribute("src")
        content = ti+"Pythonで送る最新のCell Press \n"+tit + "\n" + href
        #print("_", tit,">", href, ">", img)
        print("ツイート内容：{}".format(content))
        # URLと保存パスを指定
        #filename = "./test.jpg"
        # ダウンロード
        #r = requests.get(img)
        #with open(filename, 'wb') as outfile:
            #outfile.write(r.content)
        #api.update_with_media(filename, status = content)
        api.update_status(status = content)
        print("ツイートに成功しました")
        i +=1
        #os.remove(filename)
    except:
        print("error")
        i +=1
        
    
print("プログラムを終了しました") 
browser.close()

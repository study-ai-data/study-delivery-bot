from urllib.request import urlopen
from bs4 import BeautifulSoup
#from github import Github, Issue
from dateutil.parser import parse
from pytz import timezone

import datetime
import os


KST = timezone('Asia/Seoul')
today = datetime.datetime.now(KST)


def isDateInRange(created_at):
    suffix_KST = '.000001+09:00'
    created_at = parse(created_at + suffix_KST)
    yesterday = today - datetime.timedelta(1)
    return today > created_at > yesterday


class Okky:
    def __init__(self):
        self.name = "okky"
        self.site = "https://okky.kr"
        self.res = urlopen(self.site + "/articles/gathering?offset=0&max=20&sort=id&order=desc")
        self.soup = BeautifulSoup(self.res, 'html.parser')

    def get_content(self):
        issue_content = ""
        if self.name == "okky":
            article_list = self.soup.select('#list-article ul > li.list-group-item')
            for content in article_list:
                title = content.select('h5 > a')[0]
                published_at = content.select('div.date-created span.timeago')[0].get_text()
                item = published_at + " " + str(title).replace('href="', 'href="' + self.site).replace("\n", "").replace('  ', '').strip() + '<br>\n'
                if '마감' not in str(title) and isDateInRange(published_at):
                    issue_content += item
                else:
                    print('[filtered] ', item)
        else:
            print("준비중!")
        return issue_content

    def get_title(self):
        issue_title = ""
        if self.name == "okky":
            issue_title = "[OKKY] 스터디 모집 %s" % (today.strftime("%Y년 %m월 %d일 %H시".encode('unicode-escape').decode()).encode().decode('unicode-escape'))
        else:
            print("준비중!")
        return issue_title

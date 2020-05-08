from urllib.request import urlopen
from bs4 import BeautifulSoup
#from github import Github, Issue
from dateutil.parser import parse
from pytz import timezone

import datetime
import os
import requests


KST = timezone('Asia/Seoul')
today = datetime.datetime.now(KST)


def isDateInRange(created_at):
    suffix_KST = '.000001+09:00'
    created_at = parse(created_at + suffix_KST)
    yesterday = today - datetime.timedelta(1)
    return today > created_at > yesterday


class CampusPick:
    def __init__(self):
        self.name = "[CampusPick]"
        self.login = "https://www.campuspick.com/login"
        self.site = "https://www.campuspick.com/study/list?category1="

        # self.lang = urlopen(self.site + "1&category2=0")
        self.lang = urlopen("https://www.campuspick.com/study/list?category1=1&category2=0")
        self.soup1 = BeautifulSoup(self.lang, 'html.parser')

        self.job = urlopen(self.site + "2&category2=0")
        self.soup2 = BeautifulSoup(self.job, 'html.parser')

        self.certificate = urlopen(self.site + "3&category2=0")
        self.soup3 = BeautifulSoup(self.certificate, 'html.parser')

        self.etc = urlopen(self.site + "4&category2=0")
        self.soup4 = BeautifulSoup(self.etc, 'html.parser')

    def get_content(self):
        issue_content = ""
        return issue_content

    def get_title(self):
        issue_title = self.name + " 스터디 모집 %s" % (today.strftime("%Y년 %m월 %d일 %H시".encode('unicode-escape').decode()).encode().decode('unicode-escape'))
        return issue_title


if __name__ == "__main__":
    campusPick = CampusPick()

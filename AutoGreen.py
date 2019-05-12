# coding=utf-8

import os
import codecs
import time
import re
from git import Repo
from selenium import webdriver


def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;


class AutoGreen:
    def __init__(self):
        self.directory = os.path.dirname(os.path.abspath(__file__))
        self.repo = Repo(self.directory)
        print("dir：" + self.directory)

    def _commit(self, message):
        git = self.repo.git
        git.add(".")
        git.commit("-m", "\""+message+"\"")
        remote = self.repo.remote()
        remote.push()

    def green(self):
        if ~self.repo.bare:
            # 获取网页数据
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = True
            driver = webdriver.Firefox(options=firefox_options)
            driver.get("https://www.zhihu.com/billboard")
            titles = driver.find_elements_by_class_name("HotList-itemTitle")
            contents = driver.find_elements_by_class_name("HotList-itemExcerpt")

            text = driver.page_source

            # 写入README
            fp = codecs.open("README.md", 'a+','utf-8')
            date = time.strftime('%Y.%m.%d', time.localtime(time.time()))
            fp.write("# " + date + "\n")
            for i, title in enumerate(titles):
                pattern = re.compile(title.text + '.{,500}?"cardId":"Q_(.*?)"', re.S)
                numbers = re.findall(pattern, text)
                if len(numbers) > 0:
                    url = "https://www.zhihu.com/question/" + numbers[0]
                    fp.write("## [" + title.text + "](" + url + ")\n")
                    fp.write(contents[i].text + "\n")
                if i >= 2:
                    break
            fp.close()
            driver.close()
        self._commit(date)
        return date


autoGreen = AutoGreen()
while True:
    print(autoGreen.green()+": success")
    seconds = sleeptime(24,0,0)
    time.sleep(seconds)
import os
import time
import re
from pyvirtualdisplay import Display
from git import Repo
from selenium import webdriver


def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;


class AutoGreen:
    def __init__(self):
        self.directory = os.path.dirname(os.path.abspath(__file__))
        print("dir："+self.directory)
        self.repo = Repo(self.directory)

    def _commit(self, message):
        git = self.repo.git
        git.add(".")
        git.commit("-m", message)

    def green(self):
        if ~self.repo.bare:
            # 获取网页数据
            display = Display(visible=0, size=(900, 800))
            display.start()
            driver = webdriver.Firefox()
            driver.get("https://www.zhihu.com/billboard")
            titles = driver.find_elements_by_class_name("HotList-itemTitle")
            contents = driver.find_elements_by_class_name("HotList-itemExcerpt")

            text = driver.page_source

            # 写入README
            fp = open("README.md", 'a+')
            date = time.strftime('%Y.%m.%d', time.localtime(time.time()))
            fp.write("# " + date + "\n")
            for i, title in enumerate(titles):
                pattern = re.compile(title.text + '.{,400}?"cardId":"Q_(.*?)"', re.S)
                numbers = re.findall(pattern, text)
                if len(numbers) > 0:
                    url = "https://www.zhihu.com/question/" + numbers[0]
                    fp.write("## [" + title.text + "](" + url + ")\n")
                    fp.write(contents[i].text + "\n")
                if i >= 2:
                    break
            fp.close()

            driver.close()
            display.stop()
            # self.commit("crawl top3 topic from zhihu to add to README.md " + date)
            # self._commit("auto")


autoGreen = AutoGreen()
while True:
    autoGreen.green()
    print("2")
    seconds = sleeptime(0,0,30)
    time.sleep(seconds)
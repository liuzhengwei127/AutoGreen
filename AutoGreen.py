import os
import time
import re
from git import Repo
from selenium import webdriver


class AutoGreen:
    def __init__(self):
        self.directory = os.path.dirname(os.path.abspath(__file__))
        print("目录："+self.directory)
        self.repo = Repo(self.directory)

    def _commit(self, message):
        git = self.repo.git
        git.add(".")
        git.commit("-m", message)

    def green(self):
        if ~self.repo.bare:
            # 获取网页数据
            driver = webdriver.Chrome()
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
                print(numbers)
                if len(numbers) > 0:
                    url = "https://www.zhihu.com/question/" + numbers[0]
                    fp.write("## [" + title.text + "](" + url + ")\n")
                    fp.write(contents[i].text + "\n")
                if i >= 2:
                    break
            fp.close()

            driver.close()
            # self.commit("crawl top3 topic from zhihu to add to README.md " + date)
            self._commit("oop")


autoGreen = AutoGreen()
autoGreen.green()
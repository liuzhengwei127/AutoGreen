import os
import time
import re
from git import Repo
from selenium import webdriver


def commit(date):
    git = repo.git
    git.add(".")
    git.commit("-m", "crawl top3 topic from zhihu to add to README.md "+ date)


directory = os.path.dirname(os.path.abspath(__file__))
print("目录："+directory)
repo = Repo(directory)

if ~repo.bare:
    # 获取网页数据
    driver = webdriver.Chrome()
    driver.get("https://www.zhihu.com/billboard")
    titles = driver.find_elements_by_class_name("HotList-itemTitle")
    contents = driver.find_elements_by_class_name("HotList-itemExcerpt")

    text = driver.page_source

    # 写入README
    fp = open("README.md", 'a+')
    date = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    fp.write("# "+date + "\n")
    for i, title in enumerate(titles):
        pattern = re.compile(title.text+'.{,400}?"cardId":"Q_(.*?)"', re.S)
        numbers = re.findall(pattern, text)
        print(numbers)
        if len(numbers) > 0:
            url = "https://www.zhihu.com/question/"+numbers[0]
            fp.write("## [" + title.text + "]("+url+")\n")
            fp.write(contents[i].text + "\n")
        if i >= 2:
            break
    fp.close()

    driver.close()
    commit(date)

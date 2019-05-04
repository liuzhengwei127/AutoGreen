import os
import time
from git import Repo
from selenium import webdriver


def commit():
    git = repo.git
    git.add(".")
    git.commit("-m", "have second try to write README.md with localtime and commit it")


directory = os.path.dirname(os.path.abspath(__file__))
print("目录："+directory)
repo = Repo(directory)

if ~repo.bare:
    fp = open("README.md",'a+')
    date = time.strftime('%Y.%m.%d',time.localtime(time.time()))

    driver = webdriver.Chrome()
    driver.get("https://www.zhihu.com/billboard")
    titles = driver.find_elements_by_class_name("HotList-itemTitle")
    # urls = driver.find_element_by_class_name()
    contents = driver.find_elements_by_class_name("HotList-itemExcerpt")

    fp.write("# "+date + "\n")
    for i, title in enumerate(titles):
        fp.write("## "+title.text+"\n")
        fp.write(contents[i].text+"\n")
        if i >= 2:
            break

    driver.close()
    commit()

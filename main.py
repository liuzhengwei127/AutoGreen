from git import Repo
import os
import time

dir = os.path.dirname(os.path.abspath(__file__))
print("目录："+dir)
repo = Repo(dir)
if ~repo.bare:
    fp = open("README.md",'a+')
    date = time.strftime('%Y.%m.%d',time.localtime(time.time()))
    fp.write(date+"\n")
    git = repo.git
    git.add(".")
    git.commit("-m", "have second try to write README.md with localtime and commit it")
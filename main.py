from git import Repo
import os

dir = os.path.dirname(os.path.abspath(__file__))
print("目录："+dir)
repo = Repo(dir)
if ~repo.bare:
    fp = open("README.md",'a+')
    fp.write("have a try\n")
    git = repo.git
    git.add(".")
    git.commit("-m", "have a try to write README.md and commit it")
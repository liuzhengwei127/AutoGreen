from git import Repo
import os

dir = os.path.dirname(os.path.abspath(__file__))
print("目录："+dir)
repo = Repo(dir)
if ~repo.bare:
    fp = open("README.md",'w')
    git = repo.git
    git.add(".")
    git.commit("-m", "the first try to GitPython")
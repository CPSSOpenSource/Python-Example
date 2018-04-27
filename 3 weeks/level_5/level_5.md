# 문제
4단계 소스 코드를 동아리 github 홈페이지에 있는 python-example 레포토리에서 report 브렌치를 만들어 커밋한 후 master 브렌치와 병합하세요.

# 문제 의도
해당 문제는 git 명령어를 얼마나 활용할 수 있는가에 대해 묻고자 하는 의도가 있습니다.

# 핵심 명령어
```git config```<br />
```git merge```<br />
```git commit```<br />
```git add```<br />

# command
```
git init (if git storage is not initialize)
git clone https://https://github.com/CPSSOpenSource/Python-Example.git
cd Python-Example
git config --global user.name "cpssnetwork"
git config --global user.email "cpss.network@gmail.com"
git checkout -b report
git add "level_4.py"
git commit -m "level 4 source code updated"
git checkout master
git merge report
git push origin master
```
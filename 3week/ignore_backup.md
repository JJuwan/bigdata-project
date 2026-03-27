6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ pwd
/c/Users/6-112/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ ls
app.py  requirements.txt  venv/
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ ls
app.py  requirements.txt  venv/
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cd app.py
bash: cd: app.py: Not a directory
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ ls
app.py  requirements.txt  venv/
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cd venv/
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw/venv (main)
$ cd ..
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ mkdir 3week.md
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cat .gitignore
# 가상환경
venv/

# Python 캐시
__pycache__/
*.pyc

# 환경 변수
.env

# IDE 설정
.vscode/
.idea/

# OS 파일
.DS_Store
Thumbs.db


(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ mkdir 3week
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cat .gitignore
# 가상환경
venv/

# Python 캐시
__pycache__/
*.pyc

# 환경 변수
.env

# IDE 설정
.vscode/
.idea/

# OS 파일
.DS_Store
Thumbs.db


(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cp .gitignore
cp: missing destination file operand after '.gitignore'
Try 'cp --help' for more information.
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cp .gitignore .3week
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cp .gitignore .3week/
cp: cannot create regular file '.3week/': Not a directory
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ cp .gitignore 3week/
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ mv 3week/.gitignore ./ignore_backup.md
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ git add .
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ git commit -m "3주차 명령어 연습"
[main ab6941d] 3주차 명령어 연습
 1 file changed, 19 insertions(+)
 create mode 100644 ignore_backup.md
(venv) 
6-112@112-30 MINGW64 ~/Desktop/빅데이터분석프로그래밍/bigdata-project-b-jjw (main)
$ git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 275 bytes | 275.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/JJuwan/bigdata-project.git
   4c14e3e..ab6941d  main -> main
(venv)
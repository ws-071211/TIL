# GIT
## GIT의 명령어
#### 기본 GIT 명령어
저장소를 새로이 생성하는 <code>git init</code>

원격 저장소로부터 복제해오는 <code>git clone {url}</code>

코드에 변경사항을 체크하는 <code>git status </code>

특정한 파일을 스테이징하는 <code>git add {파일명}</code>
* 스테이징(staging):곧 커밋할 파일에 대한 정보를 저장하는 것
- 커밋(commit):변경한 작업들을 저장소에 기록하는 동작

변경된 모든 파일들을 스테이징하는 <code>git add .</code>

스테이징된 파일들을 커밋하는 <code>git commit</code>

커밋된 파일을 원격 저장소로 보내는 <code>git push</code>

원격 저장소를 추가하는 <code>git remote add origin {원격서버주소}</code>


---
#### 커밋 관련 GIT 명령어
최신 4개의 커밋을 하나로 합치는 <code>git rebase -i HEAD~4</code>

커밋 메세지를 수정하는 <code>git commit --amend </code>

커밋 이력
<pre>
* 모든 커밋했던 이력를 확인하는 <code>git log</code>
* 각 커밋을 한 줄로 표시하는 <code>git log --pretty=oneline</code>
* reset 혹은 rebase로 없어진 과거의 커밋 이력을 확인할 수 있는<code> git log</code>
</pre> 

커밋 취소

<pre>
* 마지막 커밋을 삭제하는 git reset HEAD^
* 마직막 커밋 상태로 되돌리는 git reset --hard HEAD
* 스테이징을 언스테이징으로 변경하는 git reset HEAD *
</pre>
---
#### 브랜치에 관련된 GIT 명령어
* 브랜치(branch):여러 개발자들이 동시에 다양한 작업을 할 수 있게 만들어 주는 기능
master브랜치를 특정 파일로 넘기기
<pre>
1. git checkout better_branch
2. git merge --strategy=ours master
3. git checkout master
4. git merge better_branch
</pre>
브랜치의 목록
<pre>
1. git branch//로컬
2. git branch-r// 리모트
3. git branch-a//로컬과 리모트가 포함된 모든 브랜치보기
</pre>
브랜치 생성
<pre>
1. git branch new master //master에서 new브랜치 생성
2. git push origin new//new브랜치를 리모트로 보내기
</pre>
브랜치 삭제
<pre>
1. git branch -D{삭제할 브랜치의 이름}//로컬
2. git push origin :{the_remote_branch}//리모트
</pre>
빈 브랜치 생성하기
<pre>
1. git checkout --orphan{새로운 브랜치의 이름}
2. git commit -a//커밋해야 새로운 브랜치가 생성됨
3. git checkout -b new-branch//브랜치 생성과 동시에 리모트 브랜치 가져오기
</pre>
리모트 브랜치 가져오기
<code>git checkout -t origin/{가져올 브랜치의 이름}//ref</code>
브랜치 이름 변경하기
<code>git branch -m{새로운 이름}//ref</code>

---
#### Tag관련 GIT명령어
태그 생성
<pre>
1. git tag -a {tag name}{commit hash}
2. git tag {tag name} {tag name}-f -m"{new message}"
</pre>
태그 삭제
<pre>
1. git tag -d {tag name}
2. git push origin : tags/{tag name}//리모트
</pre>
태그 푸쉬
<pre>
1. git push origin --tags
2. git push origin {tag name}
3. git push --tags
</pre>
#### 기타 GIT 명령어
파일 삭제
<code>git rm -- cached --ignore-unmatch[삭제할 파일명]</code>
히스토리 삭제   
* 목적:비밀번호, 아이디 등 비공개 정보가 담긴 파일을 실수로 오렸을 때 삭제하는 방법
<pre>
* git clone[url]//소스 다운로드
* cd [folder_name]//해당 폴더 이동
* git filter-branch --index-filter 'git rm --cached --ignore-unmatch[삭제할 파일명]' --prune-empty -- --all//모든 히스토리에서 해당 파일 삭제
* git push origin master --force //서버로 전송
</pre>
히스토리에서 폴더 삭제:
<code>
git filter-branch --tree-filter 'rm - rf vendor/gems'HEAD
</code>리모트 주소 추가하여 로컬에 싱크하기<pre>
git remote add upstream{리모트 주소}
git pull upstream{브랜
치명}
</pre>
최적화
<pre>
git gc
git gc --aggressive
</pre>

---
#### 서버 설정 GIT 명령어
강제 표시 설정
<code>git config receive.denynonfast forwards false</code>
Alias
~/.gitconfig 파일을 설정하여 Git 명령어 앨리어스를 지정할 수 있다.

~/.gitconfig > alias 부분:

[alias]
br = branch   
co = checkout    
rb = rebase   
st = status   
pl = pull   
ps = push   
lg = log --graph --abbrev-commit --decorate --format=format:'%C(cyan)%h%C(reset) - %C(green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)-%an%C(reset)%C(yellow)%d%C(reset);--all
ad = add
tg = tag
df = diff
### git config 정리
REM 사용자 이름 및 이메일
<pre>
git config --global user.name "Your name"
git config --global user.name "Your email address"
</pre>
REM 설정 조회
<pre>
git config --global --list
git config --list
</pre>
REM 출력 색상 활성화
<code>git config == global color.ul"auto"</code>   
REM 개행문자 변경 비활성화
<code>git config --global core.autocrlf false</code>   
REM SSL 사용 비활성화
<code>git config --global http.sslVerigy false</code>   
REM 인증서 설정하기
<code>git config --system http.sslcaino"C:\PortableApps\cmd_git\mingw32\ssl\certs\ca-bundle.crt"</code>   
REM 에디터 설정
<code>git config --global core.editor</code>



![Git](https://tecoble.techcourse.co.kr/static/d0f3454b578873dff73251477ca0e729/c4b07/dot-git.jpg)

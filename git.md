# GIT
## GIT의 명령어
#### 기본 GIT 명령어
저장소를 새로이 생성하는 <code>git init</code>

원격 저장소로부터 복제해오는 <code>git clone {url}</code>

코드에 변경사항을 체크하는 <code>git status </code>

특정한 파일을 스테이징하는 <code>git add {파일명}</code>
* 스테이징:곧 커밋할 파일에 대한 정보를 저장하는 것
- 커밋:변경한 작업들을 저장소에 기록하는 동작

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

test

import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        return f"이름: {self.name}, 사용자명: {self.username}, 암호:{self.password}"


class Post:
    def __init__(self, title, content, author_username):
        self.title = title
        self.content = content
        self.author_username = author_username

    def display_post(self):
        return (
            f"제목: {self.title}, 내용: {self.content}, 작성자: {self.author_username}"
        )


members = []
posts = []

member_data = [
    ["홍길동", "hong_gil_dong", "안전한_비밀번호"],
    ["이순신", "lee_sun_shin", "강한_비밀번호"],
    ["김철수", "kim_chul_soo", "비밀번호123"],
    ["박영희", "park_yeong_hee", "secure_password"],
    ["최승호", "choi_seung_ho", "12345678"],
]

for [a, b, c] in member_data:
    member = Member(a, b, c)
    members.append(member)

post_data = [
    ["1 번째 글", "내용 내용 내용 사과", members[0].username],
    ["2 번째 글", "내용 내용 내용 감", members[0].username],
    ["3 번째 글", "내용 내용 내용 배", members[0].username],
    ["4 번째 글", "더 많은 내용 딸기", members[1].username],
    ["5 번째 글", "더 많은 내용 수박", members[1].username],
    ["6 번째 글", "더 많은 내용 메론", members[1].username],
    ["7 번째 글", "더 많은 내용 바나나", members[2].username],
    ["8 번째 글", "더 많은 내용 파인애플", members[2].username],
    ["9 번째 글", "더 많은 내용 키위", members[2].username],
]


for [a, b, c] in post_data:
    post = Post(a, b, c)
    posts.append(post)


def inin():
    yorn = input("사용자 등록 y/n:")
    if yorn == "y":
        inputname = input("name:")
        inputusername = input("id:")
        inputpassword = input("pw:")
        member = Member(inputname, inputusername, inputpassword)
        members.append(member)


def ininpost():
    yorn = input("글쓰기 y/n:")
    if yorn == "y":
        inputtitle = input("title:")
        inputcontent = input("content:")
        inputusername = input("id:")
        post = Post(inputtitle, inputcontent, inputusername)
        posts.append(post)


def gogo():
    yorn = input("사용자 조회 y/n:")
    if yorn == "y":
        for member in members:
            print(member.display())


def gogocc():
    yorn = input("전체 글 조회 y/n:")
    if yorn == "y":
        for post in posts:
            print(post.display_post())


def gogoid():
    idgo = input("조회할 id:")
    found_posts = []

    for post in posts:
        if post.author_username == idgo:
            found_posts.append(post)

    if found_posts:
        for found_post in found_posts:
            print(found_post.display_post())
    else:
        print("일치하는 ID가 없습니다.")


def gogocon():
    congo = input("조회할 내용:")
    found_posts = []

    for post in posts:
        if congo in post.content:
            found_posts.append(post)

    if found_posts:
        for found_post in found_posts:
            print(found_post.display_post())
    else:
        print("일치하는 내용이 없습니다.")


while True:
    choose = input("1.사용자 등록, 2.글쓰기, 3.조회, 4.나가기 :")
    if choose == "1":
        inin()
    elif choose == "2":
        ininpost()
    elif choose == "3":
        choose1 = input("1.회원 조회, 2.포스팅 조회 :")
        if choose1 == "1":
            gogo()
        elif choose1 == "2":
            choose2 = input("1.전체 글 조회, 2.id 조회, 3.내용 조회 :")
            if choose2 == "1":
                gogocc()
            elif choose2 == "2":
                gogoid()
            elif choose2 == "3":
                gogocon()
    else:
        break

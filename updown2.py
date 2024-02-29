import random

# 시도 횟수 초기화 및 랜덤 숫자 설정
qqq = 0
random_number = random.randint(1, 100)


def updown():
    global qqq, random_number
    number = input("숫자를 입력하세요: ")
    number = int(number)
    print(random_number)

    # 입력값 검사
    if number > 100:
        print("다시 입력: 100보다 작은 숫자를 입력하세요.")
    elif number <= 0:
        print("다시 입력: 0보다 큰 숫자를 입력하세요.")
    else:
        # 정답 체크
        if number == random_number:
            print("정답입니다! ", qqq + 1, "번 걸렸습니다.")
            yn = input("다시 하시겠습니까? (y/n): ")
            if yn == "y":
                reset_game()
            elif yn == "n":
                print("안녕히 가세요.")
                return False  # 프로그램 종료

        elif number > random_number:
            print("다운")
        elif number < random_number:
            print("업")

        # 시도 횟수 증가 및 출력
        qqq += 1
        print(qqq, "번째 시도")


def reset_game():
    global random_number, qqq
    random_number = random.randint(1, 100)
    qqq = 0
    print("게임을 다시 시작합니다.")


# 무한 루프로 게임 진행
while True:
    updown()
    if not updown():
        break


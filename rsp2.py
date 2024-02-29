import random

w = 0
d = 0
b = 0

def rsp():
    global w, d, b
    while True:
        random_rsp = random.randint(1, 3)
        if random_rsp == 1:
            pc_rsp = "가위"
        elif random_rsp == 2:
            pc_rsp = "바위"
        else:
            pc_rsp = "보"

        def show_r():
            print(f"플레이어:{user_input}, 상대방:{pc_rsp}")

        def replay():
            yn_input1 = input("다시하시겠습니까? y/n: ")
            yn_input = yn_input1.lower()
            if yn_input == "n":
                print(f"승리:{w}, 패배:{d}, 무승부:{b}")
                return False
            elif yn_input == "y":
                return True
            else:
                print("y/n으로 입력해주세요")
                return replay()

        user_input = input("가위, 바위, 보 중 하나를 입력하세요: ")

        if user_input != "가위" and user_input != "바위" and user_input != "보":
            print("가위, 바위, 보 중에서만 입력하세요.")
        else:
            if user_input == pc_rsp:
                show_r()
                print("비겼습니다.")
                b += 1
            elif user_input == "가위":
                if pc_rsp == "바위":
                    show_r()
                    print("졌습니다")
                    d += 1
                if pc_rsp == "보":
                    show_r()
                    print("이겼습니다")
                    w += 1

            elif user_input == "바위":
                if pc_rsp == "보":
                    show_r()
                    print("졌습니다")
                    d += 1
                if pc_rsp == "가위":
                    show_r()
                    print("이겼습니다")
                    w += 1

            elif user_input == "보":
                if pc_rsp == "가위":
                    show_r()
                    print("졌습니다")
                    d += 1
                if pc_rsp == "바위":
                    show_r()
                    print("이겼습니다")
                    w += 1

            if not replay():
                break

rsp()

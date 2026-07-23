from Phone_Info import PhoneInfo

def show_menu():
    print("1. 메뉴")
    print("0. 종료")
    print("선택 ㄱ")

def read_date():
    name = input("이름: ")
    phone_number = input('전번: ')
    brith = input('생일: ')
    rejon = input('지역: ')

    person = PhoneInfo(name, phone_number, brith,rejon)
    person.show()
def main():
    while True:
   
        show_menu()
        menu_1 = int(input("메뉴 선택: "))
   
        if menu_1 == 1:
            print("이름,전번,생일,거주지를 입력")
            read_date()

        elif menu_1 == 0:
            print("프로그램 종료")
            break

        else:
            continue

if __name__ == "__main__":
    main()
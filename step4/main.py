from phone_service import Phon_Service
from Phon_repostory import Phone_reposetory


def show_menu():
    print("1. 메뉴")
    print("2. 데이터 조회")
    print("3.수정")
    print("5. 전체 출력")
    print("0. 종료")
    print("선택 ㄱ")


    
    
def main():
    reposetory = Phone_reposetory()
    reposetory.load()
    service = Phon_Service()
    while True:
        show_menu()
        try:
            menu_1 = int(input("메뉴 선택: "))
   
            if menu_1 == 1:
                print("이름,전번,생일,거주지를 입력")
                service.read_date()
            elif menu_1 == 2:
                print("조회")
                service.serch_deta()
            elif menu_1 ==3:
                print("수정")
                service.fix()
            elif menu_1 == 4:
                print("삭제")
                service.remv()
            elif menu_1 == 0:
                print("프로그램 종료")
                reposetory.load()
                break
            elif menu_1 ==5:
                service.show_all()

            else:
                print("잘못 입력 \n")    
        except ValueError:
            print("숫자문 입력 \n")
            continue
if __name__ == "__main__":
    main()
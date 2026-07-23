#from phonebook_service import PhoneBookService
from services.phonebook_service import instance as service
#from services.phonebook_service import instance as service2

def show_menu():
    print("선택하세요...")
    print("1. 데이터 입력")
    print("2. 데이터 검색")
    print("3. 데이터 수정")
    print("4. 데이터 삭제")
    print("5. 전체 출력")
    print("6. 데이터 저장")
    print("0. 프로그램 종료")

def main():
    
    #service = PhoneBookService()  # PhoneBookService 클래스의 인스턴스 생성

    while True:
        show_menu()
        try:
            choice = int(input("선택: "))       

            print() # 가독성을 위한 빈 줄
            
            if choice == 1:
                service.input_data()
            elif choice == 2:
                #service2.search_data()
                service.search_data()
            elif choice == 3:
                service.update_data()
            elif choice == 4:
                service.delete_data()
            elif choice == 5:
                service.show_all_data()
            elif choice == 6:
                service.backup_data()           
            elif choice == 0:
                print("프로그램을 종료합니다.")
                service.backup_data()  
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.\n")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.\n")
            continue

if __name__ == "__main__":   
    main()

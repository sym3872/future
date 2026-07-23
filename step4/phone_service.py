from Phone_Info import PhoneInfo, PhonecommpanyInfo,phoneunlvInfo


class Phon_Service:

    def __init__(self):
        self.info_sto = []

    def read_date(self): 
        print("1. 일반,  2. 대학,  3. 회사 ")
        ath = int(input(""))
        if ath == 1:
            name = input("이름: ")
            phone_number = input('전번: ')
            brith = input('생일: ')
            rejon = input('지역: ')

            info = PhoneInfo(name, phone_number, brith,rejon)
        elif ath == 2:
            name = input("이름: ")
            phone_number = input('전번: ')
            major = input("잔공: ")
            brith = input('생일: ')
            rejon = input('지역: ')

            info = phoneunlvInfo(name,phone_number,major,brith,rejon)

        elif ath == 3:
            name = input("이름: ")
            phone_number = input('전번: ')
            commpany = input("회사: ")
            brith = input('생일: ')
            rejon = input('지역: ')
        
            info = phoneunlvInfo(name,phone_number,commpany,brith,rejon)
        self.info_sto.append(info) # type: ignore

    def serch_deta(self):
        name = input("찾는 이름:")

        for i in self.info_sto:
            if name == i.name:
                print("있는 이름입니다.")
                i.show()
            else:
                print("ㄴㄴㄴ")
    def fix(self):
        name = input("수정할 이름:") # type: ignore

        for i in self.info_sto: # type: ignore
            if name == i.name: # type: ignore
                print("있는 이름입니다. 수정하시겠습니까?")
                an = input("") # type: ignore
                if an == 'Y' or 'y' or "예":
                    self.info_sto.remove() # type: ignore
                    print("수정할 내용 입력")
                    name = input("이름: ")
                    phone_number = input('전번: ') # type: ignore
                    brith = input('생일: ') # type: ignore
                    rejon = input('지역: ') # type: ignore

                    self.info_sto.append(PhoneInfo(name, phone_number, brith,rejon)) # type: ignore
                    print("추가 완료")
                else:
                    break
                
            else:
                continue

    def remv(self):
        name = input("삭제할 이름:") # type: ignore
        for i in self.info_sto: # type: ignore
            if name == i.name: # type: ignore
                print("있는 이름입니다.삭제 하시겠습니까?")
                an = input("") # type: ignore
                if an == 'Y' or 'y' or "예":
                    self.info_sto.remove() # type: ignore
                    print("삭제 완료")

                else:
                    break
            else:
                print("ㄴㄴㄴ")

    def show_all(self):
        print("==============================")
        for i in self.info_sto:  # type: ignore
            i.show() # type: ignore
        print("===============================")
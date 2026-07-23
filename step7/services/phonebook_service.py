from models.phone_info import PhoneInfo, PhoneUnivInfo, PhoneCompanyInfo
from storage.phone_repository import PhoneBookRepository

class PhoneBookService:
    def __init__(self):
        # 1. 파일 관리 전담 객체를 만들어서 장착합니다.
        self.repository = PhoneBookRepository()

        # 데이터 객체들을 담을 리스트 (개수 제한 없음)
        #self.info_storage = []
        self.info_storage = self.repository.load()

    # 🔹 [변경] 인덱스(idx) 대신 '객체 자체'를 바로 찾아오는 파이썬다운 검색 메서드
    # _find_info_by_name() 메서드는 내부적으로만 사용되므로 private 메서드로 정의 (강제X, 관례)
    def _find_info_by_name(self, name):    
        # 조건에 맞는 첫 번째 객체를 반환하고, 없으면 None을 리턴합니다.
        return next((info for info in self.info_storage if info.name == name), None)
    # next() 함수는 파이썬에서 "여러 개의 데이터 중에서 조건에 맞는 알맹이(첫 번째 데이터) 딱 하나만 즉시 꺼내줘!"라고 할 때 사용하는 파이썬 내장 함수. 
    # 조건에 맞는 데이터가 없으면 두 번째 인자로 지정한 None을 반환.
    # for문 보다 훨씬 간결하고, 파이썬다운 방식으로 데이터를 검색할 수 있습니다.
    '''
    for info in self.info_storage:
    if info.name == name:
        return info # 찾으면 리턴
    return None # 없으면 None
    '''

    def input_data(self):
        print("데이터 입력을 시작합니다..")
        print("1. 일반, 2. 대학, 3. 회사")
        choice = input("선택>> ").strip()
        
        if choice not in ("1", "2", "3"):
            print("잘못된 선택입니다. 입력 취소.\n")
            return

        # 1. 공통 필수 데이터 입력
        name = input("이름: ")
        phone = input("전화번호: ")
        
        # 2. 선택에 따른 자식 객체 분기 생성 (코드 중복 최소화)
        if choice == "1":
            info = PhoneInfo(name, phone)
        elif choice == "2":
            major = input("전공: ")
            info = PhoneUnivInfo(name, phone, major)
        elif choice == "3":
            company = input("회사: ")
            info = PhoneCompanyInfo(name, phone, company)

        # 3. 공통 선택 데이터 입력 (단축 평가 활용)
        info.birth = input("생년월일(선택): ").strip() or None
        info.region = input("지역(선택): ").strip() or None

        #self.info_storage.append(info)
        if info in self.info_storage:
            print("이미 존재하는 데이터입니다. 입력 취소.\n")
        else:
            self.info_storage.add(info)
            print("데이터 입력이 완료되었습니다. \n")

    def search_data(self):
        print("데이터 검색을 시작합니다..")
        name = input("이름: ")
        
        # 인덱스 번호가 아니라 데이터 객체를 직접 가져옵니다.
        info = self._find_info_by_name(name)
        if not info:
            print("해당하는 데이터가 존재하지 않습니다. \n")
        else:
            info.show_phone_info()  # 다형성에 의해 알맞은 형식이 출력됩니다.
            print("데이터 검색이 완료되었습니다. \n")
            
    def update_data(self):
        print("데이터 수정을 시작합니다..")
        name = input("수정할 이름: ")
        
        info = self._find_info_by_name(name)
        if not info:
            print("해당하는 데이터가 존재하지 않습니다. \n")
        else:
            print(f"[{name}] 님의 정보를 새로 입력해 주세요.")
            info.phone_number = input("새 전화번호: ")
            
            # 💡 [변경] isinstance()를 활용한 객체 타입별 맞춤형 속성 수정
            if isinstance(info, PhoneUnivInfo):
                info.major = input("새 전공: ")
            elif isinstance(info, PhoneCompanyInfo):
                info.company = input("새 회사: ")
                
            info.birth = input("새 생년월일(선택): ").strip() or None
            info.region = input("새 지역(선택): ").strip() or None
            print("데이터 수정이 완료되었습니다. \n")

    def delete_data(self):
        print("데이터 삭제를 시작합니다..")
        name = input("이름: ")
        
        info = self._find_info_by_name(name)
        if not info:
            print("해당하는 데이터가 존재하지 않습니다. \n")
        else:
            # 💡 [변경] 방 번호로 지우는 pop(idx) 대신, 객체 자체를 넘겨 지우는 remove(obj) 사용
            #self.info_storage.remove(info)
            self.info_storage.discard(info)
            print("데이터 삭제가 완료되었습니다. \n")
    
    def show_all_data(self):
        print("==========================================================================")
        print(f"{'이름':<10} {'전화번호':<15} {'생년월일':<12} {'지역':<10} {'추가정보(전공/회사)':<15}")
        print("-" * 74)
        for info in self.info_storage:
            info.show_phone_info()
        print("==========================================================================")

    def backup_data(self):
        # 외부 대신 내부에서 스스로 repository를 호출해 저장합니다.
        self.repository.save(self.info_storage)

instance = PhoneBookService()
import csv
import os
from models.phone_info import PhoneInfo, PhoneUnivInfo, PhoneCompanyInfo

class PhoneBookRepository:
    def __init__(self, file_name="step07/data/phone_book.csv"):
        self.file_name = file_name

    # 💾 1. 데이터 저장 (Save)
    def save(self, data_list):
        with open(self.file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            # 데이터 분석 및 역조립을 위해 분류(group)와 추가정보(memo) 컬럼을 설계합니다.
            writer.writerow(["name", "phone", "birth", "region", "group", "memo"])
            
            for info in data_list:
                # 💡 객체의 실제 타입을 검사하여 CSV 파일에 적힐 값들을 분기합니다.
                if isinstance(info, PhoneUnivInfo):
                    group = "대학"
                    memo = info.major
                elif isinstance(info, PhoneCompanyInfo):
                    group = "회사"
                    memo = info.company
                else:
                    group = "일반"
                    memo = ""  # 일반 친구는 추가 정보가 없음
                
                writer.writerow([info.name, info.phone_number, info.birth, info.region, group, memo])
        print(f"💾 [{self.file_name}] 파일에 데이터가 안전하게 백업되었습니다.")

    # 📂 2. 데이터 불러오기 및 복원 (Load)
    def load(self):
        #loaded_data = []
        loaded_data = set()
        if not os.path.exists(self.file_name):
            return loaded_data  # 파일이 없으면 빈 리스트 리턴 (최초 실행 대비)
            
        with open(self.file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # 헤더(첫 행) 건너뛰기
            
            for row in reader:
                name, num, birth, region, group, memo = row
                
                # 파일의 빈 문자열("") 데이터를 파이썬의 None 객체로 원래대로 복원
                birth = birth if birth != "" else None
                region = region if region != "" else None
                
                # 💡 파일에 기록된 'group' 텍스트를 보고 알맞은 자식 클래스의 객체로 부활시킵니다!
                if group == "대학":
                    info = PhoneUnivInfo(name, num, major=memo, birth=birth, region=region)
                elif group == "회사":
                    info = PhoneCompanyInfo(name, num, company=memo, birth=birth, region=region)
                else:
                    info = PhoneInfo(name, num, birth=birth, region=region)
                    
                #loaded_data.append(info)
                loaded_data.add(info)
        return loaded_data

import csv
import os
from Phone_Info import PhoneInfo, phoneunlvInfo, PhonecommpanyInfo

class PhoneBookRepository:
    def __init__(self, file_name="phone_book.csv"):
        self.file_name = file_name


    def save(self, data_list):
        with open(self.file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "birth", "region", "group", "memo"])
            
            for info in data_list:
                if isinstance(info, phoneunlvInfo):
                    group = "대학"
                    memo = info.major
                elif isinstance(info, PhonecommpanyInfo):
                    group = "회사"
                    memo = info.commpany
                else:
                    group = "일반"
                    memo = ""  # 일반 친구는 추가 정보가 없음
                
                writer.writerow([info.name, info.phone_number, info.birth, info.region, group, memo]) # type: ignore
        print(f"💾 [{self.file_name}] 파일에 데이터가 안전하게 백업되었습니다.")

    def load(self):
        loaded_data = []
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
                    info = phoneunlvInfo(name, num, major=memo, birth=birth, region=region) # type: ignore
                elif group == "회사":
                    info = PhonecommpanyInfo(name, num, commpany=memo, birth=birth, region=region) # type: ignore
                else:
                    info = PhoneInfo(name, num, birth=birth, region=region) # type: ignore
                    
                loaded_data.append(info)
        return loaded_data
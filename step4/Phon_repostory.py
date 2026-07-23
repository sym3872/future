import csv
import os
from Phone_Info import PhoneInfo, phoneunlvInfo, PhonecommpanyInfo
from phone_service import Phon_Service

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
                    memo = ""  
                
                writer.writerow([info.name, info.phone_number, info.brith, info.rejon, group, memo]) 
        print(f" [{self.file_name}] 파일에 데이터가 안전하게 백업되었습니다.")

    def load(self):
        loaded_data = []
        if not os.path.exists(self.file_name):
            return loaded_data  
            
        with open(self.file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # 헤더(첫 행) 건너뛰기
            
            for row in reader:
                if not row:
                    continue
                name, num, birth, region, group, memo = row
                
                
                birth = birth if birth != "" else None
                region = region if region != "" else None
                
                if group == "대학":
                    info = phoneunlvInfo(name, num, major=memo, birth=birth, region=region) # type: ignore
                elif group == "회사":
                    info = PhonecommpanyInfo(name, num, commpany=memo, birth=birth, region=region) # type: ignore
                else:
                    info = PhoneInfo(name, num, birth=birth, region=region) # type: ignore
                    
                loaded_data.append(info)
        return loaded_data
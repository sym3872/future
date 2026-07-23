# ==========================================
# 1. 부모 클래스 (기본 연락처 정보)
# ==========================================

class PhoneInfo:      # 클래스명은 파이썬도 자바와 동일하게 대문자로 시작하는 카멜케이스를 사용합니다.
    def __init__(self, name, num, birth=None, region=None):
        self.name = name
        self.phone_number = num
        self.birth = birth
        self.region = region

    def show_phone_info(self):
        # 데이터가 None일 경우 빈 문자열로 처리하여 가독성 유지
        birth_str = self.birth if self.birth is not None else ""
        region_str = self.region if self.region is not None else ""
        
        # 각 항목별 출력 너비 지정 (이름 10칸, 전화번호 15칸, 생일 12칸, 지역 10칸)
        # 한글 깨짐이나 밀림을 방지하기 위해 좌측 정렬(:<) 사용
        print(f"{self.name:<10} {self.phone_number:<15} {birth_str:<12} {region_str:<10}")
   
    # 1. 이름이 같으면 == 연산 시 True가 나오게 설정
    def __eq__(self, other):
        if isinstance(other, PhoneInfo):
            return self.name == other.name
        return False

    # 2. 이름이 같으면 같은 해시값이 나오게 설정 (set 중복 체크의 핵심)
    def __hash__(self):
        return hash(self.name)
    
# ==========================================
# 2. 자식 클래스 A (대학 친구 정보)
# ==========================================
class PhoneUnivInfo(PhoneInfo):
    # 생성자에서 year 매개변수를 완전히 제거했습니다.
    def __init__(self, name, num, major, birth=None, region=None):
        super().__init__(name, num, birth, region)
        self.major = major

    def show_phone_info(self):
        birth_str = self.birth if self.birth is not None else ""
        region_str = self.region if self.region is not None else ""
        major_str = self.major if self.major is not None else ""
        print(f"{self.name:<10} {self.phone_number:<15} {birth_str:<12} {region_str:<10} {major_str:<15}")  # 전공 정보만 오른쪽에 붙여 출력 후 줄바꿈


# ==========================================
# 3. 자식 클래스 B (회사 동료 정보)
# ==========================================
class PhoneCompanyInfo(PhoneInfo):
    def __init__(self, name, num, company, birth=None, region=None):
        super().__init__(name, num, birth, region)
        self.company = company

    def show_phone_info(self):
        birth_str = self.birth if self.birth is not None else ""
        region_str = self.region if self.region is not None else ""
        company_str = self.company if self.company is not None else ""
        print(f"{self.name:<10} {self.phone_number:<15} {birth_str:<12} {region_str:<10} {company_str:<15}")  # 회사 정보만 오른쪽에 붙여 출력 후 줄바꿈
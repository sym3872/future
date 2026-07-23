class PhoneInfo:
    """전화번호부 정보 클래스

    필수: name, phone_number
    선택: brith(생일), rejon(지역) - 입력만 할 수도 있음 (선택적)
    """
    def __init__(self, name, phone_number, brith = None, rejon = None):    # type: ignore
        self.name = name
        self.phone_number = phone_number
        self.brith = brith # type: ignore
        self.rejon = rejon # type: ignore

    def show(self):
        birth_str = self.brith if self.brith is not None else ""  # type: ignore
        rejon_str = self.rejon if self.rejon is not None else "" # type: ignore

        print(f"{self.name:<10} {self.phone_number:<20} {birth_str:<15} {rejon_str:<10}")
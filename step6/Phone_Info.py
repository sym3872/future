class PhoneInfo:
    def __init__(self, name, phone_number, brith = None, rejon = None):    # type: ignore
        self.name = name
        self.phone_number = phone_number
        self.brith = brith # type: ignore
        self.rejon = rejon # type: ignore

    def show(self):
        birth_str = self.brith if self.brith is not None else ""  # type: ignore
        rejon_str = self.rejon if self.rejon is not None else "" # type: ignore

        print(f"{self.name:<10} {self.phone_number:<20} {birth_str:<15} {rejon_str:<10}")

class phoneunlvInfo(PhoneInfo):
    def __init__(self, name, phone_number,major, brith = None, rejon = None):    # type: ignore
        super().__init__(name, phone_number, brith, rejon) # type: ignore
        self.major = major

    def show(self):
        birth_str = self.brith if self.brith is not None else ""  # type: ignore
        rejon_str = self.rejon if self.rejon is not None else "" # type: ignore
    
        print(f"{self.name:<10} {self.phone_number:<20} {self.major:<15} {birth_str:<15} {rejon_str:<10}")
    
    
        

class PhonecommpanyInfo(PhoneInfo):
    def __init__(self, name, phone_number,commpany, brith = None, rejon = None):    # type: ignore
        super().__init__(name, phone_number, brith, rejon) # type: ignore
        self.commpany = commpany
    
    def show(self):
        birth_str = self.brith if self.brith is not None else ""  # type: ignore
        rejon_str = self.rejon if self.rejon is not None else "" # type: ignore
        
        print(f"{self.name:<10} {self.phone_number:<20} {self.commpany:<15} {birth_str:<15} {rejon_str:<10}")


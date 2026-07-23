from Phone_Info import PhoneInfo

def main():
    person1 = PhoneInfo("Kim","010-1234-5678","2000-04-01",'seoul')
    person2 = PhoneInfo("Kim","010-1234-5678","2000-04-01")
    person3 = PhoneInfo("Kim","010-1234-5678","2000-04-01",'seoul')

    print(person1)
    print(person2)
    print(person3)

if __name__ == "__main__":
    main()
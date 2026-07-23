import csv


class Phone_reposetory:
    def asdad(self):
        with open("students.csv", "w", encoding="utf-8", newline="") as file:
         writer = csv.writer(file)

        writer.writerow(["name", "score"])
        writer.writerow(["민수", 90])
        writer.writerow(["지훈", 80])
        writer.writerow(["서준", 95])

print("CSV 파일 저장 완료")

# with open("students.csv", "r", encoding="utf-8") as file:
#   print(file.read())

# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     students = list(reader)
#     print(students)


import csv
with open("students.csv", "r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  students = list(reader)



# 輸出端(main)
print("=======================================\nClass CSV Analyzer\n========================================")
print("學生人數:", len(students))

for s in students:
    chinese = int(s["chinese"])
    english = int(s["english"])
    math = int(s["math"])
    average = (chinese + english + math) / 3
    print(s["name"], "平均為 ", round(average, 2))
print("-----------------------------------------")

T = 0
for t in students:
    chinese = int(t["chinese"])
    english = int(t["english"])
    math = int(t["math"])
    ave = (chinese + english + math) / 3
    T += ave
    if(ave > average):
        average = ave
        s = t

print("平均最高:",s["name"], round(average, 2))

for t in students:
    math = int(t["math"])
    if(math > int(s["math"])):
        s = t

print("數學最高:",s["name"], s["math"])
Ta = T / len(students)
print("全班平均", round(Ta, 2))

print("\n=================Challenge=================\n")

# Challenge A
print("Challenge A:找出平均低於 60 分的學生\n")
for s in students:
    ave=(int(s["chinese"]) + int(s["english"]) + int(s["math"])) / 3
    if ave < 60:
        print(s["name"], "平均為", round(ave, 2))

# Challenge B
print("Challenge B:找出三科都及格的學生\n")
for s in students:
    if(int(s["chinese"]) >= 60 and int(s["english"]) >= 60 and int(s["math"]) >= 60):
        print(s["name"],",")
print("三科都及格")

# Challenge C
print("\nChallenge C:找出「數學比英文高 10 分以上」的學生\n")
for s in students:
    if(int(s["math"]) - int(s["english"]) >= 10):
        print(s["name"],",")
print("數學比英文高 10 分以上")

# Challenge D
print("\nChallenge D:將輸出結果按照平均分數由高到低排列\n")
for s in students:
    ave=(int(s["chinese"]) + int(s["english"]) + int(s["math"])) / 3
    s["average"] = ave
for s in sorted(students, key=lambda x: x["average"], reverse=True):
    print(s["name"], "平均為", round(s["average"], 2))
print('\n')
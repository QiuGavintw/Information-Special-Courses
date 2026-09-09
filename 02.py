#0909-base
scores = [78, 92, 65, 88, 73, 95, 81, 69, 84, 90 ,10 ,10]

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)
top3 = sorted(scores, reverse=True)[:3] 

# reverse=True→由大到小排序, [:3]→取3名  
# reverse=False→由小到大排序

print("≡≡≡ 成績分析 ≡≡≡")
print("資料筆數:", len(scores))
print("最高分:", highest)
print("最低分:", lowest)
print("平均:", average)
print("前3名成績:", top3)

#0909-base-bonus

passed = [
    s for s in scores
        if s >= 60 
]

print("及格人數:", len(passed))
print("及格率:", len(passed) / len(scores) * 100, "%")
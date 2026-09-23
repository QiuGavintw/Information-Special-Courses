
scores = [78, 92, 65, 88, 73, 95, 81, 69, 84, 90 ,30]

# 1. 找出高於平均的分數
average = sum(scores) / len(scores)
above_average = [score for score in scores if score > average]
print("高於平均：", above_average)

# 2. 建立排行榜
ranking = sorted(scores, reverse=True)
print("排行榜：", ranking)


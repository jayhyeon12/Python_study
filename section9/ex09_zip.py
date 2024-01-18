names = ["kim1", "kim2", "kim3"]
scores = [99, 98, 97]

#print(names)
#print(scores)

# print(list(zip(names, scores)))

for person in zip(names, scores):
    name, score = person
    print(f"{name}님은 {score}점입니다.")
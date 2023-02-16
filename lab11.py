print("학번: 201704033  이름 : 한지훈")
dict1={"사과":1000, "포도": 2000, "참외": 5000, "메론": 10000, "수박": 9000, "아보카도":5000, "애플망고":10000, "복숭아":5000}
list1 = list(dict1.keys())
data1 = {str(i) : dict1[i] for i in list1 if (len(i) == 2 and dict1[i]>=5000)}
print(data1)
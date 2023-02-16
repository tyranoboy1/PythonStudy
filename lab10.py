import  random
import  re
print("학번: 201704033  이름 : 한지훈")
print("당첨자 추첨 프로그램")
person = {}
num = int(input("응모자의 수를 입력하세요: " ))

if(num<=0):
    print("0을 입력하셨습니다.")
    print("프로그램을 종료합니다.")
else:
    for num in range(1,num+1):
        name=input("이름:")
        phonenum=(input("전화번호:"))
        person[name]=phonenum
print("입력 완료")

list1 = list(person.keys())

num1 = int(input("당첨 인원 수: " ))

list1 = random.sample(list1,num1)
for n in list1:
    name1 =re.sub("^(\w)(\w)(\w)$","\g<1>*\g<3>", n)
    number1=re.sub("(^[0-9]{3}\-[0-9]{4}\-[0-9]{4})",person[n][-4:], person[n])
    print(name1,number1)











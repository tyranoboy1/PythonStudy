print("학번: 201704033  이름 : 한지훈")
num = int(input("정수를 입력하세요 : " ))
a = [num for num in range(0, num) if num%3==0]
print("0부터 15까지 3의 배수는",a,"이고, 3의 배수의 합은", sum(a),"입니다.")
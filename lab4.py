print("학번: 201704033  이름 : 한지훈")
print("덧셈을 하고싶은 정수들을 입력하세요! 0을 입력시 종료됩니다.")
sum =0;
num = int(input())
while(num > 0 or num < 0):
    sum = sum + num;
    num = int(input())
else:
    print("총 합은",sum," 입니다.")

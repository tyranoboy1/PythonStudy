print("학번: 201704033  이름 : 한지훈")
stu = 1
sum = 0
avg = 0
min =0
Records={}
pnum = int(input("몇명의 학생 데이터를 입력받겠습니까? " ))#학생수를 입력받는 수
if pnum<=0:#입력 받은 학생수가 0이거나 0보다 작을때
    print("0을 입력하셨습니다.")
    print("프로그램을 종료합니다")
elif pnum>0:#입력받은 학생수가 0보다 클때
    while True:
        print(stu,"번째 학생 성적")
        name = input("이름 : ")
        score = int(input("점수 : "))
        print("입력완료")
        stu+=1
        sum=sum+score
        avg=sum/3
        fmt = "|{0:<7}|{1:>4}|{2:>5}"
        print((fmt.format(name, score, min)))
        for name, score in sorted(Records.items()):
            min = score - avg
        if stu>pnum:
            print("합계점 : ", sum)  # 합계출력
            print("평균점 : ", avg)  # 평균출력
            print("| 이름  |점수|차이")
            break





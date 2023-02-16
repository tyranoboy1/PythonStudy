print("학번: 201704033  이름 : 한지훈")
pwd = input("패스워드를 입력해주세요:")
while str.isnumeric(pwd):#입력 받은 패스워드가 숫자로만 이루어져 있을 때 반복
    print("숫자로만 이루어진 비밀번호 입니다. 다시 입력하세요")
    pwd = input("패스워드를 입력해주세요:")#다시 비밀 번호를 입력 받게끔 함


result = len(pwd)#비밀번호의 길이를 결과 값에 저장
if(result>=9):#길이 결과 값으로 길이에 따른 안전성 측정 조건문
    print("당신의 패스워드 안정성 정도는 'Good' 입니다.")
elif(result>=5 and result<9):
    print("당신의 패스워드 안정성 정도는 'Normal' 입니다.")
elif(0<result and result<5):
    print("당신의 패스워드 안정성 정도는 'Bad' 입니다.")

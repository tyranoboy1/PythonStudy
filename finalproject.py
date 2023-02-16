import requests
import xmltodict
import json
import numpy as np
from urllib import parse
import pandas as pd
import matplotlib as plt
import datetime
import math
import re

key = '73567a6f7a73756e38384655755572'#api 인증키
total_information = 4000 #api의 총수는 46302

corona19_id = []
corona19_date = []
corona19_no = []
corona19_country = []
corona19_personal = []
corona19_area = []
corona19_travel_history = []
corona19_contact_history = []
corona19_corrective = []
corona19_leave_status = []
corona19_moving_path =[]
corona19_idate =[]
corona19_mdate = []

for i in range(1, math.ceil(total_information / 1000) + 1):

    end = i * 1000
    start = end - 1000 + 1

    if end > total_information:
        end = total_information

    url = f'http://openapi.seoul.go.kr:8088/{key}/xml/Corona19Status/{start}/{end}/'
    re = requests.get(url)
    dict_data = xmltodict.parse(re.text)#xml 데이터를 dict으로 변환
    json_data = json.dumps(dict_data)#dict_data를 json문자열로 변환
    dict_data = json.loads(json_data)#json문자열을 파이썬 오브젝트로 변환

    for u in dict_data['Corona19Status']['row']:
        corona19_id.append(u['CORONA19_ID'])
        corona19_date.append(u['CORONA19_DATE'])
        corona19_no.append(u['CORONA19_NO'])
        corona19_country.append(u['CORONA19_COUNTRY'])
        corona19_personal.append(u['CORONA19_PERSONAL'])
        corona19_area.append(u['CORONA19_AREA'])
        corona19_travel_history.append(u['CORONA19_TRAVEL_HISTORY'])
        corona19_contact_history.append(u['CORONA19_CONTACT_HISTORY'])
        corona19_corrective.append(u['CORONA19_CORRECTIVE'])
        corona19_leave_status.append(u['CORONA19_LEAVE_STATUS'])
        corona19_moving_path.append(u['CORONA19_MOVING_PATH'])
        corona19_idate.append(u['CORONA19_IDATE'])
        corona19_mdate.append(u['CORONA19_MDATE'])

df = pd.DataFrame({"연번": corona19_id,
                   "확진일": corona19_date,
                   "환자번호": corona19_no,
                   "국적": corona19_country,
                   "환자정보": corona19_personal,
                   "지역":  corona19_area,
                   "여행력": corona19_travel_history,
                   "접촉력":  corona19_contact_history,
                   "조치사항":corona19_corrective,
                   "상태": corona19_leave_status,
                   "이동경로": corona19_moving_path,
                   "등록일": corona19_idate,
                   "수정일":  corona19_mdate,
                   })

# 연번, 확진일, 지역, 상태 말고는 다 삭제
df = df.drop(columns=["환자번호","국적","환자정보","여행력","접촉력","조치사항","이동경로","등록일","수정일"])

#확진일의 type을 날짜형으로 변환해줌
df['확진일'] = df['확진일'].apply(pd.to_datetime)

#날짜별로 확진자수 나누기
df["년"] = df["확진일"].dt.year
df["월"] = df["확진일"].dt.month
df["일"] = df["확진일"].dt.day

##############################
#날짜를 입력받고 확진자 수를 구해줌

def coronaday(dayc):
    b = df.loc[df["확진일"]==dayc, ["확진일"]]
    print(dayc, "날짜의 총 확진자 수는 :", len(b), "입니다")

while True:
    dayz = input('날짜를 입력하세요:')

    pat =r'(\d{4})-(\d{1,2})-(\d{1,2})'
    correctdate = bool(re.search(pat,dayz))
    if(correctdate):
        coronaday(dayz)
        break
    else:
        print("날짜형식이 아닙니다.")
        continue
################################

#############################
#지역을 입력받고 확진자수를 구해줌
# b=input("원하는 지역 : ")
#
# def selectarea(area):
#     a = df.loc[df["지역"] ==area, ["지역"]]
#     print(area+ "지역의 확진자 수는 :", len(a), "입니다.")
#
# data = selectarea(b)
##############################





# newdata = df[['확진일','월']]
# month = newdata.groupby('확진일')
#
# a = month.count()
# a.columns =["날짜별확진자수"]
# print(a)
# a.info()

# newdata = df[['확진일','월']]
# month = newdata.groupby('월')
# print(month)
# a = month.count()
# a.columns =["월별확진자수"]
# print(a)
# a.info()






# def coronaday(dayc):
#     b = df.loc[df["확진일"]==dayc, ["확진일"]]
#     print(dayc, "날짜의 총 확진자 수는 :", len(b), "입니다")
# coronaday(dayz)

# newdata = df.groupby([df.index.year, df.index.month])

# newdata = df.iloc[df.index.month.argsort()]
# print(newdata)

#
#
# print(df[["확진일", "년", "월", "일"]])

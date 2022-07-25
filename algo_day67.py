#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 문제 출처 : 프로그래머스

# <2016년>

# [문제 설명]

# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# [제한 조건]

# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

# [입출력 예]

# a	b	result
# 5	24	"TUE"

# [나의 풀이]

import datetime                                               # 날짜 함수 import
def solution(a, b):                                           # 함수 정의
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']  # 요일 list
    return days[datetime.date(2016, a, b).weekday()]          # 2016년 날짜 정보 받아서 요일 인덱스로 전환


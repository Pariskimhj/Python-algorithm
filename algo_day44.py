#!/usr/bin/env python
# coding: utf-8

# In[33]:


# 문제 출처 : SW Expert Academy

# 오늘의 요일을 나타내는 문자열 S가 주어진다. S는 “MON”(월), “TUE”(화), “WED”(수), “THU”(목), “FRI”(금), “SAT”(토), “SUN”(일) 중 하나이다.

# 다음 (즉, 내일 이후의 가장 빠른) 일요일까지는 며칠 남았을까?
 

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 문자열 S가 주어진다.
 

# [출력]

# 각 테스트 케이스마다, 다음 일요일까지 며칠 남았는지를 한 줄에 하나씩 출력한다.

for t in range(int(input())):   # T 입력 받기
    dic = {'MON' : 0, 'TUE' : 1, 'WED' : 2, 'THU' : 3, 'FRI' : 4, 'SAT' : 5, 'SUN' : 6} # 요일 별 숫자 지정
    S = input()                 # S 입력 받기
    a = [6 -v for k, v in dic.items() if S==k] # S가 dic에 있으면 해당 숫자값을 6에서 빼기
    if a[0] == 0:               # 만약 S가 SUN이면
        print(f"#{t+1} 7")      # 7 출력
    else:                       # S가 SUN이 아니면
        print(f"#{t+1}", *(a))  # a의 계산값 출력


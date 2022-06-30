#!/usr/bin/env python
# coding: utf-8

# In[25]:


# 문제 출처 : SW Expert Academy

# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
# 첫 번째 줄에 문자열 S가 주어진다.

# [출력]
# 각 테스트 케이스마다 조건이 만족되면 “Yes”, 아니면 “No” 를 출력하라.

for t in range(int(input())):  # T 입력 받기
    a = {}                     # dict 초기화, 문자 : 문자의 개수
    for w in input():          # 문자열 입력 받아서 한 글자씩 추가
        if w in a:             # a에 이미 key로 문자(w)가 있으면
            a[w] += 1          # 개수 +1
        else:                  # a의 key에 문자가 없으면
            a[w] = 1           # 문자(w) : 1
    if len(a.keys()) == 2 and 2 in set(dic.values()): # 문자가 2개이고 문자 2개의 숫자가 2개이면
        print(f"#{t+1}","Yes")                        # Yes 출력
    else:                                             # 아니면
        print(f"#{t+1}","No")                         # No 출력


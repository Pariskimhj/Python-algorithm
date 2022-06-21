#!/usr/bin/env python
# coding: utf-8

# In[32]:


# 문제 출처 : SW Expert Academy

# 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.
# 같은 문자를 여러 번 짝지어서는 안 된다.
 
# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열의 길이는 1이상 100이하이다.
 

# [출력]

# 각 테스트 케이스 마다 예제와 같은 형식으로 남는 문자를 사전 순서대로 출력한다.
# 만약 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.

for t in range(int(input())):                              # T 입력 받기
    dic_a = {}                                             # 문자 : 빈도 형태로 만들기
    for a in input():                                      # 문자 입력받아 한 글자씩 받아오기
        if a not in dic_a.keys():                          # dic_a의 key에 문자가 없다면
            dic_a[a] = 1                                   # dic_a에 a:1 형태로 저장
        else:                                              # dic_a의 key에 문자가 있으면
            dic_a[a] += 1                                  # dic_a[a]에 1 추가
    list_A = [key for key, value in dic_a.items() if value%2 == 1]  # value가 홀수인 key만 남긴 리스트 만들기
    print(f"#{t+1}",''.join(sorted(list_A)) if len(list_A) else 'Good') # list_A에 아무것도 없으면 Good 출력 있으면 정렬해서 출력


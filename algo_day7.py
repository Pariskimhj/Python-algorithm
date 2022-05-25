#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

# [제약 사항]

# 문자열의 최대 길이는 200이다.

# [입력]

# 알파벳으로 이루어진 문자열이 주어진다.

# [출력]

# 각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.

# [시나리오]
# 1. 알파벳 문자열 받기 input
# 2. 알파벳과 문자열을 대치 -> dic에 알파벳을 키로 저장, 숫자를 value로
# 3. 이 키와 동일하면 value를 출력(빈 칸 두고)

input_data = input()
dic_al = {}
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = [num for num in range(1, 27)]
for a, n in zip(alpha, num):
    dic_al[a] = n
for i in input_data:
    print(dic_al[i], end=' ')


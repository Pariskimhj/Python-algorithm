#!/usr/bin/env python
# coding: utf-8

# In[15]:


# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.

# 내가 푼 방법
num = int(input())
for n in range(num+1):
    print(2**n, end=' ')

# 더 좋은 방법
# print(*[2**i for i in range(int(input())+1)])


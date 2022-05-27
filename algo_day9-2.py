#!/usr/bin/env python
# coding: utf-8

# In[34]:


# 주어진 숫자부터 0까지 순서대로 찍어보세요

# 아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다

#[예시]
# N N-1 N-2 ... 0

# 내가 푼 방법
# print(*[i for i in range(int(input())+1)][::-1])

# 더 좋은 방법
print(*range(int(input()),-1, -1))
# range(N, -1, -1) : 거꾸로 출력, 간격은 -1씩 추가


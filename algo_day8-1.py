#!/usr/bin/env python
# coding: utf-8

# In[16]:


# 주어진 숫자만큼 # 을 출력해보세요.

# 주어질 숫자는 100,000 이하다.

# [시나리오]
# 1. 숫자를 입력 받는다. input
# 2. 숫자만큼 #출력 for

# [내가 푼 방법] 
num = int(input())
for i in range(1, num+1):
    print("#",sep="", end="")
    
# [더 좋은 방법]
# print("#"*int(input()))


#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

# 단, 주어질 숫자는 10000을 넘지 않는다.

# [예제]

# 주어진 숫자가 10 일 경우 출력해야 할 정답은,

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
 
    
num = int(input("정수 입력 > "))
num_list = []
for i in range(1, num+1):
    num_list.append(i)
print(sum(num_list))


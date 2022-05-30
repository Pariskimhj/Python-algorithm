#!/usr/bin/env python
# coding: utf-8

# In[27]:


# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

# [제약 사항]

# N 은 5 이상 50 이하이다.

# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 
# 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.

# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# [시나리오]
# 1. 테스트 케이스 T 입력받기 input
# 2. N 입력받기 input
# 3. N개의 숫자 입력받기 input.split()
# 4. 숫자 sort

for t in range(1, int(input())+1):
    N, num = input(),list(map(int, input().split()))
    print(f"#{t}",*sorted(num))


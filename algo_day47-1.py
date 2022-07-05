#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 문제 출처 : SW Expert Academy

# 1 이상 N 이하의 정수가 적혀 있는 길이 N의 순열 p1, p2, …, pN이 있다. 수열에 있는 모든 숫자는 서로 다르다. 2 ≤ i ≤ N-1이며, pi-1, pi, pi+1 중 pi가 최솟값도, 최댓값도 아니라면 pi를 평범한 숫자라고 정의한다. 주어진 순열에서 평범한 숫자의 개수는 몇 개인가?

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
#     ∙ 첫 번째 줄에 정수 N 이 주어진다. (3 ≤ N ≤ 20)
#     ∙ 이후 N개의 정수 pi가 주어진다. (3 ≤ pi ≤ N) 모든 pi는 서로 다르다.

# [출력]
# 각 테스트 케이스마다 정답을 출력하라.

for t in range(int(input())):               # T 입력 받기
    N = input()                             # N 입력 받기
    p = list(map(int, input().split()))     # p 입력받기
    count = 0                               # 평범한 숫자 세기
    for i in range(len(p)-2):               # 리스트 길이 3씩 끊어서 확인
        pl = p[i:i+3]
        if pl[1] not in (max(pl), min(pl)): # 가운데 숫자가 list의 최대, 최소값이 아니면
            count += 1                      # count 하기
    print(f"#{t+1} {count}")                # 평범한 숫자 출력


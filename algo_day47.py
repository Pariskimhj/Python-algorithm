#!/usr/bin/env python
# coding: utf-8

# In[16]:


# 문제 출처 : SW Expert Academy

# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
 
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
# 위 예제의 정답은 아래와 같이 30 이 된다.

# [제약 사항]

# N 과 M은 3 이상 20 이하이다.

# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 두 번째 줄에는 Ai,
# 세 번째 줄에는 Bj 가 주어진다.

# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

for t in range(int(input())):              # T 입력 받기
    N, M = map(int, input().split())       # N, M 입력 받기
    Ai = list(map(int, input().split()))   # Ai 입력 받기
    Bj = list(map(int, input().split()))   # Bj 입력 받기
    if N > M:                              # N이 M보다 크면
        Ai,Bj = Bj,Ai                      # Ai, Bj 서로 바꾸기
        N,M = M,N                          # Ai, Bj 서로 바꾸기
    m = []                                 # 곱해서 더한 값의 list
    for i in range(M-N+1):                 # 리스트 길이 맞춰주기(처음 인덱스는 0부터 M-N+1까지)
        m.append(sum([a*b for a, b in zip(Ai, Bj[i:N+i])])) # 리스트의 요소끼리 곱한 후 더하기
    print(f"#{t+1} {max(m)}")              # 더한 값 중 최댓값 출력


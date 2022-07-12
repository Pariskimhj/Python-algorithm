#!/usr/bin/env python
# coding: utf-8

# In[36]:


# 문제 출처 : SW Expert Academy

# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.

# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 
# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

# [제약 사항]

# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


# [출력]

# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def ver(array):                                      # 스도쿠 검증 함수 정의
    result = []                                      # 검증 결과 저장
    for x in range(9):                               # 9개 검증
        if ''.join(sorted(array[x])) == '123456789': # 1개 단위 정렬 후 123456789가 맞으면
            result.append(1)                         # 1 추가
    if sum(result) == 9:                             # 9개가 다 123456789이면
        return True                                  # True 반환
    else:                                            # 1개라도 123456789가 아니면
        return False                                 # False 반환
for t in range(int(input())):                        # T 입력 받기
    a = [input().split() for _ in range(9)]          # array 입력 받기
    result_1 = ver(a)                                # 가로 모음 스도쿠 검증
    r_a = list(zip(*a))                              # 전치 행렬
    result_2 = ver(r_a)                              # 세로 모음 스도쿠 검증
    l = []                                           # 3*3 배열 모음 list
    for x in range(3):
        for y in range(3):
            f1 = [a[3*x+p][3*y:3*y+3] for p in range(3)] # 3*3 list 생성 / [[i, i, i],[i, i, i],[i, i, i]] 형태
            f2 = [f4 for f3 in f1 for f4 in f3]      # 정사각형 list 2중 리스트 풀기
            l.append(f2)                             # 3*3 배열 모음에 추가
    result_3 = ver(l)                                # 3*3 배열 스도쿠 검증
    if result_1 + result_2 + result_3 == 3:          # 가로, 세로, 3*3 배열이 모두 스도쿠 검증을 통과했으면
        print(f"#{t+1} {1}")                         # 1 출력
    else:                                            # 스도쿠 검증 통과 못 했을 시
        print(f"#{t+1} {0}")                         # 0 출력


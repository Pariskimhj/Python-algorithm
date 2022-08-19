#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# algo_day75
# 문제 출처 : 백준
# [OX퀴즈]

# <문제>
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# <입력>
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# <출력>
# 각 테스트 케이스마다 점수를 출력한다.

# <나의 풀이>

for _ in range(int(input())):       # 테스트 케이스 개수 입력 받기
    result = []                     # 점수 리스트
    count = 0                       # count 초기화
    for i in input():               # 퀴즈 결과 별 확인
        if i == 'O':                # 퀴즈 결과가 O이면
            count += 1              # count+1
            result.append(count)    # 매 퀴즈 결과 별 count를 result에 저장
        else:                       # 퀴즈 결과가 X이면
            count = 0               # count 초기화
    print(sum(result))              # 총 점수 출력


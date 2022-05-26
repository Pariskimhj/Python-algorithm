#!/usr/bin/env python
# coding: utf-8

# In[22]:


# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

# [제약 사항]

# 각 수는 1이상 10000이하의 정수이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
 
# [시나리오]
# 1. test case 입력 받기 input
# 2. 숫자 2개를 입력 받는다 input
# 3. 숫자의 몫과 나머지 리스트 만들기 map,%,//

# [내가 푼 방법]
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(t, a//b, a%b))
    
# [더 좋은 방법]
# for t in range(int(input())):print(f'#{t+1}',*divmod(*map(int,input().split())))

# divmod 함수 : x와 y를 받으면 x를 y로 나눈 몫과, 나머지가 들어있는 tuple을 리턴


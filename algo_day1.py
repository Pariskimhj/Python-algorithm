#!/usr/bin/env python
# coding: utf-8

# In[30]:


# 1일 1 알고리즘 문제 풀기(22.05.20)

# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
# -----------------------------------------------------------
# 시나리오
# 테스트 케이스의 개수 입력 받기
# 테스트 케이스마다 10개의 숫자 입력받기
# 10개의 숫자 중 홀수만 추출
# 홀수 더하기
# 케이스마다 #t로 10개 숫자의 홀수의 합 추출

T = int(input("test case 입력 > "))
dic_a = {}
for t in range(1, T+1):
    numbers = input("숫자 10개 입력").split()
    numbers = map(lambda x: int(x), numbers)
    number = [num for num in numbers if num%2 == 1]
    dic_a[t] = sum(number)
for test_num, num_sum in dic_a.items():
    print("#{} {}".format(test_num, num_sum))


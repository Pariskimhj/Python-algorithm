#!/usr/bin/env python
# coding: utf-8

# In[23]:


# 문제 출처: SW Expert Academy

# 1 이상 100만(10**6) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

# 참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

# [입력]

# 이 문제의 입력은 없다.

# [출력]

# 1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

def prime_list(n):                        # 함수 생성
    array = [False] + [True] * n          # 에라토스테네스의 체 초기화: index 0은 False로, n개 요소에 True 설정(소수로 간주)
    for i in range(2, int(n ** 0.5) + 1): # 2부터 n의 제곱근까지의 숫자
        if array[i] == True:              # i가 소수인 경우
            for j in range(i+i, n+1, i):  # i이후 i의 배수들을 False로 변경
                array[j] = False
    return [i for i in range(2, n+1) if array[i] == True] # 소수 목록 리턴
print(*prime_list(10**6))                    # 소수 목록 출력


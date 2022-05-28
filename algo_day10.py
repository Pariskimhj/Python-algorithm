#!/usr/bin/env python
# coding: utf-8

# In[22]:


# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

# 다음과 같은 수 분포가 있으면,

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

# 최빈수는 8이 된다.

# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

# [제약 사항]

# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
 
# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

# [출력]

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.


# [시나리오]
# 1. 테스트 케이스를 입력 받는다 input
# 2. 테스트 케이스의 번호 입력 받기 input
# 3. 1000명의 점수 입력 받아 리스트에 저장 input split
# 4. 딕셔너리에 저장 for
# 5. values 값이 가장 큰 값을 출력
# 6. 만약 values가 같으면 key를 비교해서 큰 것의 value를 출력
# 7. #t 최빈수로 출력하기

# [내가 푼 방법]

# 테스트 케이스 숫자 입력
T = int(input())
dic_a = {}
list_a = []
list_b = []
for t in range(1, T + 1):
    # t 입력
    tt = int(input())
    # input 데이터 리스트로 저장
    score = list(map(int, input().split()))
    # 딕셔너리에 {점수 : 점수의 개수} 형태로 저장
    for s in score:
        if s not in dic_a.keys():
            dic_a[s] = 1
        else:
            dic_a[s] += 1
    # 딕셔너리의 value값을 리스트로 저장
    for value in dic_a.values():
        list_a.append(value)
    # value의 max값 즉, 최빈값 m구하기
    m = max(list_a)
    # 만약 dic_a의 value가 최빈값이라면 그 value의 key값을 list_b에 저장
    for key, value in dic_a.items():
        if value == m:
            list_b.append(key)
    # list_b의 max값을 출력하면 최빈값 구하기 완료
    print("#{} {}".format(t, max(list_b)))
    # 다음 케이스를 위해 dic_a, list_a, list_b 초기화
    dic_a = {}
    list_a = []
    list_b = []

    
    
# [더 좋은 방법]
for t in range(int(input())):
    n,d=input(),input().split()
    print(f'#{n} {max(sorted(d)[::-1],key=d.count)}')
    
# 1. t값을 n에 저장, score를 d라는 list에 저장
# 2. sorted(d)으로 list d를 오름차순으로 정렬
# 3. [::-1]로 list 내부의 값을 내림차순으로 정렬
# 즉, list 내의 가장 큰 값이 제일 앞에 오도록
# 4. max함수의 key는 key함수를 만족시키는 value값 중 가장 큰 값을 구하겠다는 의미
# 5. key=d.count는 d내부의 원소들을 count하고 이 count 결과가 가장 큰 것의 원소를 리턴한다
# 6. 리스트 내의 최빈값 구하기 완성

# max함수의 key값에 적용하고 싶은 함수를 넣으면 


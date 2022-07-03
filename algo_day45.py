#!/usr/bin/env python
# coding: utf-8

# In[15]:


# 문제 출처 : SW Expert Academy

# 주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

# Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

# 위 문장에서 ti 를 검색하면, 답은 4이다.

# [제약 사항]

# 총 10개의 테스트 케이스가 주어진다.
# 문장의 길이는 1000자를 넘어가지 않는다.
# 한 문장에서 검색하는 문자열의 길이는 최대 10을 넘지 않는다.
# 한 문장에서는 하나의 문자열만 검색한다. 

# [입력]

# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장이 주어진다.

# [출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

for _ in range(10):                          # tast case 10번
    t = input()                              # tast case 번호 입력 받기
    s = input()                              # 검색할 문자열 입력 받기
    string = input()                         # 문장 입력 받기
    count = 0                                # 개수 초기화
    for i1 in range(len(string)-(len(s)-1)): # 문장에서 검색할 범위 설정(문자열의 길이 고려)
        result = ''                          # 추출된 문자열 초기화
        for i2 in range(len(s)):             # 문자열의 개수를 지정
            result += string[i1+i2]          # 문자열의 길이만큼 문자열 추출
            if result == s:                  # 만약 문자열이 검색할 문자열과 같으면
                count += 1                   # 세기
    print(f"#{t} {count}")                   # 출력


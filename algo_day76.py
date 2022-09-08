#!/usr/bin/env python
# coding: utf-8

# In[58]:


# 문제 출처 : 프로그래머스

# [KAKAO TECH INTERNSHIP] 성격 유형 검사하기

def solution(survey, choices):                                       # 함수 정의
    answer = ''                                                      # 답변
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0} # 성격유형 점수 초기화
    for s, c in zip(survey, choices):                                # 같은 index의 survey와 choices 매치해서 확인
        if c > 4:                                                    # choices가 4 초과이면
            score[s[1]] += c-4                                       # survey의 앞 유형에 점수 c-4만큼 추가
        elif c < 4:                                                  # choices가 4 미만이면
            score[s[0]] += 4-c                                       # survey의 뒤 유형에 점수 4-c만큼 추가
    answer+='R' if score['R'] >= score['T'] else 'T'                 # 점수가 R >= T 이면 성격유형은 R, R < T 이면 T
    answer+='C' if score['C'] >= score['F'] else 'F'                 # 점수가 C >= F 이면 성격유형은 C, C < F 이면 F
    answer+='J' if score['J'] >= score['M'] else 'M'                 # 점수가 J >= M 이면 성격유형은 J, J < M 이면 M
    answer+='A' if score['A'] >= score['N'] else 'N'                 # 점수가 A >= N 이면 성격유형은 A, A < N 이면 N
    return(answer)                                                   # 성격유형 리턴


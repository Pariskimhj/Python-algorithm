#!/usr/bin/env python
# coding: utf-8

# In[75]:


# 문제 출처 : 프로그래머스

# [문제 설명]

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# [제한사항]

# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"

# [입출력 예 설명]

# 예제 #1
# "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #2
# "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

# 예제 #3
# "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

# [나의 풀이]
# 시간 복잡도 고려

def solution(participant, completion):  # 함수 정의
    d = {}                              # 딕셔너리 초기화 {참여자 : 숫자}
    for p in participant:               # 참여자 별 확인
        if d.get(p):                    # 딕셔너리에 참여자가 key로 있으면
            d[p] += 1                   # value+1
        else:                           # 참여자가 없으면
            d[p] = 1                    # 참여자 추가
    for c in completion:                # 완주자는
        d[c] -= 1                       # 참여자 수에서 빼기
    for k in d:                         # 참여자 별 확인
        if d[k] == 1:                   # 완주를 못한 사람이면
            return k                    # 그 참여자를 출력

# [다른 풀이]
# 시간 복잡도 고려

from collections import Counter as C        # import
def solution(participant, completion):      # 함수 정의
    answer = C(participant) - C(completion) # 참여자 수 - 완주자 수 / 남은 {참여자 : 수}로 반환
    return list(answer)[0]                  # [key]로 반환 후 출력


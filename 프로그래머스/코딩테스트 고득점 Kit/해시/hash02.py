def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    answer = participant[-1]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # leo

# 처음 생각한 코드
def solution_ex(participant, completion):
    answer = ''
    set_participant = set(participant)
    set_completion = set(completion)
    answer = list(set_participant - set_completion)[0]

    return answer
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution_ex(["mislav", "stanko", "mislav", "ana"]	, ["stanko", "ana", "mislav"]))

# 프로그래머스 다른사람 풀이1
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# 프로그래머스 다른사람 풀이2
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

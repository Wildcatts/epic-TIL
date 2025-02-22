def solution(progresses, speeds):
    answer = []
    '''
    각 작업이 몇일 걸리는지 계산해서 리스트에 저장
    리스트의 첫번째 작업 완료일을 기준으로 그 값보다 작은 값을 answer에 추가
    그 다음 값이 걸리는 시간보다 크면 다시 계산
    리스트가 비면 종료
    '''
    days = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)

    while len(days) > 0:
        count = 1
        day = days.pop(0)
        while len(days) > 0 and day >= days[0]:
            count += 1
            days.pop(0)
        answer.append(count)        

    return answer
        
        


# 테스트 코드
progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
   

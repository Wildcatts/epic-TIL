def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            if location == 0:
                break
            else:
                priorities.pop(0)
                location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

def another_solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# 테스트 출력
print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
print(solution([1, 1, 1, 1, 1, 1], 0)) # 1
print(solution([1, 1, 1, 1, 1, 1], 5)) # 6

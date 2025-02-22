def solution(arr):
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                continue
            else:
                stack.append(i)
    return stack
# 테스트 코드
arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
'''
리스트가 비어있다 -> 숫자를 추가한다
다음 숫자와 비교해서 같다 -> 건너뛴다
다음 숫자와 비교해서 다르다 -> 다시 추가한다
순서대로 하나씩 넣어준다
'''

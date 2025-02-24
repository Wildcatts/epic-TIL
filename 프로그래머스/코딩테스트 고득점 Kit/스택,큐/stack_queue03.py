def solution(s):
    answer = True
        
    stack = []
    
    for i in s:
        if len(stack) == 0:
            if i == ')':
                return False
            else:
                stack.append(i)
        else:
            if stack[-1] != i:
                stack.pop()
                continue
            else:
                stack.append(i)
                
    if len(stack) == 0:
        return True
    else:
        return False

# 과거에 풀었던 문제

'''
프로그래머스 해시 1번 문제
'''

def solution(nums):
    answer = 0
    
    number = len(nums) / 2

    # 중복을 제거한 리스트
    hash_nums = (set(nums))

    if number < len(hash_nums):
        answer = number
    else:
        answer = len(hash_nums)
    
    return int(answer)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([3,1,2,3])) 
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

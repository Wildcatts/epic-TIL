def solution(phone_book):  # 효율성 테스트 실패
    phone_book.sort(reverse=True)
    print(phone_book)

    for i in range(len(phone_book) - 1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            
    return True

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        if phone_book[i+1].startswith(phone_book[i]) : return False
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123","456","789"])) # True

# 정렬을 했기 때문에 앞 뒤 다 비교할 필요는 없다
# 정렬 후, i+1번째가 i번째로 시작하는지만 확인하면 된다(비슷한 숫자를 찾기 때문에 정렬하면 근처에 있을 확률이 높아진다)

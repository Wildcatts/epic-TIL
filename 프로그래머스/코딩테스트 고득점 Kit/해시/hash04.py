'''
dictionary에서 key와 value를 모두 접근하는 방법은 {}에 item()을 선언해주면 된다.
dict = {}
dict{'key1'} = 1
dict{'key2'} = 2

for key, value in dict.item():
  print(key, value)  # key1 1  key2 2

해쉬로 같은 key에 대한 값을 저장하는 방법은 아래 방법으로 정리하면 좋다
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes_dict = {}
for cloth in clothes:
  if cloth[1] in clothes_dict:
    clothes_dict[cloth[1]] += 1
  else:
    clothes_dict[cloth[1]] = 1
'''

def solution(clothes):
    '''
    1. 의상의 종류가 같은 것끼리 묶어준다.
    2. head : a, b, c
    3. eye : d, e
    4. top : f, g
    5. bottom : h
    6. 각 원소의 갯수를 더한다
    7. 3 * 2 * 2 * 1 
    8. 모두 안입는 경우는 없다
    9. 6 + 7 을 해주면 된다
    10. 21

    '''
    answer = 1
    clothes_dict = {}
    for c in clothes:
        if c[1] in clothes_dict:
            clothes_dict[c[1]] += 1
        else:
            clothes_dict[c[1]] = 1
    
    print(clothes_dict)

    for key in clothes_dict:
        answer *= clothes_dict[key] + 1

    return answer - 1

def make_solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    
    print(clothes_dict)

    answer = 0

    for key, value in clothes_dict.items():
        print(key, value)

    return 0

print(make_solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

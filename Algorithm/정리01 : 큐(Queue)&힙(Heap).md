# 📌 알고리즘 정리 01: 큐(Queue) & 힙(Heap)

## 🧠 큐(Queue)란?

큐는 **선입선출(FIFO: First-In-First-Out)** 자료구조입니다.  
먼저 들어온 데이터가 먼저 나가는 구조로, 현실에서는 줄 서기와 유사합니다.

### ✅ 기본 연산
- `enqueue`: 데이터를 큐에 넣음
- `dequeue`: 데이터를 큐에서 꺼냄
- `peek`: 가장 앞에 있는 데이터를 확인 (제거하지 않음)

### 📦 Python 구현 예시
```python
from collections import deque

q = deque()
q.append(1)     # enqueue
q.append(2)
q.popleft()     # dequeue → 1
```

---

## 🤖 실무 관점: 큐는 어디에 쓰일까?

### 💡 로봇 제어에서의 응용
- **명령 큐**: 로봇이 처리할 명령을 순차적으로 실행
  - 예: Move → Pick → Place → Stop
- **이벤트 처리 시스템**: 센서 이벤트, 사용자 요청 등을 이벤트 큐로 처리
- **멀티스레드 데이터 공유**: 생산자-소비자 패턴 (Producer–Consumer)

```python
# 명령 큐 예시
from queue import Queue
command_queue = Queue()

# 명령 추가
command_queue.put("move_home")
command_queue.put("pick_object")

# 실행
while not command_queue.empty():
    cmd = command_queue.get()
    robot.execute(cmd)
```

---

## 🧠 힙(Heap)이란?

힙은 **우선순위 큐(Priority Queue)**를 구현하는 자료구조입니다.  
항상 가장 작은(또는 큰) 값이 루트에 위치하며, 삽입/삭제 시 자동으로 정렬됩니다.

- 최소 힙: 값이 작은 요소가 루트
- 최대 힙: 값이 큰 요소가 루트

### ✅ Python 구현 예시
```python
import heapq

# 최소 힙
h = []
heapq.heappush(h, 4)
heapq.heappush(h, 2)
heapq.heappush(h, 7)
print(heapq.heappop(h))  # 출력: 2 (최소값)
```

### ❗ 최대 힙을 만들고 싶을 때
음수로 변환하여 사용 (파이썬 기본은 최소 힙)
```python
heapq.heappush(h, -3)   # 최대 힙처럼 사용
val = -heapq.heappop(h) # 다시 양수로 변환
```

---

## 🤖 실무 관점: 힙은 어디에 쓰일까?

### 💡 로봇 시스템에서의 응용
- **우선순위 작업 처리**
  - 예: 배터리가 부족하면 충전이 더 높은 우선순위로 실행됨
- **경로 탐색 알고리즘**
  - 예: A* 탐색, Dijkstra 알고리즘 → 힙으로 최단거리 노드 추출
- **실시간 리소스 스케줄링**
  - 가장 먼저 끝나는 작업, 혹은 가장 중요한 작업부터 수행

---

## 🔧 큐 vs 힙 차이점 정리

| 항목         | 큐 (Queue)               | 힙 (Heap)                       |
|--------------|--------------------------|----------------------------------|
| 구조         | 선입선출 (FIFO)          | 우선순위 기반 추출               |
| 사용 목적    | 순서대로 처리             | 우선순위가 높은 항목 먼저 처리    |
| 사용 예시    | 명령 처리, 이벤트 큐     | 작업 스케줄링, 최단경로, AI 우선순위 |

---

## 📝 추천 문제

| 문제명 | 난이도 | 개념 | 링크 |
|--------|--------|------|------|
| 기능개발 (프로그래머스) | 🟢 Level 2 | 큐 | [문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42586) |
| 프린터 (프로그래머스) | 🟢 Level 2 | 큐, 우선순위 큐 | [문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42587) |
| 디스크 컨트롤러 (프로그래머스) | 🟡 Level 3 | 힙, 스케줄링 | [문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/42627) |
| 백준 11279 최대 힙 | 🟢 실버 2 | 최대 힙 | [문제 바로가기](https://www.acmicpc.net/problem/11279) |

---

## ✅ 요약
- **큐**는 순서가 중요할 때, **힙**은 우선순위가 중요할 때 사용
- 로봇 시스템에서 명령 제어, 센서 이벤트 처리, 작업 스케줄링 등에 핵심적으로 활용됨
- 단순한 알고리즘이지만, 시스템의 안정성과 효율성을 좌우할 수 있는 구조

# 📌 알고리즘 정리 03: BFS (Breadth-First Search, 너비 우선 탐색)

## ✅ 개념

**BFS (Breadth-First Search)**는 그래프 또는 트리에서 **가까운 노드부터 탐색**하는 알고리즘입니다.  
탐색 시 **큐(Queue)** 자료구조를 사용하여, 현재 노드에서 인접한 노드를 모두 먼저 방문한 뒤 다음 노드로 넘어갑니다.

- DFS는 한 갈래로 깊게 파고드는 반면,
- **BFS는 동일 레벨의 노드를 모두 탐색하고 나서 다음 레벨로 이동**합니다.

📌 BFS는 **최단 거리**를 구하는 데 적합합니다. (예: 미로 탈출, 최단 경로 문제)

---

## 🔄 동작 방식

1. 시작 노드를 큐에 삽입하고 방문 표시
2. 큐가 빌 때까지 다음을 반복:
   - 큐에서 노드를 꺼냄
   - 해당 노드의 인접 노드 중 방문하지 않은 노드를 큐에 삽입하고 방문 표시

---

## 📦 자료구조

- 큐 (`collections.deque` 사용)
- 방문 여부 체크용 리스트 (`visited`)

---

## 🧠 알고리즘 흐름 (의사 코드)

```pseudo
BFS(Graph, start):
    create empty queue Q
    mark start as visited
    Q.enqueue(start)

    while Q is not empty:
        node = Q.dequeue()
        process(node)

        for neighbor in Graph[node]:
            if neighbor is not visited:
                mark neighbor as visited
                Q.enqueue(neighbor)
```

---

## 💻 파이썬 구현 예제

### 예제 1: 그래프 탐색

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
```

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 출력: A B C D E F
```

### 예제 2: 2차원 미로에서의 최단 거리 탐색

```python
from collections import deque

def bfs_maze(maze, start, goal):
    n, m = len(maze), len(maze[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(start[0], start[1], 0)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == goal:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1  # 도달 불가
```

---

## ⏱️ 시간 복잡도

- **그래프가 V개의 정점과 E개의 간선을 가질 때**  
  ➤ `O(V + E)`

- 정점마다 한 번 방문, 간선마다 한 번씩 검사하기 때문

---

## 🔁 DFS vs BFS

| 항목 | DFS | BFS |
|------|-----|-----|
| 탐색 방식 | 깊이 우선 | 너비 우선 |
| 자료구조 | 스택 (재귀) | 큐 |
| 최단 경로 | 보장 X | 보장 O |
| 메모리 사용 | 보통 작음 | 많음 (너비에 비례) |
| 사용 예 | 백트래킹, 퍼즐 풀이 | 최단 거리, 라벨링 |

---

## 💡 로봇 제어에서의 응용

### 1. **장애물 회피 및 경로 탐색**
- 로봇이 주어진 격자 맵에서 목적지까지 이동해야 할 때, **BFS는 가장 짧은 거리**를 보장
- ex) 물류 로봇이 물건을 빠르게 찾고 돌아오는 경로 탐색

### 2. **로봇의 상태 전이 모델링**
- 각 상태(State)를 노드로 보고, 가능한 전이를 간선으로 모델링하여 BFS로 상태 전이 경로 탐색
- ex) 초기 → 중간 동작 → 최종 동작 순서 탐색

### 3. **큐 기반 이벤트 처리 시스템**
- 로봇에 들어오는 센서 신호나 명령을 **BFS 순서로 처리** (선입선출 방식)
- ex) 로봇이 여러 작업을 순차적으로 처리해야 할 때 안정적 처리 순서 보장

### 4. **멀티 타겟 위치 탐색**
- 하나의 로봇이 여러 개의 타겟(예: 피킹 포인트)을 순차적으로 탐색할 경우 BFS는 탐색 효율을 높임

---

## 📚 BFS 관련 문제 추천

1. [미로 탐색](https://www.acmicpc.net/problem/2178) (백준 2178)
2. [숨바꼭질](https://www.acmicpc.net/problem/1697) (백준 1697)
3. [토마토 익기 문제](https://www.acmicpc.net/problem/7576) (백준 7576)
4. [단지 번호 붙이기](https://www.acmicpc.net/problem/2667) (백준 2667)

---

## 🧾 정리

- BFS는 **큐 기반의 탐색 알고리즘**으로 **최단 거리 문제에 매우 유용**
- DFS보다 **메모리 사용량은 높지만**, **동일 레벨을 먼저 탐색**하기 때문에 **경로 최적화에 유리**
- 로봇 시스템에선 **경로 탐색, 이벤트 처리, 상태 전이 모델링** 등에서 효과적

---

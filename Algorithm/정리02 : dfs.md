
# 📌 알고리즘 정리 02: DFS (Depth-First Search, 깊이 우선 탐색)

---

## 🔍 DFS란?

DFS(Depth-First Search)는 **그래프나 트리와 같은 자료구조에서 하나의 경로를 끝까지 탐색한 다음, 되돌아가며 다른 경로를 탐색하는 방식**의 알고리즘입니다.

즉, 어떤 노드에서 시작하여 최대한 깊숙이 들어간 뒤, 더 이상 갈 수 없으면 다시 돌아와서 다른 경로를 탐색합니다. 이는 **백트래킹(Backtracking)**과 밀접한 관련이 있으며, **재귀(Recursion)** 또는 **스택(Stack)**을 사용하여 구현할 수 있습니다.

---

## 🧠 기본 개념

- **탐색 순서**: 시작 노드 → 자식 노드 → 자식의 자식 노드 ... → 더 이상 탐색 불가 → 이전 노드로 되돌아감
- **종료 조건**: 더 이상 방문하지 않은 인접 노드가 없을 때까지
- **방문 처리**: 이미 방문한 노드는 재방문하지 않도록 체크해야 무한 루프 방지 가능

---

## 🧮 DFS 동작 흐름 (절차적 설명)

1. 현재 노드를 방문 처리하고 출력하거나 기록한다.
2. 현재 노드와 연결된 다른 노드를 차례대로 확인한다.
3. 연결된 노드 중 방문하지 않은 노드가 있으면 그 노드를 재귀적으로 방문한다.
4. 연결된 노드가 더 이상 없을 경우, 이전 노드로 되돌아가서 다음 경로를 탐색한다.

---

## 🧪 DFS 구현 방식

### ✔️ 방법 1. 재귀 기반 DFS

```python
def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 예제 그래프
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}
visited = [False] * 6
dfs(graph, 1, visited)
```

📌 출력: `1 2 4 5 3`

---

### ✔️ 방법 2. 스택 기반 반복문 DFS

```python
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))
```

---

## 🔧 DFS의 시간 및 공간 복잡도

- **시간 복잡도**: O(V + E) (V는 정점 수, E는 간선 수)
- **공간 복잡도**: O(V) (방문 배열, 재귀 호출 스택 등)

---

## 🤖 실무 적용 사례: 로봇 소프트웨어 개발에서의 DFS

### 1. 동작 시퀀스 트리 실행
복잡한 작업 순서를 트리 형태로 모델링하고 DFS로 순회하며 로봇이 각 동작을 수행

### 2. 비전 기반 객체 연결 탐색
이미지에서 연속된 동일 색상/형태를 탐색하여 객체를 식별 (Flood Fill 방식)

### 3. 지도 영역 탐색
미탐색 지역을 DFS로 탐색하여 맵을 확장하거나 장애물 영역을 파악

### 4. 백트래킹 문제 해결
조건을 만족하는 해를 탐색할 때 DFS 기반으로 모든 경로를 시도하며 해를 찾음

---

## 🧩 DFS vs BFS 비교

| 항목 | DFS (Depth-First) | BFS (Breadth-First) |
|------|-------------------|---------------------|
| 탐색 구조 | 깊이 우선 | 너비 우선 |
| 자료구조 | 재귀 or 스택 | 큐 |
| 구현 난이도 | 간결, 재귀 활용 | 큐 사용, 메모리 소비 큼 |
| 활용 사례 | 백트래킹, 퍼즐, 영역 탐색 | 최단 경로 탐색, 네트워크 탐색 |

---

## 📝 추천 문제

| 플랫폼 | 문제명 | 링크 |
|--------|--------|------|
| 백준 | 2606 바이러스 | https://www.acmicpc.net/problem/2606 |
| 백준 | 11724 연결 요소의 개수 | https://www.acmicpc.net/problem/11724 |
| 프로그래머스 | 타겟 넘버 | https://school.programmers.co.kr/learn/courses/30/lessons/43165 |
| 백준 | 2667 단지번호붙이기 | https://www.acmicpc.net/problem/2667 |
| 백준 | 1012 유기농 배추 | https://www.acmicpc.net/problem/1012 |

---

## ✅ 요약

- DFS는 재귀적으로 혹은 스택을 이용해 깊이 우선 탐색을 수행
- 로봇 소프트웨어에서는 상태 순서 실행, 비전 영역 탐색, 조건 기반 조합 탐색 등에 매우 유용
- BFS와 비교하여 경로의 깊이나 조합 탐색이 중요한 경우 DFS가 더 적합


# 목차
1. Array
2. List
-------------

# 1. Array 개념 및 활용

## 1. Array(배열) 개념
배열(Array)은 동일한 데이터 타입을 가지는 요소(Element)들의 집합으로, 연속된 메모리 공간에 저장되는 자료구조이다. 배열을 사용하면 여러 개의 데이터를 효율적으로 관리할 수 있으며, 인덱스를 사용하여 원하는 요소에 빠르게 접근할 수 있다.

## 2. 배열의 선언 및 활용 방법

### 2.1 배열 선언 방법
배열을 선언하는 방법은 사용하는 프로그래밍 언어에 따라 다를 수 있다. 아래는 다양한 언어에서 배열을 선언하는 방법이다.

#### C언어
```c
int arr[5]; // 정수형 배열 선언 (크기 5)
```

#### Java
```java
int[] arr = new int[5]; // 정수형 배열 선언
```

#### Python
```python
arr = [0] * 5 # 정수형 배열 선언 (크기 5)
```

### 2.2 배열 활용 방법
배열 요소 접근 및 수정 예제:

#### C언어
```c
arr[0] = 10; // 첫 번째 요소에 값 저장
printf("%d", arr[0]); // 출력: 10
```

#### Java
```java
arr[0] = 10;
System.out.println(arr[0]); // 출력: 10
```

#### Python
```python
arr[0] = 10
print(arr[0]) # 출력: 10
```

## 3. 다차원 배열의 선언과 활용

### 3.1 다차원 배열 선언
2차원 이상의 배열을 선언하여 행과 열 구조의 데이터를 저장할 수 있다.

#### C언어 (2차원 배열)
```c
int matrix[3][3];
```

#### Java (2차원 배열)
```java
int[][] matrix = new int[3][3];
```

#### Python (2차원 리스트)
```python
matrix = [[0] * 3 for _ in range(3)]
```

### 3.2 다차원 배열 활용 예제

#### C언어
```c
matrix[0][0] = 1;
printf("%d", matrix[0][0]); // 출력: 1
```

#### Java
```java
matrix[0][0] = 1;
System.out.println(matrix[0][0]); // 출력: 1
```

#### Python
```python
matrix[0][0] = 1
print(matrix[0][0]) # 출력: 1
```

## 4. Array의 시간 복잡도와 공간 복잡도

### 4.1 시간 복잡도
| 연산 | 시간 복잡도 |
|------|----------|
| 접근 (Access) | O(1) |
| 검색 (Search) | O(n) |
| 삽입 (Insert) | O(n) |
| 삭제 (Delete) | O(n) |

배열의 요소 접근은 인덱스를 사용하여 O(1) 시간 복잡도를 가지지만, 특정 요소를 찾거나 삽입, 삭제하는 경우에는 O(n)의 시간이 필요할 수 있다.

### 4.2 공간 복잡도
배열은 선언된 크기만큼 메모리를 할당받으며, 공간 복잡도는 O(n)이다. 다차원 배열의 경우 O(n*m) 등의 공간이 필요하다.

# 2. List 개념 및 활용

## 1. List 개념과 종류
List(리스트)는 순서가 있는 데이터의 모음으로, 동적인 크기를 가지며 다양한 자료형을 저장할 수 있는 자료구조이다.

### 1.1 List의 종류
- **배열 리스트(Array List)**: 배열을 기반으로 구현되며, 인덱스를 통한 빠른 접근이 가능하지만 삽입과 삭제가 비용이 클 수 있다.
- **연결 리스트(Linked List)**: 노드(Node)들이 포인터를 통해 연결된 형태로, 삽입과 삭제가 빠르지만 인덱스 접근이 느리다.
- **이중 연결 리스트(Doubly Linked List)**: 각 노드가 이전 노드와 다음 노드를 가리키는 포인터를 가지는 구조로, 양방향 탐색이 가능하다.
- **원형 연결 리스트(Circular Linked List)**: 마지막 노드가 첫 번째 노드를 가리키는 형태로, 원형 구조를 가진다.

## 2. List의 기본 연산과 시간 복잡도

| 연산 | 배열 리스트 | 단일 연결 리스트 | 이중 연결 리스트 |
|------|------------|----------------|----------------|
| 접근 (Access) | O(1) | O(n) | O(n) |
| 검색 (Search) | O(n) | O(n) | O(n) |
| 삽입 (Insert) | O(n) | O(1) (앞/뒤), O(n) (중간) | O(1) (앞/뒤), O(n) (중간) |
| 삭제 (Delete) | O(n) | O(1) (앞/뒤), O(n) (중간) | O(1) (앞/뒤), O(n) (중간) |

## 3. List의 활용 방법과 예제

### 3.1 List 선언 및 활용 예제

#### Python (리스트)
```python
lst = [1, 2, 3, 4, 5] # 리스트 선언
lst.append(6) # 삽입
lst.remove(3) # 삭제
print(lst.index(4)) # 검색
```

#### Java (ArrayList)
```java
import java.util.ArrayList;
ArrayList<Integer> list = new ArrayList<>();
list.add(1);
list.add(2);
list.remove(Integer.valueOf(1));
System.out.println(list.indexOf(2));
```

#### C언어 (연결 리스트)
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void insert(struct Node** head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *head;
    *head = newNode;
}
```

리스트는 데이터의 크기가 동적으로 변할 수 있으며, 다양한 알고리즘 및 응용에서 활용된다. 배열 리스트는 빠른 접근이 필요한 경우 유용하며, 연결 리스트는 빈번한 삽입과 삭제가 필요한 경우 적합하다.


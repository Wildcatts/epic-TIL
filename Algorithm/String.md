## 목차
 1. String
 2. 패턴 매칭(Naive)
----------------------------------------------------------------------
## 1. String
- String의 개념과 문자열 처리 방법(문자열 분리, 문자열 합치기, 문자열 비교 등)
- 문자열 검색과 치환(strstr(), strcmp(), strtok() 등)

## String의 개념과 문자열 처리 방법

- *문자열(String)**은 문자들의 연속된 집합으로, 프로그래밍에서 매우 중요한 데이터 타입 중 하나입니다. 문자열은 주로 **문자(char)** 배열로 표현되며,
- 다양한 언어에서 문자열을 다루기 위한 여러 함수와 메서드가 제공됩니다. 문자열은 불변(immutable)인 경우가 많아, 한 번 생성된 문자열은 직접 수정할 수 없으며, 수정하려면 새로운 문자열을 생성해야 합니다.

### **문자열 처리 방법**

### **1. 문자열 분리 (Splitting)**

문자열을 특정 구분자를 기준으로 나누는 작업을 **문자열 분리**라고 합니다. 예를 들어, 쉼표로 구분된 CSV 데이터를 처리할 때 문자열 분리가 유용합니다.

- **C 언어**에서는 `strtok()` 함수를 사용하여 문자열을 분리합니다.
    
    ```c
    #include <stdio.h>
    #include <string.h>
    
    int main() {
        char str[] = "apple,banana,cherry";
        char *token = strtok(str, ",");
    
        while (token != NULL) {
            printf("%s\\n", token);
            token = strtok(NULL, ",");
        }
        return 0;
    }
    
    ```
    
    출력:
    
    ```
    apple
    banana
    cherry
    
    ```
    

### **2. 문자열 합치기 (Concatenation)**

여러 개의 문자열을 하나로 합치는 작업을 **문자열 합치기**라고 합니다.

- **C 언어**에서는 `strcat()` 함수를 사용하여 두 문자열을 이어 붙일 수 있습니다.
    
    ```c
    #include <stdio.h>
    #include <string.h>
    
    int main() {
        char str1[20] = "Hello";
        char str2[] = " World";
    
        strcat(str1, str2);
        printf("%s\\n", str1); // 출력: Hello World
    
        return 0;
    }
    
    ```
    

### **3. 문자열 비교 (Comparison)**

두 문자열이 같은지 비교하는 작업입니다. C 언어에서는 `strcmp()` 함수를 사용하여 두 문자열을 사전식으로 비교할 수 있습니다.

- `strcmp()`는 두 문자열이 같으면 `0`, 첫 번째 문자열이 더 크면 양수, 두 번째가 더 크면 음수를 반환합니다.
    
    ```c
    #include <stdio.h>
    #include <string.h>
    
    int main() {
        char str1[] = "apple";
        char str2[] = "banana";
    
        int result = strcmp(str1, str2);
    
        if (result == 0) {
            printf("The strings are equal.\\n");
        } else if (result > 0) {
            printf("str1 is greater than str2.\\n");
        } else {
            printf("str1 is less than str2.\\n");
        }
    
        return 0;
    }
    
    ```
    

## 문자열 검색과 치환

문자열 내에서 특정 패턴이나 문자를 검색하거나 다른 문자로 바꾸는 작업은 매우 흔한 작업입니다. C 언어에서는 이러한 작업을 위한 여러 함수들이 제공됩니다.

### **1. strstr() - 문자열 검색**

`strstr()` 함수는 특정 **부분 문자열(substring)**이 주어진 문자열 내에 존재하는지 확인하고, 그 위치를 반환합니다. 찾는 부분 문자열이 없으면 `NULL`을 반환합니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello World";
    char *result = strstr(str, "World");

    if (result != NULL) {
        printf("Found: %s\\n", result); // 출력: Found: World
    } else {
        printf("Not found\\n");
    }

    return 0;
}

```

### **2. strcmp() - 문자열 비교**

위에서 설명한 것처럼, `strcmp()` 함수는 두 문자열을 비교하는 함수입니다. 이 함수는 문자의 ASCII 값을 기준으로 사전식 비교를 수행합니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "apple";

    if (strcmp(str1, str2) == 0) {
        printf("Strings are equal\\n"); // 출력: Strings are equal
    } else {
        printf("Strings are not equal\\n");
    }

    return 0;
}

```

### **3. strtok() - 문자열 분리**

`strtok()` 함수는 구분자를 기준으로 문자열을 잘라서 토큰(token)을 추출하는 함수입니다. 첫 번째 호출에서는 원본 문자열과 구분자를 인자로 전달하고, 이후 호출에서는 `NULL`과 구분자를 전달하여 다음 토큰을 가져옵니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "apple/banana/cherry";
    char *token = strtok(str, "/");

    while (token != NULL) {
        printf("%s\\n", token); // 각 과일 이름 출력
        token = strtok(NULL, "/");
    }

    return 0;
}

```

### **4. strcpy() - 문자열 복사**

`strcpy()` 함수는 한 문자열을 다른 배열에 복사하는 데 사용됩니다. 이때 복사되는 배열의 크기가 충분히 커야 메모리 오류가 발생하지 않습니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello";
    char dest[10];

    strcpy(dest, src);

    printf("%s\\n", dest); // 출력: Hello

    return 0;
}

```

### **5. strncpy() - 안전한 문자열 복사**

`strncpy()`는 `strcpy()`와 유사하지만, 복사할 최대 길이를 명시적으로 지정할 수 있어 버퍼 오버플로우를 방지할 수 있습니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello";
    char dest[10];

    strncpy(dest, src, sizeof(dest) - 1);

    dest[sizeof(dest) - 1] = '\\0'; // 마지막에 null 문자 추가

    printf("%s\\n", dest); // 출력: Hello

    return 0;
}

```

## 결론

문자열은 프로그래밍에서 매우 중요한 데이터 타입이며 다양한 방식으로 처리할 수 있습니다. C 언어에서는 `strcpy()`, `strcmp()`, `strtok()` 등의 함수를 통해 복사, 
비교 및 분리 작업을 수행할 수 있으며, 이러한 기본적인 기능들은 대부분의 프로그래밍 언어에서도 비슷한 방식으로 제공됩니다.

- 패턴 매칭의 개념과 Naive 알고리즘
- Naive 알고리즘의 시간 복잡도와 한계점
- 패턴 매칭 알고리즘의 개선(Rabin-Karp, KMP 등)

## 2. 패턴 매칭의 개념과 Naive 알고리즘

- *패턴 매칭(Pattern Matching)**은 문자열에서 특정 **패턴**을 찾는 문제를 의미합니다. 예를 들어, 긴 텍스트에서 특정 단어나 문구가 등장하는 위치를 찾는 것이 패턴 매칭의 대표적인 예입니다.
- 패턴 매칭 알고리즘은 주어진 텍스트 내에서 원하는 패턴을 효율적으로 찾는 방법을 제공합니다.

### **Naive 알고리즘**

**Naive 알고리즘**은 패턴 매칭 문제를 해결하는 가장 기본적이고 직관적인 방법입니다. 이 알고리즘은 텍스트의 각 위치에서 패턴과 일치하는지 하나씩 비교하며, 
만약 일치하는 부분이 있으면 그 위치를 출력합니다.

### **Naive 알고리즘의 동작 방식**

1. 텍스트의 첫 번째 문자부터 시작해서, 패턴의 첫 번째 문자와 비교합니다.
2. 일치하면 다음 문자로 넘어가고, 일치하지 않으면 다음 텍스트 위치로 이동하여 다시 비교를 시작합니다.
3. 텍스트 내에서 패턴이 발견되면 그 위치를 기록하고, 이후에도 계속해서 탐색을 진행합니다.

### **Naive 알고리즘의 구현 예시 (Python)**

```python
def naive_algorithm(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i}")

# 테스트
text = "AABAACAADAABAAABAA"
pattern = "AABA"
naive_algorithm(text, pattern)

```

출력:

```
Pattern found at index 0
Pattern found at index 9
Pattern found at index 13

```

## Naive 알고리즘의 시간 복잡도와 한계점

### **시간 복잡도**

- **최선의 경우 (Best Case)**: 패턴의 첫 번째 문자가 텍스트에 없는 경우, 한 번의 탐색으로 끝나므로 시간 복잡도는 $$O(n)$$입니다.
- **최악의 경우 (Worst Case)**: 모든 문자가 일치하거나 거의 일치하는 경우에는 $$O(m \times n)$$ 시간이 소요됩니다. 여기서 $$n$$은 텍스트의 길이, $$m$$은 패턴의 길이입니다.

### **최악의 경우 예시**

텍스트가 `"AAAAAAAAAA"`이고, 패턴이 `"AAAAA"`인 경우처럼 모든 문자가 일치할 때, Naive 알고리즘은 모든 위치에서 패턴을 비교해야 하므로 최악의 성능을 보입니다.

### **한계점**

- **비효율성**: Naive 알고리즘은 단순히 모든 위치에서 하나씩 비교하기 때문에 큰 텍스트와 긴 패턴에서는 매우 비효율적입니다.
- **중복된 계산**: 이미 확인한 정보를 활용하지 않고 매번 처음부터 다시 비교하기 때문에 불필요한 계산이 많습니다.

## 패턴 매칭 알고리즘의 개선

Naive 알고리즘의 비효율성을 개선하기 위해 다양한 고급 패턴 매칭 알고리즘이 개발되었습니다. 대표적인 두 가지는 **Rabin-Karp**와 **KMP(Knuth-Morris-Pratt)** 알고리즘입니다.

### **1. Rabin-Karp 알고리즘**

**Rabin-Karp 알고리즘**은 Naive 알고리즘과 유사하게 텍스트를 한 문자씩 이동하며 패턴을 찾지만, 각 부분 문자열을 직접 비교하는 대신 **해시 함수**를 사용하여 빠르게 비교합니다.

### **동작 방식**

1. 텍스트와 패턴에 대해 해시 값을 계산합니다.
2. 텍스트 내에서 패턴과 같은 길이의 부분 문자열들의 해시 값을 계산하고, 미리 계산된 패턴의 해시 값과 비교합니다.
3. 해시 값이 같으면 실제로 문자열을 비교하여 일치 여부를 확인합니다.

### **시간 복잡도**

- 평균적으로 $$O(n)$$, 최악의 경우 $$O(m \times n)$$입니다. 해시 충돌이 발생할 때 최악의 경우가 발생할 수 있습니다.

### **2. KMP(Knuth-Morris-Pratt) 알고리즘**

KMP 알고리즘은 Naive 방식에서 발생하는 중복된 비교를 피하기 위해, **패턴 자체에 대한 전처리 과정**을 통해 효율성을 높입니다. 
KMP는 실패한 부분 문자열에 대해 불필요한 재탐색을 하지 않도록 설계되었습니다.

### **동작 방식**

1. 먼저 패턴에 대한 **부분 일치 테이블(LPS: Longest Prefix Suffix)**을 생성합니다. 이 테이블은 각 위치까지의 접두사와 접미사가 얼마나 일치하는지를 기록합니다.
2. 탐색 중에 불일치가 발생하면, LPS 테이블을 참고하여 이미 확인한 부분을 재탐색하지 않고 건너뜁니다.

### **시간 복잡도**

- KMP는 전처리에 $$O(m)$$, 검색에 $$O(n)$$ 시간이 소요되므로 전체 시간 복잡도는 $$O(n + m)$$입니다.

### **KMP 구현 예시**

```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    i = 0 # text index
    j = 0 # pattern index

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)

```

출력:

```
Pattern found at index 10

```

## 결론

- Naive 알고리즘은 간단하고 구현하기 쉽지만 시간 복잡도가 $$O(m \times n)$$으로 비효율적일 수 있습니다.
- Rabin-Karp와 KMP 같은 고급 알고리즘들은 이러한 비효율성을 개선하여 더 빠른 검색 성능을 제공합니다.
- 특히 KMP는 전처리를 통해 불필요한 재탐색을 방지함으로써 시간 복잡도를 $$O(n + m)$$으로 줄일 수 있습니다.

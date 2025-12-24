#include <stdio.h>
#include <stdlib.h>

#define MAX 100001

typedef struct Node {
    int to;
    struct Node* next;
} Node;

Node* adj[MAX];        // 인접 리스트
int parent[MAX];       // 부모 저장
int queue[MAX];        // BFS 큐

void addEdge(int u, int v) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->to = v;
    node->next = adj[u];
    adj[u] = node;
}

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        adj[i] = NULL;
        parent[i] = 0;
    }

    for (int i = 0; i < N - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        addEdge(a, b);
        addEdge(b, a);
    }

    // BFS 시작
    int front = 0, rear = 0;
    queue[rear++] = 1;
    parent[1] = -1;

    while (front < rear) {
        int cur = queue[front++];

        for (Node* p = adj[cur]; p != NULL; p = p->next) {
            int next = p->to;

            if (parent[next] == 0) {  // 방문 안 한 노드
                parent[next] = cur;
                queue[rear++] = next;
            }
        }
    }

    // 출력 (2번 노드부터)
    for (int i = 2; i <= N; i++) {
        printf("%d\n", parent[i]);
    }

    return 0;
}
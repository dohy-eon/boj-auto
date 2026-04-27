#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    char value;
    struct Node* left;
    struct Node* right;
} Node;

// 노드 생성 함수
Node* createNode(char value) {
    if (value == '.') return NULL; // '.'이면 NULL 반환 (자식이 없는 경우)
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// 전위 순회
void preorder(Node* node) {
    if (node == NULL) return;
    printf("%c", node->value);
    preorder(node->left);
    preorder(node->right);
}

// 중위 순회
void inorder(Node* node) {
    if (node == NULL) return;
    inorder(node->left);
    printf("%c", node->value);
    inorder(node->right);
}

// 후위 순회
void postorder(Node* node) {
    if (node == NULL) return;
    postorder(node->left);
    postorder(node->right);
    printf("%c", node->value);
}

// 트리에서 특정 노드 찾기
Node* findNode(Node* nodes[], char value) {
    if (value == '.') return NULL;
    return nodes[value - 'A']; // A는 0번째 인덱스
}

int main() {
    int N;
    scanf("%d", &N);
    
    Node* nodes[26] = { NULL }; // 최대 알파벳 개수(26개)
    
    for (int i = 0; i < N; i++) {
        char parent, left, right;
        scanf(" %c %c %c", &parent, &left, &right);
        
        if (nodes[parent - 'A'] == NULL) {
            nodes[parent - 'A'] = createNode(parent);
        }
        
        // 부모 노드의 자식 설정
        if (left != '.') {
            nodes[left - 'A'] = createNode(left); // 왼쪽 자식이 없으면 새로 생성
            nodes[parent - 'A']->left = nodes[left - 'A'];
        }
        
        if (right != '.') {
            nodes[right - 'A'] = createNode(right); // 오른쪽 자식이 없으면 새로 생성
            nodes[parent - 'A']->right = nodes[right - 'A'];
        }
    }
    
    Node* root = nodes[0]; // A가 루트 노드라고 가정
    
    // 순회 결과 출력
    preorder(root);
    printf("\n");
    inorder(root);
    printf("\n");
    postorder(root);
    printf("\n");
    
    // 메모리 해제
    for (int i = 0; i < 26; i++) {
        if (nodes[i] != NULL) free(nodes[i]);
    }
    
    return 0;
}
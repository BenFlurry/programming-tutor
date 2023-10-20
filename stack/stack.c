//
//  stack.c
//  testc
//
//  Created by Benjamin Alexander on 02/09/2023.
//

#include <stdio.h>
#include <stdlib.h>


typedef struct _node {
    int val;
    struct _node* next;
} Node;

typedef struct _stack {
    struct _node* head;
    int len;
} Stack;

Stack* create_stack(void) {
    Stack* s = malloc(sizeof(Stack));
    Node* n = malloc(sizeof(Node));
    s->head = n;
    s->len = 0;
    return s;
}

Stack* add_node(Stack* s, int v) {
    Node* new_node = malloc(sizeof(Node));
    new_node->val = v;
    
    if (s->len == 0) {
        new_node->next = NULL;
        s->head = new_node;
        s->len++;
        return s;
        
    }
    
    new_node->next = s->head;
    s->head = new_node;
    s->len++;
    return s;
}

void print_stack(Stack* s) {
    if (s->len == 0) {
        printf("empty stack\n");
        return;
    }
    
    Node* n = s->head;
    for (int i = 0; i < s->len; i++) {
        printf("%i, ", n->val);
        n = n->next;
    }
    printf("\n");
}

void free_stack(Stack* s) {
    if (s->len == 0) {
        free(s);
        return;
    }
    
    Node* n = s->head;
    for (int i = 1; i < s->len; i++) {
        Node* tmp = n->next;
        free(n);
        n = tmp;
    }
    free(s);
}

int pop_stack(Stack* s) {
    if (s->len == 0) {
        printf("stack empty\n");
        return 0;
    }
    Node* next = s->head->next;
    int val = s->head->val;
    free(s->head);
    s->head = next;
    s->len--;
    return val;
    
}

int peek_stack(Stack* s) {
    if (s->len == 0) {
        printf("stack empty\n");
        return 0;
    }
    return s->head->val;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    Stack* s = create_stack();
    for (int i = 0; i < 3; i++) {
        add_node(s, i);
    }
    print_stack(s);
    add_node(s, 6);
    print_stack(s);
    pop_stack(s);
    print_stack(s);
    free_stack(s);
    return 0;
    
}




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
} node;

typedef struct _stack {
    struct _node* head;
    int len;
} stack;

stack* create_stack(void) {
    stack* s = malloc(sizeof(stack));
    node* n = malloc(sizeof(node));
    s->head = n;
    s->len = 0;
    return s;
}

stack* add_node(stack* s, int v) {
    node* new_node = malloc(sizeof(node));
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

void print_stack(stack* s) {
    if (s->len == 0) {
        printf("empty stack\n");
        return;
    }
    
    node* n = s->head;
    for (int i = 0; i < s->len; i++) {
        printf("%i, ", n->val);
        n = n->next;
    }
    printf("\n");
}

void free_stack(stack* s) {
    if (s->len == 0) {
        free(s);
        return;
    }
    
    node* n = s->head;
    for (int i = 1; i < s->len; i++) {
        node* tmp = n->next;
        free(n);
        n = tmp;
    }
    free(s);
}

int pop_stack(stack* s) {
    if (s->len == 0) {
        printf("stack empty\n");
        return 0;
    }
    node* next = s->head->next;
    int val = s->head->val;
    free(s->head);
    s->head = next;
    s->len--;
    return val;
    
}

int peek_stack(stack* s) {
    if (s->len == 0) {
        printf("stack empty\n");
        return 0;
    }
    return s->head->val;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    stack* s = create_stack();
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




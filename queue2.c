#include <stdlib.h>

typedef struct _queue {
    struct _node* head;
    struct _node* tail;
    int len;
} queue;

typedef struct _node {
    struct _node* next;
    struct _node* prev;
    int val;
} node;

queue* create_queue() {
    queue* q = malloc(sizeof(queue));
    q->head = NULL;
    q->tail = NULL;
    q->len = 0;
    return q;
}

queue* enqueue(queue* q, int val) {
    node* new_node = malloc(sizeof(node));
    new_node->prev = NULL;
    new_node->next = NULL;
    new_node->val = val;

    // case where our queue is completly empty
    if (q->len == 0) {
        q->len++;
        q->head = new_node;
        return q;
    }
    // case where we have a length of 1
    if (q->len == 1) {
        q->len++;
        q->tail = q->head;
        q->head = new_node;
        q->head->next = q->tail;
        q->tail->prev = q->head;
        return q;
    }

    // case other
    q->len++;
    new_node->next = q->head;
    q->head->prev = new_node;
    q->head = new_node;
    return q;
}

int dequeue(queue* q) {
    // case where we have an empty queue
    if (q->len == 0) {
        printf("cannot dequeue an empty queue");
        return -1;
    }
    
    // case where we have length 1
    if (q->len == 1) {
        q->len--;
        int val = q->head->val;
        free(q->head);
        q->head = NULL;
        return val;
    }

    // case where we have length 2
    if (q->len == 2) {
        q->len--;
        int val = q->tail->val;
        q->head->next = NULL;
        free(q->tail);
        q->tail = NULL;
        return val;
    }

    q->len--;
    int val = q->tail->val;
    node* new_tail = q->tail->prev; 
    free(q->tail);
    q->tail = new_tail;
    q->tail->next = NULL;
    return val;
}

void free_queue(queue* q) {
    node* current = q->head;
    while (current != NULL) {
        node* tmp = current;
        current = current->next;
        free(tmp);
    }
    free(q);
}

int main(void) {

}




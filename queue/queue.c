#include "queue.h"
#include <stdlib.h>
#include <stdio.h>

queue* create_queue() {
    queue* q = malloc(sizeof(queue));
    q->head = NULL;
    q->tail = NULL;
    q->len = 0;
    return q;
}

queue* enqueue(queue* q, int val) {
    node* new_node = malloc(sizeof(node));
    new_node->next = NULL;
    new_node->val = val;

    if (q->tail) {
        q->tail->next = new_node;
        new_node->prev = q->tail;
    } else { // Queue was empty, new node is also head
        q->head = new_node;
    }

    q->tail = new_node;
    q->len++;

    return q;
}

int dequeue(queue* q) {
    if (q->len == 0) {
        printf("Cannot dequeue an empty queue\n");
        return -1;
    }

    node* temp = q->head;
    int val = temp->val;
    
    q->head = q->head->next;
    if (q->head) {
        q->head->prev = NULL;
    } else { // Queue is now empty
        q->tail = NULL;
    }

    free(temp);
    q->len--;

    return val;
}

int get_len(queue* q) {
    return q->len;
}

void print_queue_from_head(queue* q) {
    printf("printing queue from head: [");

    if (q->len == 0) printf("empty queue");

    if (q->len == 1) printf("%i", q->tail->val);

    node* current = q->head;
    for (int i = 0; i < q->len; i++) {
        printf("%i, ", current->val);
        current = current->next;
    }
    printf("]\n");
}

void print_queue_from_tail(queue* q) {
    printf("printing queue from head: [");

    if (q->len == 0) printf("empty queue");

    node* current = q->tail;
    for(int i = 0; i < q->len; i++) {
        printf("%i, ", current->val);
        current = current->prev;
    }
    printf("]\n");
}

void free_queue(queue* q) {
    node* current = q->head;
    while (current != NULL) {
        node* next = current->next;
        free(current);
        current = next;
    }

    free(q);
}

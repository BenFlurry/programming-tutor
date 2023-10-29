#include "queue.h"
#include <stdio.h>

void empty_queue() {
    printf("----- testing empty queue -----\n");
    printf("creating queue\n");
    queue* q = create_queue();
    print_queue_from_head(q);
    print_queue_from_tail(q);
    dequeue(q);
    printf("freeing queue\n");
    free_queue(q);
    printf("\n");

}

void length_1_queue() {
    printf("----- testing for a queue of length 1 -----\n");
    queue* q = create_queue();
    q = enqueue(q, 1);
    print_queue_from_head(q);
    print_queue_from_tail(q);
    int i = dequeue(q);
    printf("results of dequeue: %i", i);
    q = enqueue(q, 1);
    printf("freeing queue\n");
    free_queue(q);
    printf("\n");
}

void length_5_queue() {
    printf("----- testing for a queue of length 1 -----\n");
    queue* q = create_queue();
    for (int i = 0; i < 5; i++) {
        q = enqueue(q, i);
    }
    print_queue_from_head(q);
    print_queue_from_tail(q);
    int i = dequeue(q);
    printf("results of dequeue: %i", i);
    q = enqueue(q, 1);
    printf("freeing queue\n");
    free_queue(q);
    printf("\n");
}

int main(void) {
    // test cases for an empty queue
    empty_queue();

    // test cases for a queue of length 1
    length_1_queue();

    //test cases for a queue of length 5
    length_5_queue();

    return 0;
}
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

queue* create_queue();

queue* enqueue(queue* q, int val);

int dequeue(queue* q);

void free_queue(queue* q);

void print_queue_from_head(queue* q);

void print_queue_from_tail(queue* q);

int get_len(queue* q);

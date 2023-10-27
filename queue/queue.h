typedef struct _queue {
    node* head;
    node* tail;
    int len;
} queue;

typedef struct _node {
    struct _node* next;
    struct _node* prev;
    int val;
} node;

queue* create_queue();

queue* enqueue(queue* q, int val);

int dequeue(queue* q, int val);

void free_queue(queue* q);

void print_queue_from_head(queue* q);

void print_queue_from_tail(queue* q);

int get_len(queue* q);

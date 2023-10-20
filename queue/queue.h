typedef struct _queue {
    node* head;
    int len;
} queue;

typedef struct _node {
    struct _node* next;
    int val;
} node;

queue* create_queue();

queue* enqueue(int val);

void print_queue();

int dequeue();

int get_len();

int peek();
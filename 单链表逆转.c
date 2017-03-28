#include <iostream>
using namespace std;

//int maxlen = 0;
//int maxindex = 0;
//
//char visit[256];

typedef int datatype;

typedef struct NODE{

  datatype data;

  struct NODE *next;



}Node, *LinkList;

LinkList LinkListCreate(const int n)
{
  int i=0;
  LinkList head;
  Node *p;
  head = NULL;
  for (; i < n; i++)
  {
    p = (Node*)malloc(sizeof(Node));
    if (NULL == p)
      perror("ERROR");
    scanf_s("%d", &p->data);
    p->next = head;
    head = p;

  }
  return head;
}

Node* recursive_Link(Node* head)
{
  if (head == NULL || head->next == NULL)
    return head;
  Node* p1 = head;
  Node* p2 = p1->next;  //p2其实记录的下一步递归过程后的尾结点
  head = recursive_Link(p2);
  p2->next = p1;
  p1->next = NULL;

  return head;
}

void main()
{
  Node *head = LinkListCreate(4);

  Node* n_head = recursive_Link(head);

  for (Node* index = n_head; index != NULL; index=index->next)
  {
    printf("%d", index->data);
  }
  system("pause");
}
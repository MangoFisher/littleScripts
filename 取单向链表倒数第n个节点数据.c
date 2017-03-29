#include<stdio.h>
#include <stdlib.h>
#include<string.h>
#include <iostream>

using namespace std;

struct Node
{
  int data;
  Node* next;
};

void initList(Node* vNode)
{
  for (int i = 0; i < 20; ++i)
  {
    Node* TempNode = new Node;
    TempNode->data = i;
    TempNode->next = vNode->next;
    vNode->next = TempNode;
  }
}

Node* getNthBackWards(Node* vnode, int vN)
{
  if (vN <1 || vnode == NULL)
  {
    return NULL;
  }

  Node* p = vnode;
  Node* q = vnode;

  while (vN > 0)
  {
    q = q->next;
    if (q == NULL)
    {
      return NULL;
    }
    --vN;
  }
  while (q != NULL)
  {
    q = q->next;
    p = p->next;
  }
  return p;

}

void main()
{
  Node* root = new Node;
  root->next = NULL;
  initList(root);
  Node* result = getNthBackWards(root,7);
  std::cout << result->data << std::endl;
  system("pause");
}
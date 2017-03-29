#include<stdio.h>
#include<string.h>
char getUniqueCharacter(char *s) {
  int order[256] = { 0 };
  int counter[256] = { 0 };
  int i = 0;
  char temp;
  char *p = s;
  while (*p) {
    temp = *p;
    if (counter[temp] == 0) {
      order[i++] = temp;
    }
    counter[temp]++;
    p++;
  }
  int j;
  for (j = 0; j < 256; j++) {
    if (order[j] != 0) {
      if (counter[order[j]] == 1) {
        temp = order[j];
        break;
      }
    }
  }
  if (j >= 256) {
    return '#';
  }
  else {
    return temp;
  }
}

void main() {
  char s[] = "abcdbcde";
  int n = strlen(s);
  char result = getUniqueCharacter(s);
  printf("%c\n", result);
  getchar();
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int numberOfArithmeticSlices(int* A, int ASize){
  int n_sub(int head, int tail)
  {
    if (tail < head + 2)
      return 0;
    int k = tail - (head + 1);
    return (k + 1) * k / 2;
  }
  int n = 0;
  int head;
  int tail;
  int diff;
  int i;
  //for (head=0; head<ASize-2; head++) {
  for (head=0; head<ASize-2;) {
    //tail = head + 1;
    tail = head;
    diff = *(A+head+1) - *(A+head);
    for (i=2; head+i<ASize; i++) {
      if (*(A+head+i) - *(A+head+i-1) == diff)
        tail = head + i;
      else
        break;
    }
    n += n_sub(head, tail);
    if (tail == head)
      head += 1;
    else
      head = tail - 1;
  }

  return n;
}


int main()
{
  int A[] = {1,2,3,4};
  int ASize = 4;
  int n = numberOfArithmeticSlices(A, ASize);
  printf("numberOfArithmeticSlices(A, ASize) = %d\n", n);
  return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
//#include <stdio.h>
#include <stdlib.h>

int comp (const void *elem1, const void *elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

int* findErrorNums(int* nums, int numsSize, int* returnSize){
  returnSize = malloc(2*sizeof(int));
  // Sort nums in place
  qsort(nums, numsSize, sizeof(int), comp);
  int prev = 0;
  int current;
  int is_empty = 1;
  for (int i=0; i<numsSize; i++) {
    current = *(nums + i);
    if (current - prev == 1)
      ;
    else if (current - prev == 0)
      *returnSize = current;
    else if (current - prev == 0) {
      *(returnSize + 1) = current - 1;
      is_empty = 0;
    }
    prev = current;
  }
  /* Note that current - prev == 2 not guaranteed
     to happen, but that current - prev == 0 is
     guaranteed to take place. */
  if (is_empty)
    *(returnSize + 1) = numsSize;
}



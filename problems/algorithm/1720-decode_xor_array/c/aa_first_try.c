#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize){
  int *arr;
  *returnSize = encodedSize + 1;
  arr = malloc(sizeof(int)*(*returnSize));
  //arr = (int*)malloc(sizeof(int)*(encodedSize+1));
  //arr = (int*)malloc(encodedSize+1);
  int i;
  *arr = first;
  for (i=0;i<encodedSize;i++) {
    *(arr+(i+1)) = encoded[i] ^ *(arr+i);
  }
  return arr;
}

#include <stdio.h>
#include <stdlib.h>
#include "aa_first_try.h"

int main(int argc, char **argv) {
  int *decoded;

  int encoded[] = {6,2,7,3};
  int first = 4;
  int encodedSize = 4;
  
  //int encoded[] = {1,2,3};
  //int first = 1;
  //int encodedSize = 3;

  decoded = decode(encoded, encodedSize, first, NULL);
  for (int i=0; i<encodedSize+1; i++)
    printf("%d\n", *(decoded+i));
  return 0;
}

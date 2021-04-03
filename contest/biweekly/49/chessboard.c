#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
//#include <ctype.h>


//bool squareIsWhite(char * coordinates){
int squareIsWhite(char * coordinates){
  char letter = *coordinates;
  char number = *(coordinates+1);
  int ret = ((letter - 'a') % 2 + (number - '1') % 2) % 2;
  return ret;
}



int main(int argc, char **argv) {
  int x = '9' - '1';
  printf("'9' - '1' = %d\n", x);
  //char co[] = {'h', '3'};
  char co[] = {'c', '7'};
  int y = squareIsWhite(co);
  printf("y = %d\n", y);
  return 0;
}

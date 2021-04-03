bool squareIsWhite(char * coordinates){
  char letter = *coordinates;
  char number = *(coordinates+1);
  int ret = ((letter - 'a') % 2 + (number - '1') % 2) % 2;
  return ret;
}

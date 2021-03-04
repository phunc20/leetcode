

int missingNumber(int* nums, int numsSize){
  // sum = 0+1+2+...+n
  int sum = (1+numsSize)*numsSize/2;
  int i;
  for (i=0; i < numsSize; i++)
    sum -= *(nums+i);
  return sum;
}

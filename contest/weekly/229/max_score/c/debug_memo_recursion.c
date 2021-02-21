#include <stdio.h>
#include <stdlib.h>
//#include <string.h>
//#include <ctype.h>
//#include <math.h>


int maximumScore(int* nums, int numsSize, int* multipliers, int multipliersSize){
  int memo[numsSize][numsSize];
  int filled[numsSize][numsSize];
  for (int l=0; l<numsSize; l++) {
    for (int r=0; r<numsSize; r++) {
      filled[l][r] = 0;
      memo[l][r] = 0;
    }
  }
  float epsilon = 1e-5;
  int in_memo(int left, int right) {
    //printf("abs(memo[left][right] - empty) = %f\n", abs(memo[left][right] - empty));
    //return abs(filled_or_not[left][right] - empty) > epsilon;
    return filled[left][right];
  }
  // (?1) Existe-t-il Dictionary dans C?
  int recursive_dp(int left, int right)
  {
      /* left ~ right (both end included) */
      /* 0 <= left < right <= n-1         */
      if (in_memo(left, right)) {
        //printf("left = %d, right = %d\n", left, right);
        //printf("in_memo = True\n");
        //return (int) memo[left][right];
        return memo[left][right];
      }
      int n_multiplied = numsSize - (right - left + 1);
      int *remainig_multipliers = multipliers + n_multiplied;
      int ans;
      int ll, rr;
      // Python's if len(remainig_multipliers) == 1 must be translated to the following
      if (multipliersSize - n_multiplied == 1) {
        ll = *(nums+left)  * (*remainig_multipliers);
        rr = *(nums+right) * (*remainig_multipliers);
      }
      else {
        ll = *(nums+left)  * (*remainig_multipliers) + recursive_dp(left+1, right);
        rr = *(nums+right) * (*remainig_multipliers) + recursive_dp(left, right-1);
      }
      ans = ll > rr ? ll : rr;
      memo[left][right] = ans;
      filled[left][right] = 1;
      return ans;
  }

  return recursive_dp(0, numsSize-1);
}


int main(int argc, char **argv) {
  printf("Q11\n");
  int nums[] = {920,108,-649,-682,-778,-268,-611,795,-877,-338,804,931,959,-754,-909,-9,-245,-553,-296,500,-190,-227,-258,-683,-1000,-833,505,481,419,-29,341,522,-495,109,-106,543,616,491,-143,766,769,1000,-378,341,498,-456,14,428,470,-917,133,454,-411,-64,551,929,-186,396,-822,-781,348,445,-786,-330,334,856,-204,-294,483,-802,-138,960,991,949,-294,355,-856,-437,-413,307,-950,-263,-506,-668,60,957,-654,-726,711,-799,-222,761,865,706,626,-384,922,590,891,-784,853,-82,79,-149,420,-546,887,-57,-415,728,586,-260,176,-56,-907,839,-664,821,213,-59,394,-204,-327,-163,-874,-557,-15,646,937,-538,171,-115,491,878,963,332,-573,962,287,980,792,325,537,657,146,-899,-497,595,-644,703,-212,23,-941,-944,402,267,894,-393,1000,766,44,864,-231,373,484,404,441,-554,650,-847,181,-141,506,970,619,427,-239,413,-294,-408,-249,-101,-255,357,-608,-946,-431,639,464,-797,836,-272,850,-253,-383,902,579,836,-786,-802,493,85,-982,-757,348,742,-418,149,-748,126,-150,831,-217,-752,-961,-664,-864,408,-713,403,805,-200,-858,-716,-849,-249,67,650,662,619,-108,608,-43,168,-225,582,3,-624,899,394,692};
  int numsSize = sizeof(nums) / sizeof(int);
  int multipliers[] = {-112,19,-462,-463,-575,-337,-167,11,-736,-441,-811,94,-37,-841,-515,184,-697,-361,-143,892,697,-609,461,872,685,801,-653,417,329,876,372,118,346,-207,-631,-122,214,233,-628,931,846,-824,819,868,-802,132,-728,-241,-669,-757,693,485,-117,488,659,237,-687,219,-871,727,697,630,-106,207,-564,818,-561,-999,329,-454,367,490,-144,-85,522,-136,-161,115,130,801,-368,447,943,555,-271,-643,216,-456,-935,663,822,263,-387,167,-928,-371,-805,972,-962,661,-1000,-283,-883,865,-311,-88,-924,334,850,-806,-111,-387,7,-822,708,-847,-932,-142,403,921,443,16,982,-423,-508,519,-14,967,-88,-765,679,-697,-682,-448,741,-416,96,0,-498,968,-927,222,686,461,489,356,885,618,134,121,-298,-208,571,-425,603,532,-463,908,480,852,-418,-597};
  int multipliersSize = sizeof(multipliers) / sizeof(int);
  int ans = maximumScore(nums, numsSize, multipliers, multipliersSize);
  int expected = 43563107;
  if (ans == expected)
    printf("Correct\n");
  else
    printf("Incorrect: ans = %d, expected = %d\n", ans, expected);
  return 0;
}

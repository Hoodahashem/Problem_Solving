#include "stdio.h"
#include "stdlib.h"

int searchInsert(int* nums, int numsSize, int target) {
    int right = numsSize - 1;
	int left = 0;
    
	while(left <= right)
	{
        int mid = left + (right - left) / 2;
        if(nums[mid] == target) {
            return mid;
        } else if(nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
	}
    return left;
}


int main(void){
	int nums[] = {1,3,5,6}; 
	int target = 7;
	int numsSize = sizeof(nums) / sizeof(nums[0]);
	int result = searchInsert(nums, numsSize, target);
	printf("result: %d\n", result); // 4
	return 0;
}

## 乘积小于k的子数组
class Solution1:
	def numSubarrayProductLessThanK(self,nums,k):
		ans=left=0
		plus_total=1
		if k>=1:
			return 0
		for right,c in enumerate(nums):
			plus_total*=c
			while plus_total>=k:
				plus_total/=nums[left]
				left+=1
			ans+=right-left+1
		return ans

if __name__ == '__main__':
	nums=[10,5,2,6]
	k=100
	s=Solution1()
	print(s.numSubarrayProductLessThanK(nums,k))
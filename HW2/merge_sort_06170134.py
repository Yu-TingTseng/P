#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Solution(object): 
    def merge(self,a,b):#要記得加self  
        y=[] 
        while a and b: 
            if (a[0]<b[0]):
                y.append(a.pop(0))
            else:
                y.append(b.pop(0))
        y+=a  
        y+=b
        return y

    def merge_sort(self,nums):
        while len(nums)<=1:
            return nums
        else:
            mid=len(nums)//2 
            a=nums[:mid]
            b=nums[mid:]
            
        x=Solution().merge(Solution().merge_sort(a),Solution().merge_sort(b))#要記得把Solution().
        return  x
    
nums=[6,8,9,20,13,1,34]
output=Solution().merge_sort(nums)
output    


# In[ ]:


#助教我不懂為什麼我用list可以,用self就不行，可以請你告訴我嗎?謝謝
#找到了 謝謝


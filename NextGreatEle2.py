class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a,st= [],[]
        
        num1 =nums*2
        for i in range(len(num1)-1,-1,-1):
            if len(st)==0:
                a.append(-1)
            else:
                while len(st)>0 and st[-1] <= num1[i]:
                    st.pop()
                if len(st)==0:
                    a.append(-1)
                else:
                    a.append(st[-1])
            st.append(num1[i])
        a= a[::-1]
        return a[0:len(nums)]

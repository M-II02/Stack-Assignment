class Solution:
    def nextLargerElement(self,arr,n):
        
        a,st= [],[]
        
        for i in range(n-1,-1,-1):
            if len(st)==0:
                a.append(-1)
            else:
                while len(st)>0 and st[-1] <= arr[i]:
                    st.pop()
                if len(st)==0:
                    a.append(-1)
                else:
                    a.append(st[-1])
            st.append(arr[i])
        a = a[::-1]
        return a

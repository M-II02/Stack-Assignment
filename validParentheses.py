class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(0,len(s)):
            if s[i]== "(" or s[i]=="{" or s[i]=="[":
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                top = st.pop()
                if (s[i]==")" and top!= "(") or (s[i]=="}" and top!= "{") or (s[i]=="]" and top!= "[") :
                    return False
        if len(st)==0:
            return True
        return False

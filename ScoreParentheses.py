class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        ans = 0
        top = -1
        for i in range(len(s)):
            if s[i] == '(':
                st.append(0)
            elif s[i] == ')':
                c_in = st.pop()
                if c_in > 0:
                    count = 2 * c_in
                else:
                    count= 1
                if len(st) == 0:
                    ans += count
                else: 
                    st[top] += count
        return ans

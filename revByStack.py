def reverse(S):
  str = ''
  st = []
  for a in S:
    st.append(a)
   while(st):
    str += st.pop()
    return str

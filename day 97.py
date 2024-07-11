#Program to Check Balanced of Parenthesis in Python
def isbalanced(s):
  c= 0
  ans=False
  for i in s:
    if i == "(": 
     c += 1
    elif i == ")":
     c-= 1
    if c < 0:
     return ans
    if c==0:
     return not ans
  return ans
s="{[]}"
print("Given string is balanced :",isbalanced(s))
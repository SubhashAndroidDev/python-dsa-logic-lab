""" 
g = children's greed factors
s = cookie sizes

cookie_size >= child's_greed
Each child can get at most one cookie, and each cookie can be given to at most one child.
"""


# Sort both arrays and always give the smallest possible cookie to the child with the smallest greed.
def findContentChildren(g, s):
    g.sort()
    s.sort()

    child=0
    cookie=0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1

        cookie += 1
    return child

g=[1,2,3]
s=[1,1]
print(findContentChildren(g,s))
# Two pointers (sorted/palindrome):

l, r = 0, len(a)-1
while l < r:
    # do work / check
    l += 1; r -= 1


# Sliding window (variable size):

need = {}
have = {}
l = 0
for r, x in enumerate(a):
    # expand with a[r]
    while cond_violated():
        # shrink from left
        l += 1
    # best = max(best, r-l+1)

# Prefix sum + hashmap (subarray sum == k):

seen = {0:1}; ps = 0; ans = 0
for x in nums:
    ps += x
    ans += seen.get(ps-k, 0)
    seen[ps] = seen.get(ps, 0) + 1

# Binary search on answer:

def ok(m): ...
lo, hi = L, R
while lo < hi:
    m = (lo+hi)//2
    if ok(m): hi = m
    else: lo = m+1
return lo

# Monotonic stack (next greater):

st, ans = [], [-1]*len(a)
for i, x in enumerate(a):
    while st and a[st[-1]] < x:
        ans[st.pop()] = x
    st.append(i)

# BFS grid:

from collections import deque
q = deque([start]); seen = {start}
while q:
    r, c = q.popleft()
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = r+dr, c+dc
        if valid(nr,nc) and (nr,nc) not in seen:
            seen.add((nr,nc)); q.append((nr,nc))

# Union–Find (DSU):

par = list(range(n)); rk = [0]*n
def find(x):
    while par[x]!=x:
        par[x]=par[par[x]]; x=par[x]
    return x
def union(a,b):
    ra, rb = find(a), find(b)
    if ra==rb: return False
    if rk[ra]<rk[rb]: ra, rb = rb, ra
    par[rb]=ra
    if rk[ra]==rk[rb]: rk[ra]+=1
    return True

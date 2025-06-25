


import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-stone for stone in stones] # converts min-heap to max-heap (returns largest)
        heapq.heapify(stones)  

        while len(stones) > 1:
            # returns the largest two values from max-heap
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # if the two largest stones do not have the same weight
            # (do not destroy each other completly)
            if first != second:
                # "Smash" them and push the difference into the heap
                # negating in order to simulate a max-heap using min-heap
                heapq.heappush(stones, -(first - second))
        
        # if a stone is left over, return the weight (converted back to a positive number)
        # if all stones are destroyed, return 0
        return -stones[0] if stones else 0

"""
Case 1-

INPUT:
stones =
[2,7,4,1,8,1]

OUTPUT:
1

Case 2-

INPUT:
stones =
[1]

OOUTPUT:
1


"""

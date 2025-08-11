'''
Link: https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=plakya4j

Problem: LeetCode 141: Linked List Cycle, Floyds tortoise and Hare algorithm

Time Complexity: O(n), Space Complexity: O(1) 
'''

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#Floyds tortoise and Hare algo.
class Solution(object):
    def hasCycle(self, head):
        one_step, two_step = head, head #both start at head of list

        while two_step and two_step.next:
            one_step = one_step.next #1st pointer (moving one step)
            two_step = two_step.next.next #2nd pointer (moving two steps)

            if one_step is two_step: #if cycles exists 2nd pointer will eventually == 1
                return True
        return False #otherwise return False

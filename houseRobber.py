"""
Prompt: You are planning to rob houses on a specific street, 
and you know that every house on the street has a certain amount of money 
hidden. The only thing stopping you from robbing all of them in one night is 
that adjacent houses on the street have a connected security system. 
The system will automatically trigger an alarm if two adjacent houses are
 broken into on the same night.

Given a list of non-negative integers nums representing 
the amount of money hidden in each house, determine the 
maximum amount of money you can rob in one night without triggering an alarm.

Source of prompt: CodeSignal
"""


def houseRobber(nums):
    m, n = 0, 0
    for num in nums:
        m, n = max(n+num, m), m
    return max(m,n)
# Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
[LeetCode](https://leetcode.com/problems/two-sum/)

# Intuituon
The Two Sum problem asks us to find two numbers in an array that sum up to a given target value. We need to return the indices of these two numbers.

# Approach
1. Use a brute force approach to check every pair of elements to see if their sum equals the target. This involves nested loops. This approach has a time complexity of $O(n^2)$, where $n$ is the number of elements in the list, a space complexity of $O(1)$.(See solve1.py)
2. A more efficient approach is to use a hash table. We iterate through the list once, and for each element, check if the target minus the current element exists in the hash table. If it does, we are done. If not, we add the current element to the hash table. This approach has a time complexity of $O(n)$, where $n$ is the number of elements in the list, and a space complexity of $O(n)$.(See solve2.py)

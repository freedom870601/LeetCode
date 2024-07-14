# Description
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

# Intuition
The problem requires us to determine if the given string of brackets is valid or not. We can use a stack data structure to keep track of opening brackets encountered and check if they match with the corresponding closing brackets.
# Approach
1. Initialize an empty stack.
2. Traverse the input string character by character.
3. If the current character is an open bracket (i.e., (, {, [), push it onto the stack.
4. If the current character is a close bracket (i.e., ), }, ]), check if the stack is empty. If it is empty, return false. Otherwise, pop the top element from the stack and check if it is the corresponding open bracket. If it does not match, return false.
5. After traversing the entire input string, check if the stack is empty. If it is empty, return true. Otherwise, return false because some opening brackets have not been matched with their corresponding closing brackets.

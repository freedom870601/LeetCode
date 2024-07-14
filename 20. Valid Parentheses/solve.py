class Solution:
    def isValid(self, s: str) -> bool:
        left_bracket = ['(', '{', '[']
        right_bracket = [')', '}', ']']
        check_bracket = dict()
        for i in range(3):
            check_bracket[left_bracket[i]] = right_bracket[i]
        stack = []
        for t in s:
            if t in left_bracket:
                stack.append(t)
            if t in right_bracket:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if check_bracket[tmp] != t:
                    return False
        if stack == []:
            return True
        else:
            return False

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pop_list = ['}',']',')']
        dic ={"}":"{","]":"[",")":"("}
        if(len(s) % 2 !=0):
            return False
        for i in s:
            if i not in pop_list:
                stack.append(i)
            else:
                if len(stack) != 0 and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False
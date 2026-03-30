class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i not in "+-*/":
                stack.append(int(i))

            else:
                if stack:
                    number2 = stack.pop()
                    number1 = stack.pop()
                    if i == '+':
                        new_number = number1 + number2
                        stack.append(new_number)
                    elif i == '-':
                        new_number = number1 - number2
                        stack.append(new_number)
                    elif i == '*':
                        new_number = number1*number2
                        stack.append(new_number)
                    else:
                        new_number = int(number1/number2)
                        stack.append(new_number)

        return stack.pop()

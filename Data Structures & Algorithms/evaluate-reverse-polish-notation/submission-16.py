class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 1
        numbers = []
        tokens = list(reversed(tokens))
        while(len(tokens) > 0):
            temp = tokens.pop()
            print(temp)
            if temp.lstrip("-").isdigit():
                numbers.append(int(temp))
            else:
                num1 = numbers.pop()
                num2 = numbers.pop()
                if(temp == "+"):
                    numbers.append(num1 + num2)
                elif( temp == "-"):
                    numbers.append(num2 - num1)
                elif(temp == "/"):
                    numbers.append(int(num2/num1))
                elif temp == "*":
                    numbers.append(num1 * num2)
        print(numbers[0])
        return int(numbers[0])
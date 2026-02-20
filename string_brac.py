'''
🧩 Problem: Check if a String of Brackets is Balanced
You are given a string containing only the characters:
Copy code

(  )  {  }  [  ]
Determine whether the string is balanced.
A string is balanced if:
Every opening bracket has a corresponding closing bracket.
Brackets are closed in the correct order.
Example 1
Input:
{[()]}
Output:
True
Example 2
Input:
{[(])}
Output:
False
Example 3
Input:
((()
Output:
False
💡 Constraint
Length of string can be up to 10⁵.
'''

# Solution

def brackets_check(string):
	brackets_dict = {")":"(","}":"{","]":"["}
	stack = []

	if len(string) > 10**5:
		return f"{False}\nBecause your's string wants to accquire memory more than the system's total memory "

	for char in string:
		if char in brackets_dict.values():
			stack.append(char)
		elif char in brackets_dict.keys():
			if not stack:
				return False
			if stack[-1] != brackets_dict[char]:
				return False
			stack.pop()
		else:
			if len(stack) > 0:
				return f"{False}\nYou were in right track initialy, but for some reasons you went astray \nand started entering any random values"
			else:
				return f"{False}\nBecause you are entering input other than the original input"
	return len(stack) == 0

def main(test):
	print(f"result: {brackets_check(test)}")


if __name__ == "__main__":
	testcase = input("enter the input of your choice: ")
	main(testcase)
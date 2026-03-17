try:
	x = int(input("enter the square number: "))
except:
	print("you enter wrong number.")

def sqrt(num):
	if (x == 0 or x == 1):
		return x
	last_guess = x/2
	print(last_guess)
	while True:
		guess = (last_guess + x/last_guess)/2
		print(guess)
		if abs(guess - last_guess) < .000001:
			return guess
		last_guess = guess

print(sqrt(x))

# print(64**0.5)
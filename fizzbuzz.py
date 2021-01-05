
amount = input('Enter the amount to go to: ')
amount = int(amount)

'''

If the number is divisible by 3, write Fizz instead of the number
If the number is divisible by 5, write Buzz instead of the number
If the number is divisible by 3 and 5 both, write FizzBuzz instead of the number
otherwise, write the number as a string

'''


for x in range(amount):
	if x % 3 == 0:
		print('Fizz')

	elif x % 5 == 0:
		print('Buzz')

	elif x % 3 == 0 and x % 5 == 0:
		print('FizzBuzz')

	else:
		print(x)



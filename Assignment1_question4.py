n = int(input('Enter the number: '))


f1=1
f2=1
i=2

if n <= 0:
	print(input('please enter number again(Positive): '))
elif n == 1:
	print(f1)
else:
	print(f1)
	print(f2)

	while i < n:
		f3=f2+f1
		print(f3)
		f1=f2
		f2=f3
		i=i+1



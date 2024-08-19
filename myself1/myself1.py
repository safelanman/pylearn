numbers = []

print("Вводи число одно за другим. Чтобы остановиться, просто нажми Enter без ввода числа.")

#for i in range(3):
#	number = int(input(f"Введи число {i +1}: "))
#	numbers.append(number)

while True:
	user_input = input("Введи число (или нажми Enter для завершения): ")
	if user_input == "":
		break
	try:
		number = int(user_input)
		numbers.append(number)
	except ValueError:
		print("Пожалуйста, вводите только целые числа.")
		continue

if len(numbers) > 0:
	average = sum(numbers) / len(numbers)

#if average.is_integer():
	average = int(average)

	print(f"Среднее арифметическое: {average}")
else:
	print("Ты не ввел ни одного числа.")


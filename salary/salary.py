hoursAmount = float(input("введите количество отработанных часов: "))
hourRate = float(input("введите ставку за час: "))
MULTIPLIER = 1.5
if hoursAmount > 40:
	overtime = hoursAmount - 40
	salary = 40 * hourRate + overtime * hourRate * MULTIPLIER
	print(salary)
else:
	print(hoursAmount * hourRate)
	
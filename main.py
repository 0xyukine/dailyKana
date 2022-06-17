from randomkana import RandomKana

rk = RandomKana()
print(rk.random())

while True:
	r = rk.random()
	print(r[0])
	i = input()
	if i == r[1][0]:
		print("Correct")
	else:
		print(f"False, correct answer is: {r[1][0]}")
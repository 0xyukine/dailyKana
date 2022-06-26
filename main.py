from randomkana import RandomKana

rk = RandomKana()
print("(h)iragana, (k)atakana, or (b)oth: ", end="")
choice = input()
if choice in {"h","k","b"}:
	while True:
		if choice == "h":
			r = rk.hira()		#Random hiragana
		elif choice == "k":
			r = rk.kata()		#Random katakana
		elif choice == "b":
			r = rk.kana()		#Random kana

		print(r[0])				#Prints the kana
		i = input()
		if i == r[1][0]:		#Tests user input against romanization
			print("Correct")
		else:
			print(f"False, correct answer is: {r[1][0]}")
else:
	print("Invalid choice")
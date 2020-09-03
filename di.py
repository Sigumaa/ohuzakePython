birthdays ={}

while True:
	print("名前を入力してください(終了するにはEnterキーだけ押してください)")
	name = input()
	if name == "":
		break


	if name in birthdays:
		print(name + "の誕生日は" + birthdays[name])
	else:
		print(name + "の誕生日は未登録です。\n誕生日を入力してください")
		bday = input()
		birthdays[name] = bday
		print("更新したよ")

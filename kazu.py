# 数あてゲーム

import random

secret_number = random.randint(1,20)
print("1～20までの数を当ててください")

for guesses_taken in range(1,7):
	print("数を入力してください")
	guess = int(input())

	if guess <secret_number:
		print("小さいよ")
	elif guess > secret_number:
		print("大きいよ")
	else:
		break #あたり！


if guess == secret_number:
	print("あたり！" + str(guesses_taken) + "回で当たりました！")
else:
	print("残念だったな！ｗ正解は" + str(secret_number) + "でした")

end = input("エンターで終了")
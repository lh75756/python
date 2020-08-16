"""
Author:lihang
Time:2020.8.4
Description:
一个多回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
#!/usr/bin/python3
def game():
	#定义变量
	my_hp = 1000
	my_power = 200
	your_hp = 1000
	your_power = 199
	#循环进行血量计算
	while True:
		my_hp = my_hp - your_power
		your_hp = your_hp - my_power
		if my_hp <= 0:
			print("you win")
			#满足条件后跳出循环
			break
		elif your_hp <= 0:
			print("i win")
			#满足条件后跳出循环
			break
#调用函数
game()
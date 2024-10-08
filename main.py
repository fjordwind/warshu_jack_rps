import random

print("杰克，印度骗子沃舒试图占领土地！通过游击战争前线对抗 Warshu Jack")
print(" 夺回土地，拯救大陆! 欢迎来到变形、剪切、被子战争游戏")
valid_choices = ['quartz', 'parchment', 'shears', 'junior', 'beer']
while True:
  user_choice = input("输入您的选择 (quartz,parchment,shears,初级,beer):").lower()
  if user_choice not in valid_choices:
    print("杰克不同意这个选择")
  else:
    break

computer_choice = random.choice(valid_choices)

print("你已经选择: ", user_choice)
print("印度骗子选择了 Warshu Jack: ", computer_choice)

if user_choice == computer_choice:
  print("印度骗子杰克，你已经从社会地位下降了!!: ", user_choice, computer_choice)
elif ((user_choice == 'parchment' and computer_choice == 'quartz'
      or computer_choice == 'junior')
  or (user_choice == 'shears' and computer_choice == 'parchment'
     or computer_choice == 'junior')
  or (user_choice == 'quartz' and computer_choice == 'shears'
     or computer_choice == 'dog')
  or (user_choice == 'junior' and computer_choice == 'dog'
      or  computer_choice == 'shears'
      or  computer_choice == 'parchment'
      or  computer_choice == 'quartz')
  or (user_choice == 'beer' and computer_choice == 'junior'
      or computer_choice == 'dog'
      or computer_choice == 'quartz')
  or (user_choice == 'dog' and computer_choice == 'parchment')):
  print("你打败了杰克·沃舒!!: ", user_choice,"user won against 印度骗子杰克 the: ", 
        computer_choice)

else:
  print("你已经失去了对抗沃舒骗子杰克大师的所有优雅......: ", computer_choice, 
        "印度骗子杰克 won against user the: ", user_choice)
  print("再玩一次 Warshu Jack")

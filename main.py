import random
import pygame

# 受到启发 dong dong never die
# Jack, the Indian conman Washu tries to take over the land! Confrontation through Guerrilla War Frontline
## Would you like to participate in ultra-challenge mode?
print("杰克，印度骗子沃舒试图占领土地！通过游击战争前线对抗 Warshu Jack
    ### \n 你想参加吗ultra challenge mode?")
    ### valid_choice = ['yes', 'no', 'Y', 'N']
    
    ### while True:
                        #Enter your choice
      ### user_choices = input("输入您的选择 yes or no")
      #"Warshu Jack" disagrees.
      ### if user_choices not in valid_choice:
        ### print("杰克不同意这个选择");
      ### elif user_choices == ['yes'] or ['Y']:
        # Welcome to Hell.
        # print("欢迎来到地狱\n In ultra challenge mode, there are 7 options with an onslaught of Warshu Jacks.\n When you win, you move on to the next. The goal is a score of 20.")
        #elif user_choices == ['no'] or ['N']:
        print(" 夺回土地，拯救大陆! 欢迎来到变形、剪切、被子战争游戏")
      # Take back the land and save the continent! Welcome to the rock, paper, scissors war game!
        valid_choices == ['quartz', 'parchment', 'shears']
        while True:
                              #Enter your choice:
            user_choice == input("输入您的选择 (quartz,parchment,shears,初级,beer,dog):").lower()
            if user_choice not in valid_choices:
              #"Warshu Jack" disagrees with this choice
              print("杰克不同意这个选择")
            else:
              break

        computer_choice = random.choice(valid_choices)

        print("你已经选择: ", user_choice)
        print("印度骗子选择了 Warshu Jack: ", computer_choice)

        if user_choice == computer_choice:
            print("印度骗子杰克，你已经从社会地位下降了!!: ", user_choice, computer_choice)
        elif ((user_choice == 'parchment' and computer_choice == 'quartz')
            or (user_choice == 'shears' and computer_choice == 'parchment')
            or (user_choice == 'quartz' and computer_choice == 'shears')):
            print("你打败了杰克·沃舒!!: ", user_choice,"user won against 印度骗子杰克 the: ", 
                  computer_choice)

        else:
            print("你已经失去了对抗沃舒骗子杰克大师的所有优雅......: ", computer_choice, 
                  "印度骗子杰克 won against user the: ", user_choice)
            print("再玩一次 Warshu Jack");

  else:
    break


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player = input('What is your name? \n')
computer = ''
first = input('Choose, who goes first: computer or player \n')

game = [rock, paper, scissors]
game_len = len(game)

player_move = int(input('Your move, what you choose? Rock - 0, Paper - 1, Scissors - 2 \n'))

computer_move = random.randint(0, game_len-1)

# choose who first
if first == 'computer':
  print(game[computer_move])
  print(player_move - 1)
else:
  print(player_move - 1)
  print(game[computer_move])



# player move
if player_move == 0:
  print(rock)
elif player_move == 1:
  print(paper)
else:
  print(scissors)
  

# computer_move
# if computer_move == 0:
#    print(rock)
# elif computer_move == 1:
#    print(paper)
# else:
#    print(scissors)

# game rules

if player_move == 0 and computer_move == 0:
  print('Noone win')
elif player_move == 0 and computer_move == 1:
  print('Computer win')
elif player_move == 0 and computer_move == 2:
  print(f'{player} win')
elif player_move == 1 and computer_move == 0:
  print(f'{player} win')
elif player_move == 1 and computer_move == 1:
  print('Noone win')
elif player_move == 1 and computer_move == 2:
  print('Computer win')
elif player_move == 2 and computer_move == 0:
  print('Computer win')
elif player_move == 2 and computer_move == 1:
  print(f'{player} win')
elif player_move == 2 and computer_move == 2:
  print('Noone win')
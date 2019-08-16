import random
import pandas as pd

from player import add_player
from wordgame import listofplayers

def add_player_func(playername, word, opponent):
  try:
    add_player(playername, word, opponent)
  except:
      pass

def get_random_word():
    try:
        for player_word in listofplayers:
            listofwords = pd.read_csv("word.csv")
            player_word.word = listofwords["word"][random.randint(1,10)]
    except:
        pass

def print_list():
    for print_player in listofplayers:
        print("player name: "+ print_player.name +" player opponent : "+ print_player.opponent_name + " word :" + print_player.word +"\n")

def get_opponent():
    try:
        list_op = []
        for player in listofplayers:
            list_op.append(player)

        for player in listofplayers:
          while list_op:
            player_op = random.choice(list_op)
            if player != player_op:
               player.opponent_name = player_op.name
               list_op.remove(player_op)
               break
    except:
        pass


def kill_opponent():
 try:
    print("kill opponent")
    player_name = input("Enter your name : ")
    for player in listofplayers:
      if player.name == player_name:
       ans = input("Are you really {} ? y/n ".format(player_name))
       if str.lower(ans) == "y":
          kill_ans = input("Did you kill {} : y/n ".format(player.opponent_name))
          if kill_ans == "y":
             for opponent in listofplayers:
                 if opponent.name == player.opponent_name:
                    player.opponent_name = opponent.opponent_name
                    player.word = opponent.word
                    listofplayers.remove(opponent)
                    break
          else:
            print("So go kill him!")
 except:
     pass
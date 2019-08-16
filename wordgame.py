from Functions import *  # todo pot try except in functions logic

listofplayers = []


def main():
    try:
        print("Welcome to the game")
        numberOfplayers = input("enter number of players  : ")
        for players in range(int(numberOfplayers)):
            playername = input("enter player name : ")
            word = " "
            opponent = " "
            addplayer(playername, word, opponent)

        getrandomword()
        getopponent()
        printlist()
        killopponent()
        printlist()

    except Exception as e:
        print("error ", e)


if __name__ == "__main__":
    main()

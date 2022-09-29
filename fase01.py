import random

def play():
    user = input("'r' para pedra, 'p' para papel, 't' para tesoura\n")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'Voce ganhou!'
    if is_win(computer, user):
        return 'voce perdeu!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 't') or (player == 'p' and opponent == 'r')\
        or (player == 't' and opponent == 'p'):
        return True

print(play())

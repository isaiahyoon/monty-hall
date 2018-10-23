import random

def monty_hall(iterations):
    hits = 0
    for i in range(iterations):
        choices = [0, 1, 2]
        prize = random.randint(0, 2)

        player_choice = random.choice(choices)
        choices.remove(player_choice)
        revealed = random.choice(choices)

        if revealed == prize:
            if revealed == choices[0]:
                revealed = choices[1]
            else:
                revealed = choices[0]

        choices.remove(revealed)

        print('player choice: ' + str(player_choice))
        print('revealed: ' + str(revealed))
        print('prize ' + str(prize))
        print('=====================')
        
        if choices[0] == prize:
            hits += 1

    win_percent = 1.0 * hits / iterations
    print('winning percentage on switch: ' + str(win_percent))

monty_hall(2000)

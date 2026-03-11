import random

def monty_hall_simulation(trials):
    stay_wins = 0
    switch_wins = 0
    for i in range(10000):
        doors = [0,0,0]
        car = random.randint(0,2)
        doors[car] = 1

        choice = random.randint(0,2)

        possible = [i for i in range(3) if i!=choice and doors[i] == 0]
        opened = random.choice(possible)

        remaining = [i for i in range(3) if i!=choice and i!=opened][0]

        if doors[choice] == 1:
            stay_wins+=1
        if doors[remaining] == 1:
            switch_wins+=1

    print("Trials:", trials)
    print("Win rate if staying:", stay_wins/trials)
    print("win rate if switching:", switch_wins/trials)

monty_hall_simulation(10000)


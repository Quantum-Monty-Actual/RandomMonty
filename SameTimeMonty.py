import random

def simultaneous_monty_trials(num_trials):
    stay_wins = 0
    switch_wins = 0
    valid_trials = 0

    for _ in range(num_trials):
        # 3 doors: 0 = car, 1 = goat, 2 = goat (randomize car position)
        doors = [0, 1, 2]
        car = random.randint(0, 2)
        doors[car] = 0  # Car
        doors[(car + 1) % 3] = 1  # Goat
        doors[(car + 2) % 3] = 2  # Goat

        # Player and Monty guess simultaneously
        player_choice = random.randint(0, 2)
        monty_choice = random.randint(0, 2)

        # Toss if they pick the same door
        if player_choice == monty_choice:
            continue

        # Toss if Monty reveals the car
        if monty_choice == car:
            continue

        # Valid trial: Monty revealed a goat, different door
        valid_trials += 1
        remaining_door = 3 - (player_choice + monty_choice)  # Last door (0+1+2=3)

        # Check wins
        if player_choice == car:
            stay_wins += 1
        elif remaining_door == car:
            switch_wins += 1

    # Calculate percentages (avoid division by zero)
    if valid_trials > 0:
        stay_percent = (stay_wins / valid_trials) * 100
        switch_percent = (switch_wins / valid_trials) * 100
    else:
        stay_percent = switch_percent = 0

    return stay_wins, switch_wins, valid_trials, stay_percent, switch_percent

# Run it
if __name__ == "__main__":
    trials = 1_000_000
    stay_wins, switch_wins, valid_trials, stay_percent, switch_percent = simultaneous_monty_trials(trials)
    print(f"Total trials attempted: {trials}")
    print(f"Valid trials: {valid_trials}")
    print(f"Stay wins: {stay_wins} ({stay_percent:.1f}%)")
    print(f"Switch wins: {switch_wins} ({switch_percent:.1f}%)")

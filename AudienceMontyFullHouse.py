import random

def audience_monty_full_trials(num_trials, debug_trials=0):
    player_stay_wins = 0
    player_switch_wins = 0
    aud_any_wins = 0  # Before Monty, any door
    aud_not_player_wins = 0  # Before Monty, not Player's door
    aud_post_player_wins = 0  # After Monty, picks Player's door
    aud_post_remaining_wins = 0  # After Monty, picks remaining door
    aud_post_random_wins = 0  # After Monty, picks randomly
    valid_trials = 0

    for trial in range(num_trials):
        # Set up doors: 0 = car, 1 = goat, 2 = goat
        doors = [0, 1, 2]
        car = random.randint(0, 2)
        doors[car] = 0  # Car
        doors[(car + 1) % 3] = 1  # Goat
        doors[(car + 2) % 3] = 2  # Goat

        # Player guesses
        player_choice = random.randint(0, 2)

        # Audience 1: Any door (before Monty)
        aud_any_choice = random.randint(0, 2)

        # Audience 2: Not Player's door (before Monty)
        other_doors = [d for d in [0, 1, 2] if d != player_choice]
        aud_not_player_choice = random.choice(other_doors)

        # Monty guesses
        monty_choice = random.randint(0, 2)

        # Toss if Monty picks same as Player or reveals car
        if monty_choice == player_choice or monty_choice == car:
            continue

        # Valid trial: Monty revealed a goat, different from Player
        valid_trials += 1
        remaining_door = 3 - (player_choice + monty_choice)  # Third door

        # Audience 3: Picks Player's door (after Monty)
        aud_post_player_choice = player_choice

        # Audience 4: Picks remaining door (after Monty)
        aud_post_remaining_choice = remaining_door

        # Audience 5: Picks randomly (after Monty)
        aud_post_random_choice = random.randint(0, 2)

        # Debug: Print first few valid trials
        if debug_trials > 0 and valid_trials <= debug_trials:
            print(f"Trial {valid_trials}: Car={car}, Player={player_choice}, Monty={monty_choice}, "
                  f"Remaining={remaining_door}, Aud1={aud_any_choice}, Aud2={aud_not_player_choice}, "
                  f"Aud3={aud_post_player_choice}, Aud4={aud_post_remaining_choice}, Aud5={aud_post_random_choice}")

        # Player outcomes
        if player_choice == car:
            player_stay_wins += 1
        elif remaining_door == car:
            player_switch_wins += 1

        # Audience 1: Any door (pre-Monty)
        if aud_any_choice == car:
            aud_any_wins += 1

        # Audience 2: Not Player's door (pre-Monty)
        if aud_not_player_choice == car:
            aud_not_player_wins += 1

        # Audience 3: Player's door (post-Monty)
        if aud_post_player_choice == car:
            aud_post_player_wins += 1

        # Audience 4: Remaining door (post-Monty)
        if aud_post_remaining_choice == car:
            aud_post_remaining_wins += 1

        # Audience 5: Random (post-Monty)
        if aud_post_random_choice == car:
            aud_post_random_wins += 1

    # Percentages
    if valid_trials > 0:
        stay_percent = (player_stay_wins / valid_trials) * 100
        switch_percent = (player_switch_wins / valid_trials) * 100
        aud_any_percent = (aud_any_wins / valid_trials) * 100
        aud_not_player_percent = (aud_not_player_wins / valid_trials) * 100
        aud_post_player_percent = (aud_post_player_wins / valid_trials) * 100
        aud_post_remaining_percent = (aud_post_remaining_wins / valid_trials) * 100
        aud_post_random_percent = (aud_post_random_wins / valid_trials) * 100
    else:
        stay_percent = switch_percent = aud_any_percent = aud_not_player_percent = 0
        aud_post_player_percent = aud_post_remaining_percent = aud_post_random_percent = 0

    return (player_stay_wins, player_switch_wins, aud_any_wins, aud_not_player_wins,
            aud_post_player_wins, aud_post_remaining_wins, aud_post_random_wins,
            valid_trials, stay_percent, switch_percent, aud_any_percent, aud_not_player_percent,
            aud_post_player_percent, aud_post_remaining_percent, aud_post_random_percent)

# Run it
if __name__ == "__main__":
    trials = 1_000_000
    debug_trials = 5  # Print first 5 valid trials
    (stay_wins, switch_wins, aud_any_wins, aud_not_player_wins,
     aud_post_player_wins, aud_post_remaining_wins, aud_post_random_wins,
     valid_trials, stay_percent, switch_percent, aud_any_percent, aud_not_player_percent,
     aud_post_player_percent, aud_post_remaining_percent, aud_post_random_percent) = audience_monty_full_trials(trials, debug_trials)
    print(f"\nTotal trials attempted: {trials}")
    print(f"Valid trials: {valid_trials}")
    print(f"Player Stay wins: {stay_wins} ({stay_percent:.1f}%)")
    print(f"Player Switch wins: {switch_wins} ({switch_percent:.1f}%)")
    print(f"Audience (Any Door, Pre-Monty) wins: {aud_any_wins} ({aud_any_percent:.1f}%)")
    print(f"Audience (Not Player's Door, Pre-Monty) wins: {aud_not_player_wins} ({aud_not_player_percent:.1f}%)")
    print(f"Audience (Player's Door, Post-Monty) wins: {aud_post_player_wins} ({aud_post_player_percent:.1f}%)")
    print(f"Audience (Remaining Door, Post-Monty) wins: {aud_post_remaining_wins} ({aud_post_remaining_percent:.1f}%)")
    print(f"Audience (Random, Post-Monty) wins: {aud_post_random_wins} ({aud_post_random_percent:.1f}%)")

import random

def audience_monty_full_trials(num_trials, debug_trials=0):
    player_stay_wins = 0
    player_switch_wins = 0
    aud_any_wins = 0
    aud_not_player_wins = 0
    aud_post_player_wins = 0
    aud_post_remaining_wins = 0
    aud_post_random_wins = 0
    valid_trials = 0

    for trial in range(num_trials):
        car = random.randint(0, 2)
        player_choice = random.randint(0, 2)
        aud_any_choice = random.randint(0, 2)
        other_doors = [d for d in [0, 1, 2] if d != player_choice]
        aud_not_player_choice = random.choice(other_doors)
        monty_choice = random.randint(0, 2)

        if monty_choice == player_choice or monty_choice == car:
            continue

        valid_trials += 1
        remaining_door = 3 - (player_choice + monty_choice)

        aud_post_player_choice = player_choice
        aud_post_remaining_choice = remaining_door
        # Fix Aud 5: Pick from remaining 2 doors, not 3
        aud_post_random_choice = random.choice([player_choice, remaining_door])

        if debug_trials > 0 and valid_trials <= debug_trials:
            print(f"Trial {valid_trials}: Car={car}, Player={player_choice}, Monty={monty_choice}, "
                  f"Remaining={remaining_door}, Aud1={aud_any_choice}, Aud2={aud_not_player_choice}, "
                  f"Aud3={aud_post_player_choice}, Aud4={aud_post_remaining_choice}, Aud5={aud_post_random_choice}")

        if player_choice == car:
            player_stay_wins += 1
        elif remaining_door == car:
            player_switch_wins += 1
        if aud_any_choice == car:
            aud_any_wins += 1
        if aud_not_player_choice == car:
            aud_not_player_wins += 1
        if aud_post_player_choice == car:
            aud_post_player_wins += 1
        if aud_post_remaining_choice == car:
            aud_post_remaining_wins += 1
        if aud_post_random_choice == car:
            aud_post_random_wins += 1

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

if __name__ == "__main__":
    trials = 1_000_000
    debug_trials = 5
    (stay_wins, switch_wins, aud_any_wins, aud_not_player_wins,
     aud_post_player_wins, aud_post_remaining_wins, aud_post_random_wins,
     valid_trials, stay_percent, switch_percent, aud_any_percent, aud_not_player_percent,
     aud_post_player_percent, aud_post_remaining_percent, aud_post_random_percent) = audience_monty_full_trials(trials, debug_trials)
    print(f"\nTotal trials attempted: {trials}")
    print(f"Valid trials: {valid_trials}")
    print(f"Player Stay wins: {stay_wins} ({stay_percent:.1f}%)")
    print(f"Player Switch wins: {stay_wins} ({switch_percent:.1f}%)")
    print(f"Audience (Any Door, Pre-Monty) wins: {aud_any_wins} ({aud_any_percent:.1f}%)")
    print(f"Audience (Not Player's Door, Pre-Monty) wins: {aud_not_player_wins} ({aud_not_player_percent:.1f}%)")
    print(f"Audience (Player's Door, Post-Monty) wins: {aud_post_player_wins} ({aud_post_player_percent:.1f}%)")
    print(f"Audience (Remaining Door, Post-Monty) wins: {aud_post_remaining_wins} ({aud_post_remaining_percent:.1f}%)")
    print(f"Audience (Random, Post-Monty) wins: {aud_post_random_wins} ({aud_post_random_percent:.1f}%)")

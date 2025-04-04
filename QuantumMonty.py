import random

def monty_hall_trial(monty_knowledgeable=True, player_intent=False, log_file=None):
    doors = [0, 0, 1]  # 0 = goat, 1 = car
    random.shuffle(doors)
    player_choice = 0  # Always picks door 1 (index 0)
    
    if monty_knowledgeable:
        available_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
        monty_reveal = random.choice(available_doors)
    else:
        other_doors = [i for i in range(3) if i != player_choice]
        monty_reveal = random.choice(other_doors)
        if doors[monty_reveal] == 1:
            # Log discarded trial
            if log_file:
                log_file.write(f"Random Monty, Doors: {doors}, Player: {player_choice}, Monty Reveal: {monty_reveal} (car), Discarded\n")
            return None
    
    switch_choice = [i for i in range(3) if i != player_choice and i != monty_reveal][0]
    win = 1 if doors[switch_choice] == 1 else 0
    
    # Intent tweak (1% flip chance)
    if player_intent and random.random() < 0.01:
        win = 1 - win
    
    # Log the trial
    if log_file:
        intent_str = "Yes" if player_intent else "No"
        result_str = "Win" if win else "Lose"
        log_file.write(f"{'Knowledgeable' if monty_knowledgeable else 'Random'} Monty, Doors: {doors}, Player: {player_choice}, Monty Reveal: {monty_reveal}, Switch: {switch_choice}, Intent: {intent_str}, Result: {result_str}\n")
    
    return win

def run_simulations(num_trials=1000000):
    # Open log file
    with open("monty_hall_log.txt", "w") as log_file:
        log_file.write("Monty Hall Quantum Experiment Log\n")
        log_file.write(f"Trials per condition: {num_trials}\n\n")
        
        # Knowledgeable Monty
        k_wins = 0
        log_file.write("=== Knowledgeable Monty Trials ===\n")
        for _ in range(num_trials):
            result = monty_hall_trial(monty_knowledgeable=True, player_intent=random.choice([True, False]), log_file=log_file)
            k_wins += result
        
        # Random Monty
        r_wins = 0
        valid_trials = 0
        log_file.write("\n=== Random Monty Trials ===\n")
        while valid_trials < num_trials:
            result = monty_hall_trial(monty_knowledgeable=False, player_intent=random.choice([True, False]), log_file=log_file)
            if result is not None:
                r_wins += result
                valid_trials += 1
        
        # Summary
        k_rate = k_wins / num_trials * 100
        r_rate = r_wins / num_trials * 100
        log_file.write(f"\n=== Summary ===\n")
        log_file.write(f"Knowledgeable Monty Switch Win Rate: {k_rate:.2f}%\n")
        log_file.write(f"Random Monty Switch Win Rate: {r_rate:.2f}%\n")
    
    return k_rate, r_rate

# Run it
random.seed()
print("Running 1M trials per condition... this might take a sec.")
k_rate, r_rate = run_simulations()
print(f"Knowledgeable Monty: Switch win rate = {k_rate:.2f}%")
print(f"Random Monty: Switch win rate = {r_rate:.2f}%")
print("Check 'monty_hall_log.txt' for the full verbose log!")

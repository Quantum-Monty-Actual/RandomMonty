import random

def monty_hall_trial(monty_knowledgeable=True, log_file=None):
    doors = [0, 0, 1]
    random.shuffle(doors)
    player_choice = 0
    
    if monty_knowledgeable:
        available_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
        monty_reveal = random.choice(available_doors)
    else:
        other_doors = [i for i in range(3) if i != player_choice]
        monty_reveal = random.choice(other_doors)
        if doors[monty_reveal] == 1:
            if log_file:
                log_file.write(f"Random Monty, Doors: {doors}, Player: {player_choice}, Monty Reveal: {monty_reveal} (car), Discarded\n")
            return None
    
    switch_choice = [i for i in range(3) if i != player_choice and i != monty_reveal][0]
    win = 1 if doors[switch_choice] == 1 else 0
    
    if log_file:
        result_str = "Win" if win else "Lose"
        log_file.write(f"{'Knowledgeable' if monty_knowledgeable else 'Random'} Monty, Doors: {doors}, Player: {player_choice}, Monty Reveal: {monty_reveal}, Switch: {switch_choice}, Result: {result_str}\n")
    
    return win

def run_simulations(num_trials=1000000):
    with open("monty_hall_log.txt", "w") as log_file:
        log_file.write("Monty Hall Experiment Log\n")
        log_file.write(f"Trials per condition: {num_trials}\n\n")
        
        k_wins = 0
        log_file.write("=== Knowledgeable Monty Trials ===\n")
        for _ in range(num_trials):
            result = monty_hall_trial(monty_knowledgeable=True, log_file=log_file)
            k_wins += result
        
        r_wins = 0
        valid_trials = 0
        log_file.write("\n=== Random Monty Trials ===\n")
        while valid_trials < num_trials:
            result = monty_hall_trial(monty_knowledgeable=False, log_file=log_file)
            if result is not None:
                r_wins += result
                valid_trials += 1
        
        k_rate = k_wins / num_trials * 100
        r_rate = r_wins / num_trials * 100
        log_file.write(f"\n=== Summary ===\n")
        log_file.write(f"Knowledgeable Monty Switch Win Rate: {k_rate:.2f}%\n")
        log_file.write(f"Random Monty Switch Win Rate: {r_rate:.2f}%\n")
    
    return k_rate, r_rate

random.seed()
print("Running 1M trials per condition...")
k_rate, r_rate = run_simulations()
print(f"Knowledgeable Monty: Switch win rate = {k_rate:.2f}%")
print(f"Random Monty: Switch win rate = {r_rate:.2f}%")
print("Check 'monty_hall_log.txt' for the full log!")

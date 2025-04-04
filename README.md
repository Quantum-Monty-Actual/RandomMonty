Blind Monty: My White Whale

Monty Hall’s a classic: three doors, one car, two goats. Pick a door, Monty—who knows where the car is—reveals a goat, and switching wins 2/3 of the time. It’s clean, counterintuitive, and stats gospel. But what if Monty doesn’t know? That’s been my white whale—a simple question with a big answer. This repo tests it: a mechanically identical setup, but Monty guesses blind. The results? The 2/3 advantage dies, and something weirder pops up.
What’s Here

Three Python scripts tweak Monty Hall by making Monty ignorant:

    RandomMonty.py: Player picks, Monty guesses a door randomly, tosses trials where he reveals the car. One question: stay or switch?
    SameTimeMonty.py: Player and Monty guess simultaneously, tossing same-door picks or car reveals. Same deal—stay or switch?
    AudienceMontyFullHouse.py: Player picks, two audience members guess pre-Monty (one any door, one not Player’s door), Monty guesses, then three more guess post-reveal (Player’s door, remaining door, random). Who finds the car?

No dependencies, just Python 3. Runs 1M trials in seconds—even on a 14-year-old laptop.
The Results

    Player Odds: Across all scripts, it’s 50/50—stay wins half, switch wins half. Blind Monty kills the classic 2/3 switch edge. Why? His ignorance flattens the probability—no clever redistribution, just a coin flip between your door and the other.
    Audience (Any Door, Pre-Monty): 33.4%. Blind guess from three doors, unaffected by Monty’s filter. Expected.
    Audience (Not Player’s Door, Pre-Monty): 25.0%. Here’s the weird one—picks from two doors (not Player’s), should be >33%, but the filter (tossing car reveals) drags it down. A quirk worth digging into.
    Audience (Post-Monty): All three—Player’s door (50.0%), Remaining door (50.0%), Random from the two (50.0%)—match Player’s odds. Seeing Monty’s goat reveal locks them into the 50/50 reality.

Check the outputs in each script—1M trials each, tight margins.
How to Run

Clone it, cd in, and:

    python3 RandomMonty.py
    python3 SameTimeMonty.py
    python3 AudienceMontyFullHouse.py

No setup, no fuss. Tweak num_trials if you want more (or less) runs.
Why It Matters

Classic Monty Hall leans on Monty’s omniscience—strip that, and the game shifts. These scripts prove it: 50/50 isn’t just a fluke, it’s the rule when Monty’s blind. That 25% anomaly? It’s not a bug—it’s a signal. Pre-Monty guesses get tangled in the filter, post-Monty ones ride the resolved odds. Stats says one thing, causality another—maybe there’s more under the hood.
Dig In

The code’s simple—fork it, break it, fix it. Got an idea? Run it. That 25% bugging you? Explain it. This isn’t about rewriting textbooks—it’s about asking what happens when you pull one thread.

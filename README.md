# RandomMonty
My personal white whale

This Python script tests a variation on the Monty Hall problem, exploring if Monty’s knowledge state affects switch odds beyond classical probability. Standard setup predicts a 2/3 win rate (~66.7%) for switching. Does intent—or lack of it—change that?

Setup: 1M trials each: Knowledgeable Monty (knows car location, reveals a goat) vs. Random Monty (picks randomly, discards car reveals). Player always switches.

Hypothesis: Random Monty’s lack of knowledge might alter odds, possibly via retrocausality or observer effects.

Results: Knowledgeable Monty: 66.48% (expected). Random Monty: 50.01% (near 50/50, not 66.7%). Anomaly or error?

Code’s simple, log’s verbose—every trial’s recorded. Open for replication, critique, or expansion.

How to Run:

python3 QuantumMonty.py
Outputs win rates + monty_hall_log.txt (2.5M+ lines of trial details).

Purpose:

Unexplored angle on a classic problem. Null or not, it’s a data point. Run it, test it, dig deeper.

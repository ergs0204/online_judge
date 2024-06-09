def baseball_game_scoring(input_data):
    bases = [0, 0, 0]  # Represents the three bases, not including home.
    score = 0
    outs = 0
    player = 0  # Index of the current player.
    hits = input_data[:-1]  # All the hits except the last line which is the out limit.
    out_limit = int(input_data[-1][0])  # The number of outs to simulate until.

    for hit in hits:
        hit_info = hit.split()[1:]  # Skip the first number which is the number of hits.
        for h in hit_info:
            if h in ['FO', 'GO', 'SO']:  # Check if the hit is an out.
                outs += 1
                if outs == out_limit:
                    return score
            else:  # It's a hit, so move the players.
                hit_base = int(h[0])  # Number of bases to move.
                bases = [1] + bases  # The hitter is on the first base.
                for _ in range(hit_base):
                    score += bases.pop()  # Add the player on the third base to the score if there is one.
                    bases.insert(0, 0)  # Add an empty base at the start.
    return score

# Example inputs and outputs from the problem statement
inputs = [
    ["5 1B 1B FO GO 1B", "5 1B 2B FO FO SO", "4 SO HR SO 1B", "4 FO FO FO HR", "4 1B 1B 1B 1B", "4 GO GO 3B GO", "4 1B GO GO SO", "4 SO GO 2B 2B", "4 3B GO GO FO", "3"],
    ["5 1B 1B FO GO 1B", "5 1B 2B FO FO SO", "4 SO HR SO 1B", "4 FO FO FO HR", "4 1B 1B 1B 1B", "4 GO GO 3B GO", "4 1B GO GO SO", "4 SO GO 2B 2B", "4 3B GO GO FO", "6"]
]

outputs = [0, 5]

# Test the function with the example inputs
for i, input_data in enumerate(inputs):
    result = baseball_game_scoring(input_data)
    assert result == outputs[i], f"Test case {i+1} failed: expected {outputs[i]}, got {result}"
    print(f"Test case {i+1} passed: expected {outputs[i]}, got {result}")
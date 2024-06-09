def simulate_baseball_game(batting_results, total_outs):
    score = 0
    outs = 0
    bases = [0, 0, 0]  # Represents first, second, and third base
    player_index = 0  # Start with the first player

    while outs < total_outs:
        for hit in batting_results[player_index]:
            if hit == "SO" or hit == "FO" or hit == "GO":
                outs += 1
                if outs == total_outs:
                    break
            else:
                # Move runners based on the hit
                if hit == "1B":
                    score += bases[2]
                    bases = [1, bases[0], bases[1]]
                elif hit == "2B":
                    score += bases[2] + bases[1]
                    bases = [0, 1, bases[0]]
                elif hit == "3B":
                    score += sum(bases)
                    bases = [0, 0, 1]
                elif hit == "HR":
                    score += 1 + sum(bases)
                    bases = [0, 0, 0]

            if outs % 3 == 0 and outs != 0:
                # Clear bases after every three outs
                bases = [0, 0, 0]

        player_index = (player_index + 1) % 9  # Move to the next player

    return score

# Input processing
batting_results = []
for _ in range(9):
    player_data = input().split()[1:]  # Skip the first number
    batting_results.append(player_data)
total_outs = int(input())

# Calculate and print the score
print(simulate_baseball_game(batting_results, total_outs))

# Test the function with example input
# example_input_1 = [
#     "5 1B 1B FO GO 1B",
#     "5 1B 2B FO FO SO",
#     "4 SO HR SO 1B",
#     "4 FO FO FO HR",
#     "4 1B 1B 1B 1B",
#     "4 GO GO 3B GO",
#     "4 1B GO GO SO",
#     "4 SO GO 2B 2B",
#     "4 3B GO GO FO",
#     "3"
# ]

# example_input_2 = [
#     "5 1B 1B FO GO 1B",
#     "5 1B 2B FO FO SO",
#     "4 SO HR SO 1B",
#     "4 FO FO FO HR",
#     "4 1B 1B 1B 1B",
#     "4 GO GO 3B GO",
#     "4 1B GO GO SO",
#     "4 SO GO 2B 2B",
#     "4 3B GO GO FO",
#     "6"
# ]

# print(baseball_game_scoring(example_input_1))  # Expected output: 0
# print(baseball_game_scoring(example_input_2))  # Expected output: 5
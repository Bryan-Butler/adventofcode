dial_turns = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("input.txt")]
dial = 50
numb_of_zeros = 0

for turn in dial_turns:
    dial = (dial + turn) % 100
    if dial == 0: numb_of_zeros += 1
print(numb_of_zeros)
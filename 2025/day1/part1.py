instructions = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("input.txt")]
dial = 50
count = 0

for turn in instructions:
    dial = (dial + turn) % 100
    if dial == 0: count += 1

print(count)
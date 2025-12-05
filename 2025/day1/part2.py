dial_turns = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("input.txt")]
dial = 50
numb_of_zeros = 0

for turn in dial_turns:
    if turn < 0:
        div, mod = divmod(turn, -100)
        numb_of_zeros += div
        if dial != 0 and dial + mod <= 0:
            numb_of_zeros += 1
    else:
        div, mod = divmod(turn, 100)
        numb_of_zeros += div
        if dial + mod >= 100:
            numb_of_zeros += 1
    dial = (dial + turn) % 100
print(numb_of_zeros)
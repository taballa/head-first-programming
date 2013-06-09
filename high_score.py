result_f = open("results.txt")

high_score = 0

for line in result_f:
    if float(line) > high_score:
        high_score = float(line)

result_f.close()

print("The highest score was: " + str(high_score))

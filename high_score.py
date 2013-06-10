result_f = open("results.txt")

high_score = 0
scores = []

for line in result_f:
    (name, score) = line.split()
    score = float(score)
    scores.append(score)
    if score > high_score:
        high_score = score

result_f.close()
# scores.sort()
# scores.reverse()
scores.sort(reverse = True)

print("The highest score was: " + str(high_score))
print(scores[0])
print(scores[1])
print(scores[2])

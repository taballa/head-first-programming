result_f = open("results.txt")
result_surfing = open('surfing_data.csv')

high_score = 0
scores = []
hash_scores = {}

for line in result_f:
    (name, score) = line.split()
    score = float(score)
    scores.append(score)
    hash_scores[score] = name
    if score > high_score:
        high_score = score

result_f.close()
# scores.sort()
# scores.reverse()
scores.sort(reverse = True)

for each_score in sorted(hash_scores.keys(), reverse = True):
    print('Surfer ' + hash_scores[each_score] + ' scored ' + str(each_score))

print("The highest score was: " + str(high_score))
print(scores[0])
print(scores[1])
print(scores[2])

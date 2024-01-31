hole1_score = 5
hole1_handi = 2

hole2_score = 6
hole2_handi = 3

hole3_score = 7
hole3_handi = 1

handicap = 2

test_data = [(hole1_handi, hole1_score, "hole1"), (hole2_handi, hole2_score, "hole2"), (hole3_handi, hole3_score, "hole3")]
print(test_data)
test_data = sorted(test_data, key=lambda tuple: tuple[0])
print(test_data)

gross_score = hole1_score + hole2_score + hole3_score

# walk through data one hole at a time, subtracting one from score until handicap runs out

while handicap > 0:
    for i in range(0, len(test_data)-1):
        test_data[i] = (test_data[i][0], test_data[i][1]-1, test_data[i][2])
        handicap -= 1

print(test_data)


import functools

with open("inputs/day7.txt") as file:
	puzzle = file.read().strip()


labels1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
labels2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
hands = {record.split()[0]: int(record.split()[1]) for record in puzzle.split("\n")}


# Part one
def ordering1(hand1, hand2):
	t1 = get_type(hand1)
	t2 = get_type(hand2)
	if t1 == t2:
		for card1, card2 in zip(hand1, hand2):
			if labels1.index(card1) < labels1.index(card2):
				return 1
			elif labels1.index(card1) > labels1.index(card2):
				return -1
		return 0
	
	if t1 > t2:
		return 1
	elif t1 < t2:
		return -1
	else:
		return 0


def get_type(hand):
	s = list(set(hand))
	ls = len(s)
	if ls == 1:
		return 6
	elif ls == 2 and any([hand.count(c) == 4 for c in hand]):
		return 5
	elif ls == 2 and all([hand.count(c) in [2,3] for c in hand]):
		return 4
	elif ls == 3 and all([hand.count(c) in [1,3] for c in hand]):
		return 3
	elif ls == 3 and sum([hand.count(c) == 2 for c in s]) == 2:
		return 2
	elif ls == 4 and sum([hand.count(c) == 2 for c in s]) == 1:
		return 1
	elif ls == 5:
		return 0


sorted_ = sorted(hands, key=functools.cmp_to_key(ordering1))
result = 0
for i, hand in enumerate(sorted_, 1):
	result += (i * hands[hand])
print("Part one:", result)


# Part two
def get_type2(hand):
	if "J" in hand:
		h = hand.replace("J", "")
		if h == "": # hand -> "JJJJJ" (best pretend is "AAAAA")
			return get_type("AAAAA")
		pretend_as = sorted(h, key=hand.count)[-1]
		return get_type(hand.replace("J", pretend_as))
	return get_type(hand)


def ordering2(hand1, hand2):
	t1 = get_type2(hand1)
	t2 = get_type2(hand2)
	if t1 == t2:
		for card1, card2 in zip(hand1, hand2):
			if labels2.index(card1) < labels2.index(card2):
				return 1
			elif labels2.index(card1) > labels2.index(card2):
				return -1
		return 0
	
	if t1 > t2:
		return 1
	elif t1 < t2:
		return -1
	else:
		return 0


sorted_ = sorted(hands, key=functools.cmp_to_key(ordering2))
result = 0
for i, hand in enumerate(sorted_, 1):
	result += (i * hands[hand])

print("Part two:", result)
def change(target, coins_available, coins_so_far):
    if sum(coins_so_far) == target:
        yield coins_so_far
    elif sum(coins_so_far) > target:
        pass
    elif coins_available == []:
        pass
    else:
        for c in change(target, coins_available[:], coins_so_far + [coins_available[0]]):
            yield c
        for c in change(target, coins_available[1:], coins_so_far):
            yield c


import itertools
solutions = 0
for s in change(20, [1,2,3], []):
    solutions += len(list(set(itertools.permutations(s))))

print(solutions)

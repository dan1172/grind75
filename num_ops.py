from itertools import permutations, product

def can_reach(cards, target):
    operations = ['+', '-', '*']
    
    new = [int(n) for n in nums]
    
    for card_permutation in permutations(cards):
        for ops in product(operations, repeat=4):
            expression = f"(({card_permutation[0]}{ops[0]}{card_permutation[1]}){ops[1]}{card_permutation[2]}){ops[2]}{card_permutation[3]}{ops[3]}{card_permutation[4]}"
            if eval(expression) == target:
                return "YES"
    return "NO"

# Example usage
# cards = [40, 1, 3, 4, 20]
cards = [1,1,1,1,1]
print(can_reach(cards, 7))
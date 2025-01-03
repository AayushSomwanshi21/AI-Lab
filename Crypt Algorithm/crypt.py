import itertools


def get_values(word, substitution):

    s = 0
    factor = 1

    for letter in reversed(word):
        s += factor*substitution[letter]
        factor *= 10
    return s


def solve(equation: str):

    left, right = equation.lower().replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    for word in left:
        for let in word:
            letters.add(let)

    # extracting all the unique letters from the left and right part
    letters = list(letters)

    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):

        # assigns number generated by permutation to the letters
        sol = dict(zip(letters, perm))

        if sum(get_values(word, sol) for word in left) == get_values(right, sol):

            left_values = '+'.join(str(get_values(word, sol)) for word in left)
            right_value = get_values(right, sol)
            mapping = sol
            print(f"{left_values} = {right_value} (mapping : {mapping})")


solve('SEND + MORE = MONEY')

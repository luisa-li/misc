def lem(num_cups_sold: int) -> int:
    """ Calculates total profit from selling lemonade by purchasing 16oz bottles of lemonade. """
    num_bottles_required = (num_cups_sold + 3) // 4
    price_per_bottle = 2
    revenue_per_cup = 1

    return num_cups_sold * revenue_per_cup - num_bottles_required * price_per_bottle


def lemonade_stand_2(num_cups_sold: int) -> float:
    """ Calculates total profit from selling lemonade by purchasing 640oz bottles of lemonade. """
    price_per_bottle = 20
    revenue_per_cup = 0.75
    max_num_cups = 640 // 4
    cups_served = min(num_cups_sold, max_num_cups)

    return cups_served * revenue_per_cup - price_per_bottle


def which_stand_better(num_cups_sold: int) -> int:
    """ Determines which stand, 1 or 2, is more profitable based on cups sold. """
    profit_stand_1 = lem(num_cups_sold)
    profit_stand_2 = lemonade_stand_2(num_cups_sold)

    if profit_stand_1 > profit_stand_2:
        return 1
    elif profit_stand_2 > profit_stand_1:
        return 2
    else:
        return 0


def tick(seconds: int) -> int:
    """ Advances the time by one second. """
    if seconds < 59:
        return seconds + 1
    else:
        return 0


def add_prefix(prefix: str, words: list) -> list:
    """ Adds given prefix to each word. """
    return list(map(lambda word: prefix + word, words))


def remove_odd_length_strings(strings: list) -> list:
    """ Removes strings with odd lengths. """
    return list(filter(lambda s: len(s) % 2 == 0, strings))


def f(x: int) -> int:
    x = x + 20
    return x


def g(y: int) -> None:
    global x
    x = f(y)


if __name__ == "__main__":
    breakpoint()
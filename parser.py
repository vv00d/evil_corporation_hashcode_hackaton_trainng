from collections import defaultdict


def read_file(path: tuple):
    with open(path, "r") as file:
        lines = file.read().splitlines()
    return lines


def parse_string(string: str):
    return tuple(string.split()[1:])


def get_person(lines, number_of_people):
    diapason = number_of_people * 2

    person = (parse_string(lines[diapason - 1]),
              parse_string(lines[diapason])
              )
    return person


def count(ingredients: defaultdict, current_ingredients: tuple[str], positive: bool):
    for ingredient in current_ingredients:
        ingredients[ingredient][0 if positive else 1] += 1


def count_profitability(ingredients: defaultdict, person: tuple[tuple[str], tuple[str]]):
    count(ingredients, person[0], True)
    count(ingredients, person[1], False)


def parse_people(lines: list):
    number_of_people = int(lines[0])
    clients: list[tuple[tuple[str]]] = []
    ingredients = defaultdict(lambda: [0, 0])

    for person_number in range(1, number_of_people + 1):
        person = get_person(lines, person_number)
        count_profitability(ingredients, person)
        clients.append(person)

    return clients, ingredients

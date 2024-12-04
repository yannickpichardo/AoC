import re


### Part 1
def parse_memory(input: str):
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex, input)
    parsed_numbers = [(int(a), int(b)) for a, b in matches]
    return parsed_numbers


def get_multiply_sum(parsed_tuples):
    return sum([a * b for a, b in parsed_tuples])


### Part 2
def parse_memory_extended(input: str):
    regex = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    matches = re.findall(regex, input)
    active = True
    results = []
    for match in matches:
        if match == "do()":
            active = True
        elif match == "don't()":
            active = False
        elif match.startswith("mul") and active:
            match_obj = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", match)
            if match_obj:
                a, b = map(int, match_obj.groups())
            results.append(a * b)
    return sum(results)


if __name__ == "__main__":
    file_path = r"day03input.txt"
    with open(file_path, "r") as file:
        input = file.read()
    # Part 1
    parsed_numbers = parse_memory(input=input)
    part1_result = get_multiply_sum(parsed_numbers)
    print(part1_result)
    # Part 2
    part2_results = parse_memory_extended(input)
    print(part2_results)

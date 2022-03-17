import hashlib


def get_value(secret_key: str, starts_with: str) -> int:
    result = ""
    i = 0
    while not result.startswith(starts_with):
        i += 1
        result = hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()

    return i


if __name__ == "__main__":
    puzzle_input = "iwrupvqb"
    five_zeros_output = get_value(puzzle_input, "00000")
    print(f"{five_zeros_output} is the lowest positive number that starts with 5 zeros")
    six_zeros_output = get_value(puzzle_input, "000000")
    print(f"{six_zeros_output} is the lowest positive number that starts with 6 zeros")

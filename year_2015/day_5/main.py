import re

RE_VOWELS = re.compile(r"[aeiou]", re.IGNORECASE)


def old_rules_is_nice(s: str) -> bool:
    vowels = RE_VOWELS.findall(s)
    if len(vowels) < 3:
        return False

    return any(letter == s[i] for i, letter in enumerate(s[1:])) and all(
        bad_str not in s for bad_str in ["ab", "cd", "pq", "xy"]
    )


def new_rules_is_nice(s: str) -> bool:
    letter_pairs = [s[i] + letter for i, letter in enumerate(s[1:])]

    return any(
        pair in letter_pairs[i + 2 :] for i, pair in enumerate(letter_pairs[:-2])
    ) and any(s[i + 2] == letter for i, letter in enumerate(s[:-2]))


if __name__ == "__main__":
    old_rules_nice_count = 0
    new_rules_nice_count = 0
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            if old_rules_is_nice(line):
                old_rules_nice_count += 1
            if new_rules_is_nice(line):
                new_rules_nice_count += 1
    print(f"{old_rules_nice_count} nice strings with old rules")
    print(f"{new_rules_nice_count} nice strings with new rules")

import itertools
import math


def calculate_wrapping_paper_sq_ft(dimensions: str) -> int:
    l_w_h = [int(dim) for dim in dimensions.split("x")]
    face_dimensions = list(itertools.combinations(l_w_h, 2))
    areas = [length * width for length, width in face_dimensions]
    return sum(areas) * 2 + min(areas)


def calculate_ribbon_ft(dimensions: str) -> int:
    l_w_h = [int(dim) for dim in dimensions.split("x")]
    face_dimensions = list(itertools.combinations(l_w_h, 2))
    perimeters = [(length + width) * 2 for length, width in face_dimensions]
    return math.prod(l_w_h) + min(perimeters)


if __name__ == "__main__":
    wrapping_paper_sq_ft = 0
    ribbon_ft = 0
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            dimensions_ = line.strip()
            wrapping_paper_sq_ft += calculate_wrapping_paper_sq_ft(dimensions_)
            ribbon_ft += calculate_ribbon_ft(dimensions_)
    print(f"Order {wrapping_paper_sq_ft} sq ft of wrapping paper")
    print(f"Order {ribbon_ft} ft of ribbon")

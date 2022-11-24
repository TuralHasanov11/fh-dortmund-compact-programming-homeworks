import math


def area(r: int) -> float:
    return round((r**2) * math.pi, 2)


if __name__ == '__main__':
    radius = int(input("Enter radius of circle: "))
    print(f"Area of circle: {area(r=radius)}")

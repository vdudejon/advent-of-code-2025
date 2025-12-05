with open("input.txt") as f:
    input = [line.strip() for line in f.readlines()]


def rotate(
    position: int,
    move: str,
    password: int,
    method_2: bool = False,
) -> tuple[int, int]:
    # If Right, add to position
    if "R" in move:
        move_int = int(move.strip("R"))
        for _ in range(move_int):
            position += 1
            if position == 100:
                position = 0
            if method_2 and position == 0:
                password += 1

    # If Left, subtract to position
    if "L" in move:
        move_int = int(move.strip("L"))
        for _ in range(move_int):
            position -= 1
            if method_2 and position == 0:
                password += 1
            if position == -1:
                position = 99
    if not method_2 and position == 0:
        password += 1

    return position, password


# Part 1
position: int = 50
password: int = 0
for move in input:
    position, password = rotate(position, move, password, method_2=False)

print(f"The password for method 1 is {password}")

# Part 2
position: int = 50
password: int = 0
for move in input:
    position, password = rotate(position, move, password, method_2=True)

print(f"The password for method 2 is {password}")

# --- Day 1: Secret Entrance ---

DEBUG = True


def run():
    dial = 50
    dial_min, dial_max = 0, 99
    password = 0

    with open("2025/src/01/input.txt", "r") as f:
        lines = [x.strip() for x in f.readlines()]

    if DEBUG:
        print(f"\nThe dial starts by pointing at {dial}.")

    for instruction in lines:
        direction = instruction[0]

        amount = int(instruction[1:])

        if direction == "L":
            dial -= amount
        else:  # "R"
            dial += amount

        # Handle wrapping
        if dial < dial_min:
            dial += 100
        elif dial > dial_max:
            dial -= 100

        if DEBUG:
            print(f"The dial is rotated {instruction} to point at {dial}.")

        # Check for password increment
        if dial == 0:
            password += 1
            if DEBUG:
                print(f"Dial at {dial}, registering occurrence...\n")


    return f"Final password: {password}"


if __name__ == "__main__":
    print(run())

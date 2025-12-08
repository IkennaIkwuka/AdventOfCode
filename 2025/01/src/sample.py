from utils.python import project_path

txtInput = project_path(__file__, "docs", "sample.txt")

with open(txtInput, "r") as f:
    lines = [x.strip() for x in f.readlines()]

start = 0


end = 100


def method():
    point = 50

    for i in lines:
        if i.startswith("L"):
            pointer = point - int(i[1:])
            if pointer < 0:
                pointer = 100 + pointer
                point = pointer
            point = pointer

        if i.startswith("R"):
            pointer = point + int(i[1:])
            point = pointer
            if pointer > 100:
                pointer = pointer - 100
                point = pointer

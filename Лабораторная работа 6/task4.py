import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(INPUT_FILE, "r") as f:
        headers = f.readline().split(",")
        headers[-1] = headers[-1].replace("\n", "")
        data = []
        for line in f:
            line = line.replace("\n", "")
            values = line.split(",")
            data.append(dict(zip(headers, values)))
    return data

    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

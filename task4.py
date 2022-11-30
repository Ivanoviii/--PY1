import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as inp:
        dts = []
        for num, line in enumerate(inp):
            pol = line.strip(new_line).split(delimiter)
            if num == 0:
                zag = pol
                continue
            dts.append({})
            for i, _ in enumerate(zag):
                dts[-1][zag[i]] = pol[i]
    return dts



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
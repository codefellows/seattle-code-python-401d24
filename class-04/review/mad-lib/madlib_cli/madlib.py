def read_template(path):
    """
    takes in a path to a tempate file
    returns the stripped text
    """

    with open(path) as file:
        contents = file.read()
        return contents.strip()


def parse_template(template):
    parts = []
    stripped = ""

    capturing = False
    capture = ""

    for char in template:
        if capturing:
            if char == "}":
                parts.append(capture)
                stripped += char
                capture = ""
                capturing = False
            else:
                capture += char
        else:
            stripped += char

            if char == "{":
                capturing = True

    return stripped, tuple(parts)


def merge(stripped_template, responses):
    return stripped_template.format(*responses)

def main():
     # run the game

    template = read_template("assets/dark_and_stormy_night_template.txt")

    stripped_template, parts = parse_template(template)

    responses = gather_responses(parts)

    # merge once we have the user's responses
    merged = merge(stripped_template, responses)

    print(merged)

    with open("assets/dark_and_stormy_night_completed.txt", "w+") as file:
        file.write(merged)

def gather_responses(parts):

    responses = []

    for part in parts:
        response = input(f"Enter a {part}: ")
        responses.append(response)

    return responses

if __name__ == "__main__":
    # check to see if running as a script
    # if this check is missing then it will mess up pytest
    main()



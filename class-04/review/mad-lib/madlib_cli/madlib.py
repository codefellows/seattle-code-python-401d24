def read_template(path):
  """
  takes in a path to a tempate file
  and returns the stripped text
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

def merge(stripped_template, parts):
    return stripped_template.format(*parts)

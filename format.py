import argparse

parser = argparse.ArgumentParser(description = "Formats some files")
parser.add_argument("file", type = str)
parser.add_argument("output", type = str)
arg = parser.parse_args()

with open(arg.file, "r") as f:
    buf = ""
    for line in f:
        # Detect comment and keep them
        if line.startswith("#"):
            buf += line
            continue
        elif line == "\n":
            continue

        splitl = line.split()
        buf += splitl[0].upper() + "\n"

with open(arg.output, "w") as f:
    f.write(buf)


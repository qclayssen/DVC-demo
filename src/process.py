import sys
in_path, out_path = sys.argv[1:3]
with open(in_path) as f:
    data = f.read()
# simple transform: convert to uppercase
with open(out_path, 'w') as f:
    f.write(data.upper())

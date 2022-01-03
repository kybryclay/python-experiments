table = {
  "000": "0",
  "001": "0",
  "010": "1",
  "011": "1",
  "100": "1",
  "101": "1",
  "110": "0",
  "111": "0",
}

output = {
  "0": "  ",
  "1": "🚼",
}

def tri(n):
  start = "1"
  for row in range(n):
    start = "0" + start + "00"
    yield start
    new = ""
    for i in range(0, len(start) - 2):
      window = start[i:i+3]
      result = table[window]
      new = new + result
    start = new
  
for row in tri(32):
  for letter in row:
    print(output[letter], end="")
  print()
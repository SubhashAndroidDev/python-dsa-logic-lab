text = "abcdefghij"

result = text[1::2]

print(result)

"""
dry run
text = a b c d e f g h i j
index  0 1 2 3 4 5 6 7 8 9

Start = 1
Step  = 2

1 → b
3 → d
5 → f
7 → h
9 → j
"""
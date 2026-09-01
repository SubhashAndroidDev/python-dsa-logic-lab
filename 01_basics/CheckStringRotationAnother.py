s1 = "ABCD"
s2 = "CDAB"

result = s1 + s1

if s2 in result:
    print("Rotation")
else:
    print("Not Rotation")



"""
s1 + s1

"ABCD" + "ABCD"

"ABCDABCD"

"CDAB" in "ABCDABCD"
True
"""    
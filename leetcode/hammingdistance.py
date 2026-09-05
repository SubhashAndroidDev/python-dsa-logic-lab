
"""
Hamming Distance = number of positions where two strings/binary numbers are different.

String 1: 1011101
String 2: 1001001

Compare:
1 = 1 ✅
0 = 0 ✅
1 = 0 ❌
1 = 1 ✅
1 = 0 ❌
0 = 0 ✅
1 = 1 ✅

Hamming Distance = 2
"""
def hamming_distance(s1,s2):
    count=0

    for i in range(len(s1)):
        if  s1[i] !=s2[i]:
            count+=1
    return count


s1="1011101"
s2="1010001"
print(hamming_distance(s1,s2))

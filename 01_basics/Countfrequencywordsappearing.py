def freq_words():
    str=input("Enter a string: ")
    li=str.split()
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print("Frequency of words in the given string is: ", d) 

freq_words()

"""
Enter a string: sheena loves eating apple and mongo . her sister loves eating apple and mongo
Frequency of words in the given string is:  {'sheena': 1, 'loves': 2, 'eating': 2, 'apple': 2, 'and': 2, 'mongo': 2, '.': 1, 'her': 1, 'sister': 1}
"""
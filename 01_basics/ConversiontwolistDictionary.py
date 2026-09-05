def list_to_dict():
    keys=[1,2,3,4]
    values=['a','b','c','d']
    result=dict(zip(keys,values))
    print("Dictionary formed from the two lists is: ", result)

# list_to_dict()    
def dict_to_list():
    d={1:'a',2:'b',3:'c',4:'d'}
    keys=list(d.keys())
    values=list(d.values())
    print("Keys of the dictionary are: ", keys)
    print("Values of the dictionary are: ", values)

dict_to_list() 
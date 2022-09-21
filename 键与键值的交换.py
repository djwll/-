def change_table(dictionary):
    key = list(dictionary)
    keyword= list(dictionary.values())
    dictionary=dict(zip(keyword,key))
    return dictionary
            

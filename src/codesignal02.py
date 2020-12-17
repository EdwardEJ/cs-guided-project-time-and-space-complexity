def csFindAddedLetter(str_1: str, str_2: str) -> str:
    # iterate through str1 and assign to dictionary
    # have each iteration have a counter
    # iterate through str_2
    # for every instance of a matching key, decrease counter by 1
    # resulting key with a value of -1 is the extra key added
    dict = {}
    
    for i in str_1:
      if i in dict:
        dict[i] += 1
      else:
        dict[i] = 1

    for i in str_2:
      if i in dict:
        dict[i] -= 1
      else:
        dict[i] = -1

    for key, value in dict.items(): 
         if -1 == value: 
             return key 


print(csFindAddedLetter('bcde', 'bcdef'))
print(csFindAddedLetter('b', 'bb'))
print(csFindAddedLetter('xqmxtheyvpdqounqmfyaqdqxwe', 'xqmxtheyvpdqounqmfyaqxdqxwe'))
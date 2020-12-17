def csFirstUniqueChar(input_str: str) -> int:
    # dict = {}
    
    # for i in input_str:
    #     if i in dict:
    #         dict[i] += 1
    #     else:
    #         dict[i] = 1

    # print(sorted(dict.items()))
    for i in input_str:
        if input_str.count(i) == 1:
            return input_str.index(i)
   
    return -1

print(csFirstUniqueChar("lambdaschool"))
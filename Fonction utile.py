def dict_to_list(L):
    L_res = []
    
    for i in L:
        for j in i:
            L_res.append(j)
    return L_res

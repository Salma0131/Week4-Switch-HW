def Permutations_String(str):
    if len(str) == 1:
        return str
    if len(str) == 2:
        return [str,str[::-1]]
    else:
        result = []
        for char in str:
            for per in Permutations_String(str.replace(char,"")):
                result.append(char + per)
        return result
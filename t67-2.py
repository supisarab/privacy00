def find_reprated_substrings(s: str) -> list:
    result = {}
    check = []

    for i in range(len(s)):
        for a in range(2 + i, len(s) + 1):
            check.append(s[i:a])
    for a in check:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1
    return [a for a,b in result.items() if b > 1]

print(find_reprated_substrings("banana"))
print(find_reprated_substrings("abcdfg"))
print(find_reprated_substrings("abcabcabc"))
print(find_reprated_substrings("aaaa"))

 #for i in range(len(s)+1):
        #for a in range(2+i, len(s)+1):
            #check.append(s[i:a])
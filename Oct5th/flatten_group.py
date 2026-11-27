def combined(nest):
    return group_by(flatten(nest))


def flatten(nest):
    result = []
    for group in nest:
        if isinstance(group, list):
            result.extend(flatten(group))
        else:
            result.append(group)
    return result

def group_by(words, key_fn = 0):
    dic = {}
    for word in words:
        dic.setdefault(word[key_fn], []).append(word)
    return dic

print(combined([["apple", "avocado"], ["banana"], [["cherry"]]]))

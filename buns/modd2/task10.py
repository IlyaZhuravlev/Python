def new_world_creater(words):
    n_word = ""
    for word in words:
            if len(word) > 0:
                n_word += word[-1]
    return n_word

words = map(str, input().split(' '))
result = new_world_creater(words)
print(result)

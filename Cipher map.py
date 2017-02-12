lst = list()

# def execute(list1, list2):
#     for i, m in zip(list1, list2):
#         for pos, char in enumerate(i):
#             if char == "X":
#                 lst.append(m[pos])
#     return(''.join(lst))

# print("Execute:", execute(('X...', '..X.', 'X..X', '....'), ('itdf', 'gdce', 'aton', 'qrdi')))


def recall_password(cipher_grille, ciphered_password):
    n = 0
    while n < 4:
        for i, m in zip(cipher_grille, ciphered_password):
            for pos, char in enumerate(i):
                if char == "X":
                    lst.append(m[pos])
                # cipher_grille = (list(zip(*cipher_grille[::-1])))
                # print(list(zip(*cipher_grille[::-1])))
        n = n + 1
    return ''.join(lst)

    # n = 0
    # while n < 2:
    #     execute(list(zip(*cipher_grille[::-1])), ciphered_password)
    #     cipher_grille = list(zip(*cipher_grille[::-1]))
    #     n += 1
    # return (''.join(execute(list(zip(*cipher_grille[::-1])), ciphered_password)))

print("Recall:", recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')))


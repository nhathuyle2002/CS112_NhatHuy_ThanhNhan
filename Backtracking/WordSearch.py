table = input()[3:-3].split("\'], [\'")
table = [row.split("\', \'") for row in table]
word = input()

#------------------------------------------#


def solve(table, word, current, i, j, avail):
    if current == len(word):
        return True

    if i < 0 or i >= len(table) or j < 0 or j >= len(table[0]) or\
            avail[i][j] or table[i][j] != word[current]:
        return False

    avail[i][j] = True
    result = solve(table, word, current + 1, i + 1, j, avail) or\
                solve(table, word, current + 1, i - 1, j, avail) or\
                solve(table, word, current + 1, i, j + 1, avail) or\
                solve(table, word, current + 1, i, j - 1, avail)

    avail[i][j] = False
    return result


def check(table, word):
    avail = [[False for j in range(len(table[0]))] for i in range(len(table))]

    for i in range(len(table)):
        for j in range(len(table[0])):
            if solve(table, word, 0, i, j, avail):
                return True

    return False

#------------------------------------------#

if check(table, word) == True:
    print("true")
else:
    print("false")
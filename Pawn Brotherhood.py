def safe_pawns(pawns):

    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        print("real pawns:", row, col)
        pawns_indexes.add((row, col))
    count = 0
    for row, col in pawns_indexes:
        print("indexes:", row, col)
        is_safe = ((row - 1, col -1) in pawns_indexes or (row - 1, col + 1) in pawns_indexes)
        # print(is_safe)
        if is_safe:
            count += 1
            # print(count)
    return count
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

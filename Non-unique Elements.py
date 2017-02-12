lst = [5, 5, 5, 5, 5]
nlst = []
for i in lst:
    if lst.count(i) == 1:
        continue
    else:
        nlst.append(i)
print(nlst)



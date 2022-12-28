if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        l1 = [name, score]
        l.append(l1)
print(l)
l.sort(key=lambda x: x[1])
for list in l:
    # for number in list:
    k = lambda a: a[1]
    print(k(list))

# print(min(l))
str
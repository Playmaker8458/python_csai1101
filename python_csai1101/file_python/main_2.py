n = int(input("Enter you number: "))
a, b, c = 0, 1, 0
total = 0
while c < (2 * n):
    if c % 2 == 1:
        total+=c

    c = a + b
    a = b
    b = c    

print(f"Total = {total}")
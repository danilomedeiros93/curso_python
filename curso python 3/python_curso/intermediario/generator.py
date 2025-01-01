def generator(n=0, maxinum=20):
    while True:
        yield n
        n += 1

        if n >= maxinum:
            return
        

gen = generator(maxinum=200)
for n in gen:
    print(n)
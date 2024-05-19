for i in range(1,6):
    for j in range(i):
        print("*",end='')
    print()

# output will be 
            # *
            # **
            # ***
            # ****
            # *****
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(5,0,-1):
    for j in range(i):
        print("*",end='')
    print()
            # output will be

            # *****
            # ****
            # ***
            # **
            # *

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for i in range(1,6):
    for j in range(i):
        print(i,end='')
    print()

        # output will be
                # 1
                # 22
                # 333
                # 4444
                # 55555

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in range(5,0,-1):
    for j in range(i):
        print(i,end='')
    print()


            # output will be 
                # 55555
                # 4444
                # 333
                # 22
                # 1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

            # output will be 
                    # 1
                    # 12
                    # 123
                    # 1234
                    # 12345

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

    # output will be
                # 12345
                # 1234
                # 123
                # 12
                # 1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

                
for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j,end="")
    print()
        # output will be
            # 1
            # 21
            # 321
            # 4321
            # 54321
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
        # output will be 
        # 54321
        # 4321
        # 321
        # 21
        # 1
)

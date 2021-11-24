try:
    # with open("order.txt") as file:
    #     print(file, type(file))
    #     orders = file.readlines()
    #     for line in orders:
    #         line = line.strip()
    #         print(line)
    #         #print(file.readline())
    # #file.close()
    #
    with open("order.txt") as file:
        orders = file.read().split('\n')


except FileNotFoundError as errmsg: # captures the error message as a variable
    print("The file cannt be found")
    print(errmsg)
    raise
finally: # occurs even if an error is raised
    print("xyz")

with open("tickets.txt", "a") as file:
    for order in orders:
        file.write(f" one {order} coming right up!\n")

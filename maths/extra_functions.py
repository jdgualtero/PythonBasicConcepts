def tables(tableNumber):
    if tableNumber != 0 and tableNumber is not None:
        print("Table of {}".format(tableNumber))
        print()
        for operator in range(1,11):
            result = tableNumber * operator
            print("{} * {} = {}".format(tableNumber,operator,result))

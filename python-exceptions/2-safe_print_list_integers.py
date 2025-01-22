def safe_print_list_integers(my_list=[], x=0):
    if my_list[0] is int:
        try:
            for i in range(x):
                print("{:d}".format(my_list[i]))
            return x
        except:
            return x - 1

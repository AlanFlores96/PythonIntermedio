def run():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    odd = list(filter(lambda x : x%2 != 0, my_list))
    print(odd)


if __name__=="__main__":
    run()
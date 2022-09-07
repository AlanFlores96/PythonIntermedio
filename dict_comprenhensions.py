def run():
    # cubic = {}
    # for i in range(1,101):
    #     cubic.update({i:i**3})
    
    # cubic = {}
    # for i in range(1,101):
    #     if i%3!=0:
    #         cubic[i]=i**3

    cubic = {i: i**3 for i in range(1, 1001) if i%3!=0}

    square = {i : i**(1/2) for i in range(1,1001)}

    for key, value in square.items():
        print(key, "-", value)


if __name__=="__main__":
    run()
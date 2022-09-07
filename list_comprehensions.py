def run():
    # squares = []
    # for i in range(1,101):
    #     squares.append(i**2)
    # print(squares)

    # squares2 = []
    # for i in range(1,100):
    #     if i%3!=0:
    #         squares2.append(i**2)
    # print(squares2)

    squares = [i**2 for i in range(1,101) if i%3 != 0]

    print(squares)

    squares2 = [i for i in range(1, 100000) if i%4==0 and i%6==0 and i%9==0 ]

    print(squares2)

if __name__=="__main__":
    run()
def int_input(x):
    try:
        temp=int(input(x))
    except ValueError:
        print("出错,您输入的不是整数!")
        temp=int_input(x)
    return temp

final=int_input("请输入一个整数：")

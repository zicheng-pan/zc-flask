def logger(function,**outargs):
    def inner(*args, **kargs):
        print("inner...")
        result = function(*args, **kargs)
        print("inner method execute end")
        return result

    return inner


@logger
def test01(*args, **kargs):
    print("this is test method")
    print(str(args))
    print(str(kargs))
    print("this is test method end")


test01(1, 2, argument1="argument1", argument2="argument2")


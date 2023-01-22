import Technology

# 测速一
def Testing_Math() -> bool:
    try:
        print([each for each in Technology.math.PascalTriangle(100)])
        return True
    except BaseException as e:
        print("="*20)
        print(e)
        print("="*20)
        return False
    

# 测速二
def Testing_Password() -> bool:
    try:
        print(Technology.password.Dictionary().Caesar(10, True, True, True))
        print(Technology.password.Decrypt().Fence("OK123"))
        print(Technology.password.Encrypt().Fence("OK123"))
        print(Technology.password.Decrypt().Substitution("OK123", Technology.password.Dictionary().Caesar(10, True, True, True)))
        print(Technology.password.Encrypt().Substitution("OK123", Technology.password.Dictionary().Caesar(10, True, True, True)))
        return True
    except BaseException as e:
        print("="*20)
        print(e)
        print("="*20)
        return False

def Main() -> None:
    Status = [Testing_Math(), Testing_Password()]
    Fail = 0
    for each in Status:
        if each is False:
            Fail += 1
    print("检查完成，共有{}个异常".format(Fail))
    if Fail > 0:
        quit(-1)

if __name__ == "__main__":
    Main()
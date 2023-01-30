def PascalTriangle(limit:int) -> list:
    """
    limit
        sets the limit on the number of output layers.

    Tip: If you need to use an unlimited number of layers, you can use PascalTriangle_Loop function.
    """
    Result = [1]
    for times in range(int(limit)):
        yield Result
        _Product = [1]
        for i in range(0, len(Result)):
            if i + 1 > len(Result) - 1:
                _Product.append(Result[0])
                break
            else:
                _Product.append(Result[i] + Result[i+1])
        Result = _Product

def PascalTriangle_Loop() -> list:
    """
    Warning: This function does not limit the number of layers, please use the for loop traversal with caution
    """
    Result = [1]
    while True:
        yield Result
        _Product = [1]
        for i in range(0, len(Result)):
            if i + 1 > len(Result) - 1:
                _Product.append(Result[0])
                break
            else:
                _Product.append(Result[i] + Result[i+1])
        Result = _Product

# 调试
if __name__ == "__main__":
    pass
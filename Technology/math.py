def PascalTriangle(limit):
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

def PascalTriangle_Loop():
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
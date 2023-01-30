__all__ = ["Time_Master", "Exp"]
import time


def Time_Master(Func):
    def Runner() -> None:
        print("Starting Call The Function")
        _Start = time.time()
        Func()
        _Stop = time.time()
        print(f"FINISH, It used {_Stop-_Start}s")
    return Runner

def Exp(Exponential:int):
    def Exp_of(Number):
        return Number ** Exponential
    return Exp_of

if __name__ == "__main__":
    pass
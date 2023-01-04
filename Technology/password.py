__all__ = ["Dictionary", "Encrypt"]

class Encrypt:
    def __init__(self) -> None:
        self.Mode = ["Strict", "Ignore"]
 
    def Encrypt(self, Text:str, Dictionary:dict, Mode="Strict", Add_Spaces=True) -> str:
        if bool(Add_Spaces):
            Dictionary[" "] = " "
        __Undefined = [Undefined for Undefined in Text if Undefined not in Dictionary]
        _ErrorMessage = "The plaintext entered is empty" if not bool(Text) else "The current pattern does not exist" if Mode not in self.Mode else "The value of the dictionary must be of type dict" if type(Dictionary) is not dict else "Contains characters that are not defined in the dictionary {}{}".format("\n", str( __Undefined)) if bool(__Undefined) and self.Mode.index(Mode) == 0 else None
        if bool(_ErrorMessage):
            raise Exception(_ErrorMessage)
        _ModeType = self.Mode.index(Mode)
        _Password = ""
        _PasswordList = [Dictionary[each] for each in Text] if _ModeType == 0 else [Dictionary[each] for each in Text if each in Dictionary] if _ModeType == 1 else None
        for each in _PasswordList:
            _Password += each

        return _Password

class Dictionary:
    def __init__(self) -> None:
        self.Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.Numbers = "1234567890"


    def Caesar(self, Offset:int, Uppercase=True, Lowercase=False, Number=False, Self_String=None) -> dict:
        """
        Offset
            Sets the number of character offset bits
        Uppercase
            Enables/disables uppercase letters(Enabled by default)
        Lowercase
            Enables/disables lowercase letters(Disabled by default)
        Number
            Enable/disable numbers(Disabled by default)
        Self_String
            Enter your own custom string to generate a dictionary.(Default None)
        
        Note:
            1. When Self_String is enabled, the bool types of Uppercase, Lowercase, and Number will be ignored, and the dictionary will be generated directly using Self_String for the value, so the three ignored data set at this time will be invalid
            2. The offset parameter cannot exceed the number of strings to be generated as a dictionary, otherwise it will self-explode
            3. You cannot set Uppercase, Lowercase and Number at the same time without setting Self_String, that is, there is no string to generate, otherwise it will explode.
        """
        _Upper = self.Uppercase
        _Lower = self.Lowercase
        _Numbers = self.Numbers
        _Offset = int(Offset)
        _StringList = []
        _Dictionary = {}
        _Source = Self_String if bool(Self_String) else (_Upper if bool(Uppercase) else "") + (_Lower if bool(Lowercase) else "") + (_Numbers if bool(Number) else "")
        _ErrorMessage = "The offset data exceeds the limit" if _Offset > len(_Source) else "The offset data exceeds the limit" if _Source is None else False
        if bool(_ErrorMessage):
            raise Exception(_ErrorMessage)
        for each in _Source:
            _StringList.append(each)
        for each in _StringList:
            _Dictionary[each] = _StringList[_StringList.index(each) + _Offset] if _StringList.index(each) + _Offset < len(_StringList) else _StringList[_StringList.index(each) - len(_StringList) + _Offset]
        
        return _Dictionary

# 调试
if __name__ == "__main__":
    pass
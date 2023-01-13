__all__ = ["Dictionary", "Encrypt", "Decrypt"]

class PasswordError(Exception):
    pass

class Password:
    """
    This class is the parent class of all classes in this module, and centrally manages the functions that are called repeatedly
    """
    # 设置配置
    def Set_Config(self) -> None:
        self.Mode = ["Strict", "Ignore", "Retain"]
        self.Ignore = [" ", "\n", "(", ")", ",", ".", "_", ":", "-"]
    # 设置字符
    def Set_Str(self) -> None:
        self.Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.Numbers = "1234567890"
    # 导出未定义的字符
    def Export_Undefined(self, Text:str, Dictionary:dict) -> list:
        return [Undefined for Undefined in Text if Undefined not in Dictionary]
    # 导出错误信息(Encrypt和Decrypt专用)
    def Export_ErrorMessage_Decrypt_Encrypt(self, Text:str, Dictionary, Mode:int, Undefined:list):
        return "The plaintext entered is empty" if not bool(str(Text)) else "The Value of Dictionary is empty" if not bool(Dictionary) else "The current pattern does not exist" if Mode not in self.Mode else "The value of the dictionary must be of type dict" if type(Dictionary) is not dict else "Contains characters that are not defined in the dictionary {}{}".format("\n", str(Undefined)) if bool(Undefined) and self.Mode.index(Mode) == 0 and bool([each for each in Undefined if each not in self.Ignore]) else None
    # 导出错误信息(Dictionary专用)
    def Export_ErrorMessage_Dictionary(self, Offset:int, Source:str):
        return "The offset data exceeds the limit" if Offset > len(Source) else "The offset data exceeds the limit" if Source is None else None
    # 将未定义的字符导出为字典
    def Export_Undefined_Dictionary(self, Undefined:list) -> dict:
        return {each:each for each in Undefined}


class Dictionary(Password):
    def __init__(self) -> None:
        super().Set_Str()


    def Caesar(self, Offset:int, Uppercase:bool=True, Lowercase:bool=False, Number:bool=False, Self_String:str=None) -> dict:
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
        _ErrorMessage = super().Export_ErrorMessage_Dictionary(_Offset, _Source)
        if bool(_ErrorMessage):
            raise PasswordError(_ErrorMessage)
        for each in _Source:
            _StringList.append(each)
        for each in _StringList:
            _Dictionary[each] = _StringList[_StringList.index(each) + _Offset] if _StringList.index(each) + _Offset < len(_StringList) else _StringList[_StringList.index(each) - len(_StringList) + _Offset]
        
        return _Dictionary

class Encrypt(Password):
    def __init__(self) -> None:
        super().Set_Config()
    
 
    def Substitution(self, Text:str, Dictionary:dict, Mode:str="Strict", Add_Ignore:bool=True) -> str:
        """
        Text
            Text that needs to be encrypted
        Dictionary
            Dictionary required for encryption(can be generated using the Dictionary object)
        Mode
            Encrypted mode(Strict by Default), You can view all modes in the Mode property of the object.
        Add_Ignore
            Add characters that need to be ignored in the dictionary, these characters will be preserved (spaces are disabled by default and enabled), and you can modify the value of Ignore to change them

        Mode_Note
            Strict: Include all the characters in plaintext in the dictionary, if they do not, they will self-detonate.
            Ignore: Ignore and discard all characters that are not included in the dictionary.
            Retain: Keep undefined characters (undefined characters are automatically added to the dictionary)
        """
        # 错误检查
        _Undefined = super().Export_Undefined(Text, Dictionary) # 导出未定义的字符
        _ErrorMessage = super().Export_ErrorMessage_Decrypt_Encrypt(Text, Dictionary, Mode, _Undefined)
        if bool(_ErrorMessage):
            raise PasswordError(_ErrorMessage)
        _ModeType = self.Mode.index(Mode) # 将Mode字符转换为整数
        _Password = ""
        # 添加默认忽略字符
        if Add_Ignore:
            Dictionary.update(super().Export_Undefined_Dictionary(self.Ignore))
        if _ModeType == 2 and bool(_Undefined):
            Dictionary.update(super().Export_Undefined_Dictionary(_Undefined)) # Retain模式添加未定义的字符
        _PasswordList = [Dictionary[each] for each in Text] if _ModeType in [0, 2] else [Dictionary[each] for each in Text if each in Dictionary] if _ModeType == 1 else None # 加密
        for each in _PasswordList:
            _Password += each

        return _Password
    
    def RSA(self):
        pass
class Decrypt(Password):
    def __init__(self) -> None:
        super().Set_Config()
    
    def Substitution(self, Password:str, Dictionary:dict, Mode:str="Strict", Add_Ignore:bool=True) -> str:
        """
        Text
            Text that needs to be decrypted
        Dictionary
            Dictionary required for decryption(can be generated using the Dictionary object)
        Mode
            Decrypted mode(Strict by Default), You can view all modes in the Mode property of the object.
        Add_Ignore
            Add characters that need to be ignored in the dictionary, these characters will be preserved (spaces are disabled by default and enabled), and you can modify the value of Ignore to change them

        Mode_Note
            Strict: Include all the characters in plaintext in the dictionary, if they do not, they will self-detonate.
            Ignore: Ignore and discard all characters that are not included in the dictionary.
            Retain: Keep undefined characters (undefined characters are automatically added to the dictionary)
        """
        Dictionary = {Value:Key for Key, Value in Dictionary.items()}
        _Undefined = super().Export_Undefined(Password, Dictionary)
        _ModeType = self.Mode.index(Mode) # 将Mode字符转换为整数
        _ErrorMessage = super().Export_ErrorMessage_Decrypt_Encrypt(Password, Dictionary, Mode, _Undefined)
        if bool(_ErrorMessage):
            raise PasswordError(_ErrorMessage)
        _Text = ""
        if Add_Ignore:
            Dictionary.update(super().Export_Undefined_Dictionary(self.Ignore))
        if _ModeType == 2 and bool(_Undefined):
            Dictionary.update(super().Export_Undefined_Dictionary(_Undefined)) # Retain模式添加未定义的字符
        _TextList = [Dictionary[each] for each in Password] if _ModeType in [0, 2] else [Dictionary[each] for each in Password if each in Dictionary] if _ModeType == 1 else None # 加密
        # 将列表转换成字符
        for each in _TextList:
            _Text += each
        
        return _Text
# 调试
if __name__ == "__main__":
    pass
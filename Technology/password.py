import base64
from abc import ABCMeta, abstractmethod

__all__ = ["Dictionary", "Encrypt", "Decrypt"]

# 自定义错误
class PasswordError(Exception):
    """
    Base class for all custom errors in this module
    """
    pass
class EncryptError(PasswordError):
    """
    Errors encountered during encryption
    """
    pass
class DecryptError(PasswordError):
    """
    Errors encountered during decryption
    """
    pass

class Password(metaclass=ABCMeta):
    """
    This class is the parent class of all classes in this module, and centrally manages the functions that are called repeatedly
    """
    # 初始化
    ErrorMessageList = {
        "Empty":["The plaintext entered is empty", "The Value of Dictionary is empty"],
        "Index":["The offset data exceeds the limit", "The offset data exceeds the limit"],
        "Exist":["The current pattern does not exist", "The value of the dictionary must be of type dict", "Contains characters that are not defined in the dictionary"],
        "Type":["The type of the value must be a string"]}
    @abstractmethod
    def __init__(self) -> None:
        self.Mode = ["Strict", "Ignore", "Retain"]
        self.Ignore = [" ", "\n", "(", ")", ",", ".", "_", ":", "-"]
        self.Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.Numbers = "1234567890"
    # 导出未定义的字符
    def Export_Undefined(self, Text:str, Dictionary:dict) -> list:
        return [Undefined for Undefined in Text if Undefined not in Dictionary not in self.Ignore]
    # 导出错误信息(Encrypt和Decrypt的Substitution专用)
    def Export_ErrorMessage_Decrypt_Encrypt(self, Text:str, Dictionary, Mode:int, Undefined:list) -> str:
        return self.ErrorMessageList["Type"][0] if not type(Text) is str else self.ErrorMessageList["Empty"][0] if not bool(str(Text)) else self.ErrorMessageList["Empty"][1] if not bool(Dictionary) else self.ErrorMessageList["Exist"][0] if Mode not in self.Mode else self.ErrorMessageList["Exist"][1] if type(Dictionary) is not dict else "{}{}{}".format(self.ErrorMessageList["Exist"][2] ,"\n", str(Undefined)) if bool(Undefined) and self.Mode.index(Mode) == 0 else None
    # 导出错误信息(Encrypt和Decrypt的Fence专用)
    def Export_ErrorMessage_Fence(self, Text:str) -> str:
        return  self.ErrorMessageList["Type"][0] if not type(Text) is str else self.ErrorMessageList["Empty"][0] if not bool(Text) else None
    # 导出错误信息(Dictionary专用)
    def Export_ErrorMessage_Dictionary(self, Offset:int, Source:str) -> str:
        return self.ErrorMessageList["Index"][0] if Offset > len(Source) else self.ErrorMessageList["Index"][1] if Source is None else None
    # 将未定义的字符导出为字典
    def Export_Undefined_Dictionary(self, Undefined:list) -> dict:
        return {each:each for each in Undefined}
    # 将明文分为N组
    def Split_Text_Fence(self, Text:str, N:int) -> dict:
        _Index = 0
        Groups = {f"Group{each}":[] for each in range(1, N+1)}
        Groups_Index = [each for each in Groups]
        for each in Text:
            _Index += 1
            Groups[Groups_Index[_Index%N]].append(each)
        return Groups, Groups_Index
    # 使用Base64加密
    def Base64_Action(self, Text:str, Mode:str) -> str:
        if Mode == "Encode":
            return base64.b64encode(Text.encode("utf-8")).decode("utf-8")
        elif Mode == "Decode":
            return base64.b64decode(Text.encode("utf-8")).decode("utf-8")

class Dictionary(Password):
    """
    This class is used to generate dictionaries.
    """
    def __init__(self) -> None:
        super().__init__()


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
        _Upper, _Lower, _Numbers, _Offset, _Dictionary = self.Uppercase, self.Lowercase, self.Numbers, int(Offset), {}
        _Source = Self_String if bool(Self_String) else (_Upper if bool(Uppercase) else "") + (_Lower if bool(Lowercase) else "") + (_Numbers if bool(Number) else "") # 设置字符
        # 错误检查
        _ErrorMessage = super().Export_ErrorMessage_Dictionary(_Offset, _Source)
        if bool(_ErrorMessage):
            raise PasswordError(_ErrorMessage)
        _StringList = [each for each in _Source] # 导入字符到列表
        # 生成字典
        for each in _StringList:
            _Dictionary[each] = _StringList[_StringList.index(each) + _Offset] if _StringList.index(each) + _Offset < len(_StringList) else _StringList[_StringList.index(each) - len(_StringList) + _Offset]
        
        return _Dictionary

class Encrypt(Password):
    """
    This class is used to encrypt text.
    """
    def __init__(self, Text:str, UseBase64:bool=True) -> None:
        super().__init__()
        self.UseBase64 = UseBase64
        self.Text = super().Base64_Action(Text, "Encode") if UseBase64 else Text
    
 
    def Substitution(self, Dictionary:dict, Mode:str="Strict", Add_Ignore:bool=True, UseBase64:bool=False) -> str:
        """
        Text
            Text that needs to be encrypted
        Dictionary
            Dictionary required for encryption(can be generated using the Dictionary object)
        Mode
            Encrypted mode(Strict by Default), You can view all modes in the Mode property of the object.
        Add_Ignore
            Add characters that need to be ignored in the dictionary, these characters will be preserved (spaces are disabled by default and enabled), and you can modify the value of Ignore to change them
        UseBase64
            Use Base64 to encrypt passwords twice

        Mode_Note
            Strict: Include all the characters in plaintext in the dictionary, if they do not, they will self-detonate.
            Ignore: Ignore and discard all characters that are not included in the dictionary.
            Retain: Keep undefined characters (undefined characters are automatically added to the dictionary)
        """
        Text = super().Base64_Action(self.Text, "Decode") if self.UseBase64 else self.Text
        _Undefined = super().Export_Undefined(Text, Dictionary) # 导出未定义的字符
        # 错误检查
        _ErrorMessage = super().Export_ErrorMessage_Decrypt_Encrypt(Text, Dictionary, Mode, _Undefined)
        if bool(_ErrorMessage):
            raise EncryptError(_ErrorMessage)
        _ModeType, _Encrypted = self.Mode.index(Mode), ""
        # 添加默认忽略字符
        if Add_Ignore:
            Dictionary.update(super().Export_Undefined_Dictionary(self.Ignore))
        if _ModeType == 2 and bool(_Undefined):
            Dictionary.update(super().Export_Undefined_Dictionary(_Undefined)) # Retain模式添加未定义的字符
        _EncryptedList = [Dictionary[each] for each in Text] if _ModeType in [0, 2] else [Dictionary[each] for each in Text if each in Dictionary] if _ModeType in [1] else None # 加密
        for each in _EncryptedList:
            _Encrypted += each

        return _Encrypted if not UseBase64 else super().Base64_Action(_Encrypted, "Encode")
    
    def Fence(self, Group:int, UseBase64:bool=False) -> str:
        """
        Use the fence password to encrypt plaintext

        Text
            Text that needs to be encrypted
        """
        Text = super().Base64_Action(self.Text, "Decode") if self.UseBase64 else self.Text
        # 错误检查
        _ErrorMessage = super().Export_ErrorMessage_Fence(Text)
        if bool(_ErrorMessage):
            raise EncryptError(_ErrorMessage)
        Groups, Group_Index = super().Split_Text_Fence(Text, Group)
        _EncryptedList, _Encrypted, _ = [], "", [len(Groups[Group_Index[each]]) for each in range(len(Group_Index))]
        _.sort()
        _Times = _[-1] # 确定遍历次数
        del _
        # # 加密成列表
        _EncryptedList = []
        for times in range(_Times):
            _EncryptedList.extend([(Groups[each][times]) for each in Group_Index if times < len(Groups[each])])
        # 将列表转换成字符
        for each in _EncryptedList:
            _Encrypted += each

        return _Encrypted if not UseBase64 else super().Base64_Action(_Encrypted, "Encode")

class Decrypt(Password):
    """
    This class is used to decrypt password.
    """
    def __init__(self, Password:str, UseBase64:bool=False) -> None:
        super().__init__()
        self.UseBase64 = UseBase64
        self.Password = super().Base64_Action(Password, "Encode") if UseBase64 else Password
    
    def Substitution(self, Dictionary:dict, Mode:str="Strict", Add_Ignore:bool=True, UseBase64:bool=False) -> str:
        """
        Text
            Text that needs to be decrypted
        Dictionary
            Dictionary required for decryption(can be generated using the Dictionary object)
        Mode
            Decrypted mode(Strict by Default), You can view all modes in the Mode property of the object.
        UseBase64
            Whether the password uses Base64 secondary encrypt
        
        Add_Ignore
            Add characters that need to be ignored in the dictionary, these characters will be preserved (spaces are disabled by default and enabled), and you can modify the value of Ignore to change them

        Mode_Note
            Strict: Include all the characters in plaintext in the dictionary, if they do not, they will self-detonate.
            Ignore: Ignore and discard all characters that are not included in the dictionary.
            Retain: Keep undefined characters (undefined characters are automatically added to the dictionary)
        """
        Password = super().Base64_Action(self.Password, "Decode") if self.UseBase64 else self.Password
        _Password = super().Base64_Action(Password, "Decode") if UseBase64 else Password
        Dictionary = {Value:Key for Key, Value in Dictionary.items()}
        _Undefined = super().Export_Undefined(_Password, Dictionary)
        _ModeType, _Text = self.Mode.index(Mode), ""
        _ErrorMessage = super().Export_ErrorMessage_Decrypt_Encrypt(_Password, Dictionary, Mode, _Undefined)
        # 错误检查
        if bool(_ErrorMessage):
            raise DecryptError(_ErrorMessage)
        if Add_Ignore:
            Dictionary.update(super().Export_Undefined_Dictionary(self.Ignore)) # 增加默认忽略的字符
        if _ModeType == 2 and bool(_Undefined):
            Dictionary.update(super().Export_Undefined_Dictionary(_Undefined)) # Retain模式添加未定义的字符
        _DecryptedList = [Dictionary[each] for each in _Password] if _ModeType in [0, 2] else [Dictionary[each] for each in _Password if each in Dictionary] if _ModeType in [1] else None # 加密
        # 将列表转换成字符
        for each in _DecryptedList:
            _Text += each
        
        return _Text

    def Fence(self, Password:str, Group:int, UseBase64:bool=False) -> str:
        """
        Use the fence password to decrypt password

        Text
            Text that needs to be decrypt
        Group
            The number of characters that need to be grouped
        UseBase64
            Whether the password uses Base64 secondary encrypt
        """
        Password = super().Base64_Action(self.Password, "Decode") if self.UseBase64 else self.Password
        _Password = Password if not UseBase64 else super().Base64_Action(Password, "Decode")
        # 错误检查
        _ErrorMessage = super().Export_ErrorMessage_Fence(_Password)
        if bool(_ErrorMessage):
            raise DecryptError(_ErrorMessage)
        Groups, Group_Index = super().Split_Text_Fence(_Password, Group)
        _DecryptedList, _Decrypted, _ = [], "", [len(Groups[Group_Index[each]]) for each in range(len(Group_Index))]
        _.sort()
        _Times = _[-1] # 确定遍历次数
        del _
        # # 加密成列表
        _DecryptedList = []
        for times in range(_Times):
            _DecryptedList.extend([(Groups[each][times]) for each in Group_Index if times < len(Groups[each])])
        # # 转换为字符串
        for each in _DecryptedList:
            _Decrypted += each

        return _Decrypted
# 调试
if __name__ == "__main__":
    pass
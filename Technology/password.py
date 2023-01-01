class Encrypt:
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lowercase = "abcdefghijklmnopqrstuvwxyz"
    Numbers = "123456789"

    def Dictionary(self, Offset:int, Uppercase=True, Lowercase=False, Number=False, Self_String=None) -> dict:
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
        Upper = self.Uppercase
        Lower = self.Lowercase
        Numbers = self.Numbers
        Offset = int(Offset)
        StringList = []
        Dictionary = {}
        Source = Self_String if bool(Self_String) else (Upper if bool(Uppercase) else "") + (Lower if bool(Lowercase) else "") + (Numbers if bool(Number) else "")
        if Source is None:
            raise Exception("No source data is set")
        if Offset > len(Source):
            raise Exception("The offset data exceeds the limit")
        for each in Source:
            StringList.append(each)
        for each in StringList:
            Dictionary[each] = StringList[StringList.index(each) + Offset] if StringList.index(each) + Offset < len(StringList) else StringList[StringList.index(each) - len(StringList) + Offset]
        
        return Dictionary

# 调试
if __name__ == "__main__":
    pass
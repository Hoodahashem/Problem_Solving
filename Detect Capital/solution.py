def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word.isupper() == True:
        return True
    elif word.islower() == True:
        return True
    elif word[0].isupper() == True and word[1:].islower() == True:
        return True
    else:
        return False

print(detectCapitalUse("USA")) # True
print(detectCapitalUse("FlaG")) # False
print(detectCapitalUse("flag")) # True

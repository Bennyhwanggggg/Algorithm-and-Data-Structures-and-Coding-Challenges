def is_match(text, pattern):
    return helper(text, pattern, 0, 0)


def helper(text, pattern, textIndex, patIndex):
    if textIndex >= len(text):
        if patIndex >= len(pattern):
            return True
        else:
            if (patIndex + 1 < len(pattern) and pattern[patIndex + 1] == '*'):
                return helper(text, pattern, textIndex, patIndex + 2)
            else:
                return False
    elif (patIndex >= len(pattern)) and (textIndex < len(text)):
        return False
    elif (patIndex + 1 < len(pattern)) and (pattern[patIndex + 1] == '*'):
        if pattern[patIndex] == '.' or text[textIndex] == pattern[patIndex]:
            return helper(text, pattern, textIndex, patIndex + 2) or helper(text, pattern, textIndex + 1, patIndex)
        else:
            return helper(text, pattern, textIndex, patIndex + 2)
    elif pattern[patIndex] == '.' or pattern[patIndex] == text[textIndex]:
        return helper(text, pattern, textIndex + 1, patIndex + 1)
    else:
        return False
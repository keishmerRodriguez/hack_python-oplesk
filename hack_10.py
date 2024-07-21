"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman" 
    
    text = "fooziman"
    
    text = text.upper()
    
    substitutions = {
        'O': '0',
        'I': '1',
        'A': '@'
    }
    
    result = []
    for char in text:
        if char in substitutions:
            result.append(substitutions[char])
        else:
            result.append(char)
    
    return result

    
    
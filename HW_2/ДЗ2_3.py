def check_delimiters(expression):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack.pop() != matching_bracket[char]:
                return "Несиметрично"
    
    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"


print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_delimiters("( 23 ( 2 - 3);"))  # Несиметрично
print(check_delimiters("( 11 }"))  # Несиметрично

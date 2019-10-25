def balance_check(s):
    if len(s) %2 !=0:
        return False
    
    paren_dict = {'(':')','[':']','{':'}'}
    my_stack = []
    for char in s:
        if char in paren_dict:
            my_stack.append(paren_dict[char])
        else:
            if not my_stack:
                return False

            elif my_stack.pop() != char:
                return False
    if my_stack:
        return False
    else:
        return True

print(balance_check('([](()())'))
        
        
        
    
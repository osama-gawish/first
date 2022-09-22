def balanced(expression):
    #your code goes here
    listt = []
    for i in expression:
        if i == '(' or i == ')':
            listt.insert(0, i)
    right = 0
    left = 0       
    for j in listt:
        if j == '(':
            right+=1
        if j == ')':
            left+=1
    if right==left and listt[0] == ')' and listt[-1] == '(':
        return True
    else:
        return False
    

print(balanced(input()))
#The Shunting Yard Algoryhthm for Regular Expressions.

#The Input
infix = "(a|b).c*"
print("Input is:", infix)
#Expected Output : "ab|c*."
print("Expected: ","ab|c*.")

#Convert input to a stack-ish list.
infix = list(infix)[::-1]

#Operator Stack.
opers = []

#Output List.
postfix = []

#Operator Precendence
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

# Loop through input one character at a time
while infix:
    # Pop Character from the input
    c = infix.pop()
    
    # Decide What to do With the Character
    if c == '(':
         # Push An Open Bracket to the opers stack
        opers.append(c)
    elif c == ')':
        # Pop the operators stack until you find )
        while opers[-1] != '(':
            postfix.append(opers.pop())
        # Get rid of the '('.
        opers.pop()
    elif c in prec:
        # Push any operators on the opers stack with higher prec to the ouput.
        while opers and prec[c] < prec[opers[-1]]:
            postfix.append(opers.append())
        # Push C to Operator Stack
        opers.append(c)
    else:
        # Typically we just push the character to the output.
        postfix.append(c)
# Pop all operators to the output.   
while opers:
    postfix.append(opers.pop())
        
# Convert output list to string.
postfix = ''.join(postfix)
    
# Print the Result
print("Output is:", postfix)
        

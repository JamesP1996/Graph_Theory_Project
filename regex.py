# James Porter G00327095
# Classes used in thompson's construction

class State:
    """A State with one or two edges, all edges labled by label."""
    # Constructor for the Class
    def __init__(self, label=None, edges=[]):
        # Every State has 0,1 or 2 edges from it
        self.edges = edges
        # Label for the Arrows. None Means Epsilon.
        self.label = label
 
class Fragment:
    """An NFA fragment with a start state and an accept state."""
    # Constructor
    def __init__(self, start , accept):
        # Start state of NFA fragment.
        self.start = start
        # Accept State of NFA fragment.
        self.accept = accept

def shunt(infix):
    """Return the infix regular expression in postfix."""
    #Convert input to a stack-ish list.
    infix = list(infix)[::-1]

    #Operator Stack.
    opers = []

    #Postfix regular expression.
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
            # Push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            # Push C to Operator Stack
            opers.append(c)
        else:
            # Typically we just push the character to the output.
            postfix.append(c)
            
    # Pop all operators to the output.   
    while opers:
        postfix.append(opers.pop())
        
    # Convert output list to string.
    return ''.join(postfix)
    

def compile(infix):
    """Return NFA Fragment representing the infix regular expression."""
    
    # Convert infix to postfix.
    postfix = shunt(infix)
    # Make postfix a stack of characters.
    postfix = list(postfix)[::-1]
    
    # A stack for NFA fragments.
    nfa_stack = []
    
    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # Pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            # The new start state is frag2's.
            start = frag2.start
            # The new accept state is frag1's.
            accept = frag1.accept   
        elif c == '|':
            # Pop Two Fragments off the stack.
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            # Point the old accept states at the new one.
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)      
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new Start and Accept States
            accept = State()
            start = State(edges=[frag.start,accept])
            # Points the arrows.
            frag.accept.edges = ([frag.start, accept])
        else:
            accept = State()
            start = State(label=c,edges = [accept])
            
        # Create new Instance of Fragment to represent the new NFA.
        newfrag = Fragment(start,accept)     
        # Push the new NFA to the NFA Stack.
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()  

def followes(state, current):
    """Add a State to a Set and follow the e(psilon) arrows"""
    if state not in current:
        # Put the state itself into current.
        current.add(state)
        # See whether state is labeled by e(psilon).
        if state.label is None:
            # Loop through the states pointed to by this state.
            for x in state.edges:
                # Follow all their e(psilons) too.
                followes(x, current)
            
def match(regex, s):
    """Checks if the String S matches the Regular Expression Fully then returns True/False"""
    # This function will return True if and only if the regular expression
    # regex (fully) matches the string s. It returns false otherwise.
    
    # Compile the regular expression into NFA
    nfa = compile(regex)
    
    # Try to Match the Regular Expression to the String S.
    
    # The Current set of states.
    current = set()
    # Add the first state , and follow all e(psilon) arrows.
    followes(nfa.start,current)
    # The Previous set of states.
    previous = set()
    
    # Loop Through Characters in S.
    for c in s:
        # Keep track of where we were.
        previous = current
        # Create new empty set for states we're about to be in.
        current = set()
        # Loop Through Previous States
        for state in previous:
            # Only follow arrows not labeled by e(psilon)
            if state.label is not None:
                # If the Label of the state is equal to the Character you just read in.
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0],current)
    
    # Ask the NFA if it matches the string s.
    return nfa.accept in current

# Can Call the Print Function for the Regex Expressions Match
# In Another Python File. In This case "myScript.py"
# If not in Regex File Print "Regex" else if ran through this file
# Print __main__
if __name__ == "__main__":
    tests = [
        ["a.b|b*","bbbbbb",True],
        ["a.b|b*","bbbx",False],
        ["a.b","ab",True],
        ["b**","b",True],
        ["b*","",True]
    ]
    
    for test in tests:
        assert match(test[0], test[1]) == test[2], test[0] + \
        (" Should match " if test[2] else " should not match ") + test[1]
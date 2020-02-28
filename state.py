# James Porter G00327095
# Classes used in thompson's construction

class State:
    # Every State has 0,1 or 2 edges from it
    edges = []

    # Label for the Arrows. None Means Epsilon.
    label = None
    
    # Is this an accept state?
    def __init__(self,label=None,edges=[]):
        self.edges = edges
        self.label = label
 
class Frag:
    # Start state of NFA fragment.
    start = None
    # Accept State of NFA fragment.
    accept = None

    # Constructor
    def __init__(self, start , accept):
        self.start = start
        self.accept = accept

myinstance = State(label='a',edges=[])
myotherinstance = State(edges=[myinstance])
myfrag = Frag(myinstance,myotherinstance)
print(myinstance.label)
print(myotherinstance.edges[0])
print(myfrag)

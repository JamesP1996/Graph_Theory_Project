# Build Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then Match them with a String
## James Porter G00327095


# Introduction
This is a project I made for my <b>Third Year Graph Theory Module of my Software Development Degree</b>.
It's written using the python programming language and it's purpose is to construct <b>Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then match them with a String</b> to see if it returns True for it matches or False if it does not match.

# Methodology / Project Direction

The method I used to go about this is that I used the [Shunting Yard and SPF by Dijkstra](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) to convert infix Regular Expressions to their postfix (Sometimes Known as <i>"Reverse Polish Notation"</i>) counterpart and then from this built the Non-Deterministic Finite Automata using [Thompson's Construction](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
Once the DNFA's were built, I could then use them to compare the Regular Expression to a Inputted String as displayed in the Tests Section of the Code in NFA_Regex_Matcher.Py

# What I had to Learn

My Knowledge of Python as a programming language was limited to Udemy Courses and a few modules in college where we used it for Graphics using OpenCV. I had to learn some of the python programming language to understand and navigate the language. Most of my teaching in python and the numerous algorithms/methods used in this project were supplied by my lecturer Ian McLoughlin who greatly pushed me and my class forward and uploaded content for us to follow and learn from in order to understand how to navigate this project from Start to Finish.
Outside of this it was mainly my research and sources online that helped  me along this project. 

# Research

Before jumping head first into this project it was very important to gain a basic grasp of python and Finite Automata,Thompson's Construction,Regex and Shortest Path First Algorithm.

### The Sources I Used Most were :

#### Graph Theory
- Ian McLoughlin's Learn Online Slides, Videos and Lectures.

- [A Great Video on "Regular Expression" to NFA (Youtube)](https://www.youtube.com/watch?v=RYNN-tb9WxI)

- [Brilliant's Shunting Algorithm Wiki](https://brilliant.org/wiki/shunting-yard-algorithm/)

- [Operator Precedence and Infix to Postfix by RuneStone Academy](https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html)

- Written in Go But was Very Useful Blog with Descriptive Diagrams.
<br>[Regex Compiler in Go by Phanindra Moganti](https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079)

#### Python
- [Learn Python Website](https://www.learnpython.org/)
- [Introduction to Python Programming Udemy](https://www.udemy.com/course/pythonforbeginnersintro/)
- [Code Academy Python Section](https://www.codecademy.com/)

# Diagrams

<b>Non-Special Characters by Ian McLoughlin</b><br>
![alt text](https://i.imgur.com/9uSLMM5.png "Non Special Characters Diagram")

<b>Concatenation of Characters by Ian McLoughlin</b><br>
![alt text](https://i.imgur.com/dfU2xiz.png "Concatenation of Characters Diagram")

<b>Union of Characters by Ian McLoughlin</b><br>
![alt text](https://i.imgur.com/BgKM57J.png "Union of Characters Diagram")

<b>Kleene * One or More Characters by Ian McLoughlin</b><br>
![alt text](https://i.imgur.com/NqoUDuR.png "Kleene * One or More Characters Diagram")

<b>Regular expression to ∈-NFA by GeekForGeeks.org</b><br>
![alt text](https://i.imgur.com/D707UCW.png "Regular Expression Diagram")




# How the Program/Code Works (Functions, Classes)

<b>The Class State</b>:</br> Represents the State a Fragment can be in along with their connecting arrows. Every State can have 0-2 Edges Coming from it. Each Edge is labeled, but they an edge can also mean none "Episilon" ε.

<b>The Class Fragment</b>:</br>
All NFA Fragments have a Start(Initial) State and An Accept(End) State. This class basically creates a constructor with these states without defining the variables before the constructor. One of the great features of python is it's ability to write clean conscise code. In the likes of java you would have to define these variables before making a constructor with them.

<b>The Class Shunt</b>:</br>
This is the Class where we perform the Dijkstra's Shortest Path First algorithm (SPF) on infix expressions to make them into postfix regular expressions and use Shunting Yard Algorithm by Dijkstra. In order to do this we had to convert the input into a stack like list. Then Create a Operator Stack, and a PostFix Stack. After this you need to understand operator precedence and you need to create a precedence dictionary from greatest to lowest. For Example <b>The Kleene Star '*'</b> has a higher precedence than the <b>Concatenation '.'</b> Operator.
During a while loop through the infix expressions. We then decide what to do with each characters. As shown in the code in NFA_Regex_Matcher.py. After the infix to postfix is finished 'A+B' in infix should come out to 'AB+' in postfix expression.

<b>The Class Compile</b>:</br>
First we convert infix to postfix using the Shunt Class, Create a Postfix stack of characters then a empty stack for NFA Fragments.
While Postfix is not none, Pop a Character from the Stack and based on the character if its sepecial do as described in a if statement else just push the character and label to the stack.
Special Characters are all dealt with in if and elif statements. So for example the '|' Operator will make us pop two fragments off the stack, create a new accept state and a start state linked to the second and first fragment's start states then append the new accept state to fragment one and fragments two's accept state edges.
This may sound complex but this is why it's very important to understand NFA's , DFA's , Shunting Yard, SPF and General Graph Theory Terminology in relation to these , to begin to program something like this. There is numerous resources online for this.

<b>The Class Followes</b>:</br>
This Class Adds a State to a Set and Follows the Epsilon ε Arrows.

<b>The Class Match</b>:</br>
This is the final class of our program. It is used to check if a postfix regular expression matches a inputted String/Character.
It first Creates a Non Deterministic Finite Automata. Makes a Current Set of States. Adds the First State of the NFA to the followees class and follows the arrows. We then create a previous set of states and loop thrugh each character in the String.
Previous will be used to keep track of where we were.
Create a new empty set of states for the states we are about to be in and for each state in the previous only followed the arrows that are not empty (Epsilon) ε. If the Label of the arrow is is equal to the character you just read in from the string. Add the State at the end of the arrow to the current state. Once each and every character in a string is done. Return true or false if the NFA matches the String.

Finally After all of these Classes I have a list of tests for the user to perform , that you can edit if you want to try different types of strings against a regex expression.

If all Tests match their respective True or False Statement. Then the program will run without any error else the program will show an assertion error.

# Tests In File Currently (Can be Edited/Changed)
```Python
if __name__ == "__main__":
    tests = [
        ["a.b|b*","bbbbbb",True],
        ["a.b|b*","bbbx",False],
        ["a.b*","abbb",True],
        ["b**","b",True],
        ["b*","",True],
        ["a.b*","abbb",True],
        ["a$","a",False],
        ["a.b+","ab",True],
        ["a.b|a?","abbbb",False]
    ]
```

# Conclusion
In Conclusion the Project was quite hard to tackle at the beginning of the semester as I was completely inexperienced in Graph Theory and had very little knowledge of Python but through research and my Lecturer Ian's Great Explanations and Diagrams , I saw the purpose in this information and it gave me a great appreciation for the history and genius of programmers long ago.

I feel now that if i were asked to re-write this program in a less loosely types programming language such as Java,C,C++,C# I would have a interesting time in doing so and would maybe like to do this in the future as a side project and add more to it.

I created a 'myScript' python file which can be edited , if you wish to see what statements return true or false rather then editing the nfa_regex matcher code. It uses the nfa_regex_matcher as a importable resource and basically returns true or false based on the regex and the string. 
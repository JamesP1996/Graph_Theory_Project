# Build Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then Match them with a String
## James Porter G00327095


# <b>Introduction</b>
This is a project I made for my <b>Third Year Graph Theory Module of my Software Development Degree</b>.
It's written using the python programming language and it's purpose is to construct <b>Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then match them with a String</b> to see if it returns True for it matches or False if it does not match.

# <b>Running the Code</b>
To run this project you will a version of Python. Preferably Python 3. You can download python at their website https://www.python.org/downloads/.

I used Vi on a Google Cloud Machine to code this up but I would recommend to use Visual Studio Code or Pycharm if you were going to do this locally and wanted some auto code completion features.

## <b>NFA_Regex_Matcher.py</b>
To run this file , it uses a python package known as argparse. If you run this file with no command line arguments, nothing will come up so you need to run it with different optional commands. If you need help while running the program you can use, 
```
python NFA_Regex_Matcher.py --help
```
in the command line terminal where the file in the directory the file is located.
The List of Command Line Arguments you can use in conjunction are 

### <b>Regex Match a Regular Expression and a String (Evaluates to True or False)</b>

- ``` python NFA_Regex_Matcher.py --regex "<Regular Expression Here> -- String <Some String to Match Here>" ```

OR

- ``` python NFA_Regex_Matcher.py -r "<Regular Expression Here> -s "<Some String to Match Here>" ```

<i>The -r and -s are short handed ways of telling the argument parser what you want to input. So -r is the same as --regex and -s is the same as --string.</i>

### <b>Input Infix Expression and Return a Postfix Expression</b>

- ``` python NFA_Regex_Matcher.py --postfix "<Infix Expression Here>" ```

OR

- ``` python NFA_Regex_Matcher.py -p "<Infix Expression Here>" ```

<i>Doing so will return the postfix version of any infix string you input into the command line argument.</i>

### <b>Run Tests within the NFA_Regex_Matcher.py Python Code</b>
- ``` python NFA_Regex_Matcher.py --tests ```

OR

- ``` python NFA_Regex_Matcher.py -t ```

<i> The Test Part takes no positional arguments and is simply run by the --tests or -t command. It will run through all the tests in the code and if the test returned the correct result it will say the test along with a print saying "Completed Successfully" underneath it. If this does not happen and it returns a error then that test where it stopped posting successful is where it failed</i>

## How do the Tests Work in the NFA_Regex_Matcher.py File ?
The tests in NFA_Regex_Matcher.py were basically setup using a dictionary/list of different Regex expressions matched against Strings then what the matching program should return. So For Example 
The Regex Expression "a.b|b*" should match the string "bbbbbb" and return True.

<b>Tests in File:</b>
``` 
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


Down at the end of the code we have a paragraph which has a For In Loop. For Each Test in tests. In this we are asserting that the regex matches the string and returns what we put as the false or true value. If it does not return the right true or false value that we inputted the assertion tests will fail and it will be displayed in the console. If it is successful it will print the test along with the line <b>"Completed Successfully"</b>.

<b>Code at End of File Relating to Testing:</b>

```
elif (args.tests is True):
        for test in tests:
            assert match(test[0], test[1]) == test[2], test[0] + \
            (" Should match " if test[2] else " should not match ") + test[1]
            print(test)
            print("Completed Successfully")
```

# Algorithms Used

The method I used to go about this is that I used the [Shunting Yard and SPF by Dijkstra](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) to convert infix Regular Expressions to their postfix (Sometimes Known as <i>"Reverse Polish Notation"</i>) counterpart and then from this built the Non-Deterministic Finite Automata using [Thompson's Construction](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
Once the Deterministic Non Finite Automata's were built, I could then use them to compare the Regular Expression to a Inputted String as displayed in the Tests Section of the Code in NFA_Regex_Matcher.py

1. Shunting Yard and SPF by Dijkstra
2. Thompson's Construction

## Shunting Yard and SPF by Dijkstra

We use Shunting Yard and SPF to ensure that when we do our NFA's out and our matching that the Regular Expression is readable to a machine. Us as humans use Infix Regular Expression as it's readable and understandable to us so for example "a.b|b*" but to a machine this is not very readable so we have to convert it to postfix in this case it would be "ab.b*|". 

Here is a diagram on how Shunting Yard Works. Sourced from Wikipedia Link I detailed above.

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Shunting_yard.svg/400px-Shunting_yard.svg.png "Shunting Yard Diagram")

This diagram uses a three-way railroad junction like approach to try explain how each input get's handled. Whether its a string like "a" and gets pushed to output straight away or if its a operator like "+" and gets sent to the operator stack.
After all the pushing and popping is complete, you will eventually get the Postfix Version of a Infix Expression.
Such as in the diagram A+BxC-D became ABCx+D-.


## Thompson's Construction

Thompson's construction algorithm, also called the McNaughton-Yamada-Thompson algorithm[1], is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA).This NFA can be used to match strings against the regular expression. This algorithm is credited to Ken Thompson.

Sourced from IMGUR , unsure of it's original creator, this is what a typical non-deterministic automaton looks like below.


![alt text](https://i.stack.imgur.com/oGfLc.png "Non-Deterministic Automaton")

A diagram or NFA is made up of edges and fragments. For Example a is a fragment whilst 0 or 1 are edges. 
There is always a Start State which would be A and a Accept State which in this case would be C. 

Here is an example of a minimal deterministic automaton from Wikipedia.

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/DFA_example_multiplies_of_3.svg/369px-DFA_example_multiplies_of_3.svg.png "Deterministic Automaton")

The Differences Between Deterministic Finite Automata and Non Deterministic Finite Automata will be listed below.

### Deterministic Finite Automata

- For a particular input the computer will give always same output.
- Can solve the problem in polynomial time.
- Can determine the next step of execution.

### Non Deterministic Finite Automata 

- For a particular input the computer will give different output on different execution.
- Can’t solve the problem in polynomial time.
- 	Cannot determine the next step of execution due to more than one path the algorithm can take.

In the case of this project we are using Getting Infix Regular Expressions and forwarding them to their postfix counter part and then constructing Non-Deterministic Finite Automata out of them and Comparing the NDFA Regular Expression to a String to see if they do or do not match.

There are many diagrams on the README file of this GitHub relevant to how each operator works in a NDFA construction.

# References

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

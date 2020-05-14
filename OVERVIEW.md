# Build Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then Match them with a String
## James Porter G00327095


# <b>Introduction</b>
This is a project I made for my <b>Third Year Graph Theory Module of my Software Development Degree</b>.
It's written using the python programming language and it's purpose is to construct <b>Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then match them with a String</b> to see if it returns True for it matches or False if it does not match.

# <b>Running the Code</b>
To run this project you will a version of Python. Preferably Python 3. You can download python at their website https://www.python.org/downloads/.

I used Vi on a Google Cloud Machine to code this up but I would reccomend to use Visual Studio Code or Pycharm if you were going to do this locally and wanted some intellisense.

## <b>NFA_Regex_Matcher.py</b>
To run this file , it uses a python package known as argparse. If you run this file with no command line arguements, nothing will come up so you need to run it with different optional commands. If you need help while running the program you can use, 
```
python NFA_Regex_Matcher.py --help
```
in the command line terminal where the file in the directory the file is located.
The List of Command Line Arguements you can use in conjunction are 

### <b>Regex Match a Regular Expression and a String (Evaluates to True or False)</b>

- ``` python NFA_Regex_Matcher.py --regex "<Regular Expression Here> -- String <Some String to Match Here>" ```

OR

- ``` python NFA_Regex_Matcher.py -r "<Regular Expression Here> -s "<Some String to Match Here>" ```

<i>The -r and -s are short handed ways of telling the arguement parser what you want to input. So -r is the same as --regex and -s is the same as --string.</i>

### <b>Input Infix Expression and Return a Postfix Expression</b>

- ``` python NFA_Regex_Matcher.py --postfix "<Infix Expression Here>" ```

OR

- ``` python NFA_Regex_Matcher.py -p "<Infix Expression Here>" ```

<i>Doing so will return the postfix version of any infix string you input into the command line arguement.</i>

### <b>Run Tests within the NFA_Regex_Matcher.py Python Code</b>
- ``` python NFA_Regex_Matcher.py --tests ```

OR

- ``` python NFA_Regex_Matcher.py -t ```

<i> The Test Part takes no posistional arguements and is simply run by the --tests or -t command. It will run through all the tests in the code and if the test returned the correct result it will say the test along with a print saying "Completed Successfully" underneath it. If this does not happen and it returns a error then that test where it stopped posting successful is where it failed</i>

## How do the Tests Work in the NFA_Regex_Matcher.py File ?
The tests in NFA_Regex_Matcher.py were basically setup using a dictionary/list of different Regex expressions matched against Strings then what the matching program should return. So For Example 
The Regex Expresssion "a.b|b*" should match the string "bbbbbb" and return True.

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


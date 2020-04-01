# Graph Theory Project for GMIT Software Development Year 3 "Graph Theory" Module. 
# James Porter G00327095


# Introduction
This is a project I made for my Third Year Graph Theory Module of my Software Development Degree.
It's written using the python programming language and it's purpose is to construct Non-Deterministic Finite Automata(NDFA) based on Postfix Regular Expressions and then match them with a String to see if it returns True for it matches or False if it does not match.

# Methodology / Project Direction

The method I used to go about this is that I used the Dijkstra's Shortest Path First algorithm (SPF) to convert infix Regular Expressions to their postfix counterpart and then from this built the Non-Deterministic Finite Automata using Thompson's Construction.
Once the DNFA's were built, I could then use them to compare the Regular Expression to a Inputted String as displayed in the Tests Section of the Code in NFA_Regex_Matcher.Py

# What I had to Learn

My Knowledge of Python as a programming language was limited to Udemy Courses and a few modules in college where we used it for Graphics using OpenCV. I had to learn some of the python programming language to understand and navigate the language. Most of my teaching in python and the numerous algorithms/methods used in this project were supplied by my lecturer Ian McLoughlin who greatly pushed me and my class forward and uploaded content for us to follow and learn from in order to understand how to navigate this project from Start to Finish.
Outside of this it was mainly my research and sources online that helped  me along this project. 

# Research

Before jumping head first into this project it was very important to gain a basic grasp of python and Finite Automata,Thompson's Construction,Regex and Shortest Path First Algorithm.

### The Sources I Used Most were :

#### Graph Theory
- Ian McLoughlin's Learn Online Slides, Videos and Lectures.
- A Great Video on "Regular Expression" to NFA (Youtube)
- Brilliant's Shunting Algorithm Wiki.
- Operator Precedence and Infix to Postfix by RuneStone Academy
- Written in Go But was Very Useful Blog with Descriptive Diagrams. [Regex Compiler in Go by Phanindra Moganti]
(https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079)
#### Python
- [Learn Python Website](https://www.learnpython.org/)

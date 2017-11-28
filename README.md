XLines - Executable Lines
=========================

***"A new approach towards Python programming"***

`Copyright (c) SavSec XLines`

XLines `(executable lines)` is a Python program which allows users to call any section of code within the program they are running by adding a tag! This feature allows people to reduce repeating processes without having to define a function!

xLines [Executable Lines]
Programmer: @Russian_Otter
Inspiration: @js.avi

Usage
-----

```python
>>> import xlines
... filename,tab = "test.py","\t"
... xl = xlines.XLines(filename,tab)
... 
... def function():
... 	print "Welcome To", ##xl-welcome-2
... 	print "XLines"
... 	print a
... 
... xl.run("welcome",{"a":5})
Welcome To XLines
5
```

About
-----

XLines/Executable-Lines is a program that allows you to call any marked portion of code within the program you are running or external programs that you have saved!
With XLines you can dramatically shorten the number of lines used in a program without using 'def', and you can call the marked code from anywhere!

Syntax
------

To add a marker to a portion of code use the following syntax on the line you wish to start with:
	
	##xl-macro-lines
	
	'macro' -> The name of the marker
	'lines' -> the number of lines you want to run after the current line is run

Example:

```python
>>> print "hi" ##xl-hi-1
... print "bye"
```


To execute a marker, use the following syntax:
	
```python
xl.run(macro)
```

	'macro' -> The name of the marker you wish to call


To replace a value in the code you want to execute use following syntax:

```python
xl.run(macro, switch=(find, replace))
```

	'macro' -> The name of the marker you wish to call
	'find' -> Target code/value
	'replace' -> substitute code/value


To add local variables to your target code use the following syntax:

```python
xl.run(macro, {"var": value})
```

	'macro' -> The name of the marker you wish to call
	'var' -> The name of the local variable you wish to add
	'value' -> The value of the variable

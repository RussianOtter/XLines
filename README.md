XLines - Executable Lines
=========================

***"A new approach towards Python programming"***

XLines `(executable lines)` is a Python program which allows users to call any section of code within the program they are running by adding a tag! This feature allows people to reduce repeating processes without having to define a function!

Syntax
======

**Adding Tags**

Tags are inserted onto the line of code you which to run. The syntax is `##lx-name-lines` and can be put anywhere (even if it is on a tab)!

*Explained Example:*

```python
import xlines
xl = xlines.XLines("test.py","\t")

def function():
	print "hello"
	print "this" ##xl-func-3
	print "is"
	print "a"
	print "function"
```

In this example the flag starts at `print "this"`, the call-name is `func`, and the flag includes the next `3` lines. When you call this using xlines it should look like this:

```python
xl.run("func")
```
```
this
is
a
function
```

Complete Example
================

```python
import xlines
xl = xlines.XLines("test.py","\t")

def algorithm():
	if 1**2.0 == (0.5*2)**2:
		for _ in range(3): ##xl-math-2
			print (10**2)/3.5
			print ~_
		print "Finished"

xl.run("math")
```
```
28.5714285714
-1
28.5714285714
-2
28.5714285714
-3
```

import os, sys

class XLines(object):
	"""
xLines [Executable Lines]
Programmer: @Russian_Otter
Inspiration: @js.avi

	--------------
	 xlines Usage
	--------------
	
>>> import xlines
... filename,tab = "test.py","\\t"
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

	--------------
	 xlines About
	--------------

XLines/Executable-Lines is a program that allows you to call any marked portion of code within the program you are running or external programs that you have saved!
With XLines you can dramatically shorten the number of lines used in a program without using 'def', and you can call the marked code from anywhere!

	---------------
	 xlines Syntax
	---------------

To add a marker to a portion of code use the following syntax on the line you wish to start with:
	
	##xl-macro-lines
	
'macro' -> The name of the marker
'lines' -> the number of lines you want to run after the current line is run

Example:
	>>> print "hi" ##xl-hi-1
	... print "bye"


To execute a marker, use the following syntax:
	
	xl.run(macro)

'macro' -> The name of the marker you wish to call


To replace a value in the code you want to execute use following syntax:
	
	xl.run(macro, switch=(find, replace))

'macro' -> The name of the marker you wish to call
'find' -> Target code/value
'replace' -> substitute code/value


To add local variables to your target code use the following syntax:
	
	xl.run(macro, {"var": value})

'macro' -> The name of the marker you wish to call
'var' -> The name of the local variable you wish to add
'value' -> The value of the variable

	"""
	def parse(self):
		for _ in self.content:
			if "2323".decode("hex")+"xl-" in _:
				id, lines = _.split("2323".decode("hex")+"xl-")[1].split("-")
				lines = lines.replace("\n","")
				line = self.content.index(_)
				self.marks.update({line:(id, lines)})
	
	def format_x(self):
		for _ in self.marks:
			code = self.content[_:_+int(self.marks[_][1])+1]
			tab_count = range(1,9)
			tab_count.reverse()
			nc = []
			for t in tab_count:
				if code[0].startswith(self.tab*t):
					for c in code:
						nc.append(c[t:])
					break
			code = "".join(nc)
			self.macros.update({self.marks[_][0]:code})
	
	def run(self, id, values=None, switch=None):
		code = self.macros[id]
		combine = ""
		if switch != None:
			if len(switch) == 2:
				code = code.replace(switch[0], switch[1])
		if type(values) == dict:
			for _ in values:
				if type(values[_]) == str:
					combine += "%s = '%s'\n"%(_,values[_])
				else:
					combine += "%s = %s\n"%(_,values[_])
		code = combine + code
		exec code
	
	def __init__(self, file, tab=False):
		self.content = open(file).readlines()
		self.marks = {}
		self.macros = {}
		self.file = file
		if not tab:
			for _ in self.content:
				if " "*4 in _:
					tab = " "*4
					break
				if "\t" in _:
					tab = "\t"
					break
				if " "*2 in _:
					tab = " "*2
					break
		self.tab = tab
		self.parse()
		self.format_x()

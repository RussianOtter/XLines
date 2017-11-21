import os, sys

class XLines(object):
	"""
	xLines [Executable Lines]
	@Russian_Otter
	"""
	def parse(self):
		for _ in self.content:
			if "2323".decode("hex")+"xl-" in _:
				id,lines = _.split("2323".decode("hex")+"xl-")[1].split("-")
				lines = lines.replace("\n","")
				line = self.content.index(_)
				self.marks.update({line:(id,lines)})
	
	def format_x(self):
		for _ in self.marks:
			code = self.content[_:_+int(self.marks[_][1])+1]
			tab_count = range(1,8)
			tab_count.reverse()
			nc = []
			for t in tab_count:
				if code[0].startswith(self.tab*t):
					for c in code:
						nc.append(c[t:])
					break
			code = "".join(nc)
			self.macros.update({self.marks[_][0]:code})
	
	def run(self,id,switch=None):
		code = self.macros[id]
		if switch != None:
			if len(switch) == 2:
				code = code.replace(switch[0], switch[1])
		exec code
	
	def __init__(self, file, tab="\t"):
		self.content = open(file).readlines()
		self.marks = {}
		self.macros = {}
		self.file = file
		if tab == "\t" and sys.platform != "ios":
			tab = " "*4
		self.tab = tab
		self.parse()
		self.format_x()

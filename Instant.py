from math import *

class Instant(object):
	'''Formate HH:MM:SS,XXX'''
	def __init__(self,*args,positive=True):
		self._milliSeconds = args[-1]
		if len(args) > 1:
			self._seconds = args[-2]
		else:
			self._seconds = 0
		if len(args) > 2:
			self._minutes = args[-3]
		else:
			self._minutes = 0
		if len(args) > 3:
			self._hours = args[-4]
		else:
			self._hours = 0
		self._positive = positive
		self.correct()

	def intoMilliSeconds(self):
		return self._milliSeconds + 1000*(self._seconds + 60*(self._minutes + 60*self._hours))

	def correct(self):
		if self.intoMilliSeconds() < 0:
			self._positive = False
			self._hours = -self._hours
			self._minutes = -self._minutes
			self._seconds = -self._seconds
			self._milliSeconds = -self._milliSeconds
		self._seconds += self._milliSeconds // 1000
		self._milliSeconds %= 1000
		self._minutes += self._seconds // 60
		self._seconds %= 60
		self._hours += self._minutes // 60
		self._minutes %= 60
		self._hours %= 100

	def setWithString(self,str):
		if str[0] == '-':
			str = str[1:]
			self._positive = False
		else:
			self._positive = True
		self._hours = int(str[0:2])
		self._minutes = int(str[3:5])
		self._seconds = int(str[6:8])
		self._milliSeconds = int(str[9:12])

	def strWithForcedZeros(self,n,digits):
		#Return 0003 instead of 3 with digits=4 (n=3)
		if n == 0:
			return digits*'0'
		else:
			return (digits - int(log10(n))-1)*'0' + str(n)

	def __add__(self,other):
		s1,s2 = 2*self._positive-1,2*other._positive-1
		inst = Instant(s1*self._hours + s2*other._hours,s1*self._minutes + s2*other._minutes,s1*self._seconds + s2*other._seconds,s1*self._milliSeconds + s2*other._milliSeconds)
		inst.correct()
		return inst

	def __pos__(self):
		return self

	def __neg__(self):
		self._positive = not self._positive
		return self

	def __sub__(self,other):
		return self + -other

	def __abs__(self):
		self._positive = True
		return self

	def __str__(self):
		return "{}{}:{}:{},{}".format("-" if not self._positive else "",self.strWithForcedZeros(self._hours,2),self.strWithForcedZeros(self._minutes,2),self.strWithForcedZeros(self._seconds,2),self.strWithForcedZeros(self._milliSeconds,3))		
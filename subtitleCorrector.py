from Instant import Instant
from os import listdir


## The subtitles of each file in the current folder will be translated of shiftTime

shiftTime = Instant(-53,-500) #Time with the imported class Instant : Instant(hours,minutes,seconds,milli-seconds), might be negative


## Processing
everyFile = listdir('./')
fileList = []
for f in everyFile:
	if f[-4:] in ['.txt', '.srt']:
		fileList.append(f)
for f in fileList:
	f2 = open('correction_'+f,'w')
	print(100*'*')
	print(f)
	content = open(f,"r").read()
	repliesList = content.split("\n\n")
	for reply in repliesList:
		try:
			subBlock = reply.split("\n")
			while subBlock and subBlock[0] == '':
				del subBlock[0]
			if subBlock:
				f2.write(subBlock[0]+'\n')

				subTimes = subBlock[1]
				t1,t2 = subTimes.split(' --> ')
				inst1,inst2 = Instant(0),Instant(0)
				inst1.setWithString(t1)
				inst2.setWithString(t2)
				f2.write(str(inst1 + shiftTime))
				f2.write(' --> ')
				f2.write(str(inst2 + shiftTime))
				f2.write('\n')

				for line in subBlock[2:]:
					f2.write(line+'\n')
				f2.write('\n')
		except:
			pass

from Instant import Instant
from os import listdir


## The subtitles of each file in the current folder will be translated of shiftTime

shiftTime = Instant(0,0,0,0) #Time with the imported class Instant : Instant(hours,minutes,seconds,milli-seconds), might be negative


## Processing
everyFile = listdir('./')
fileList = []
for file in everyFile:
	if file[-4:] in ['.txt', '.srt']:
		fileList.append(file)
for file in fileList:
	print(100*'*')
	print(file)
	print("Subtitles shifted of {}".format(shiftTime))
	content = open(file,"r").read()
	repliesList = content.split("\n\n")
	new_file = open(file,'w')
	for reply in repliesList:
		try:
			subBlock = reply.split("\n")
			while subBlock and subBlock[0] == '':
				del subBlock[0]
			if subBlock:
				# print(subBlock)
				new_file.write(subBlock[0]+'\n')
				subTimes = subBlock[1]
				t1,t2 = subTimes.split(' --> ')
				# print(t1,t2)
				inst1,inst2 = Instant(0),Instant(0)
				# print(subBlock[0],inst1,inst2)
				inst1.setWithString(t1)
				inst2.setWithString(t2)
				new_file.write(str(inst1 + shiftTime))
				new_file.write(' --> ')
				new_file.write(str(inst2 + shiftTime))
				new_file.write('\n')

				for line in subBlock[2:]:
					new_file.write(line+'\n')
				new_file.write('\n')
		except:
			pass

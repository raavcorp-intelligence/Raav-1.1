#def FINALGetValues(ValueQuestion):
import time
global questionsAsked = []
def memoryStorageReadValues():
	filepathx1 = "Memorytest.raavmemory"
	with open(filepathx1) as fp:
		linex1 = fp.readline()
		count = 1
		while linex1:
			questionsAsked.append(linex1.strip())
			linex1 = fp.readline()
			count += 1
questionsAskedX1 = []
def memoryStorageReadValuesX():
	filepathx2 = "Questiontest.raavmemory"
	with open(filepathx2) as fp:
		linex2 = fp.readline()
		count = 1
		while linex2:
			questionsAskedX1.append(linex2.strip())
			linex2 = fp.readline()
			count += 1






def memoryStorageReadgetValues(QA):
	QA = ">>>" + QA
	if questionsAsked.index(QA):
		for listItem in questionsAsked:
			for index, x in enumerate(questionsAsked):
				print(x, index)
				time.sleep(1)
				if index == listItem:
					index = index + 1
					return index, x
	else:
		return False

def memoryStorageWrite(addMEM, MEMquestion):
	#indexQuestion = memoryStorageReadgetValues(MEMquestion)
	#if indexQuestion == True:

	fileMEM = open("Memorytest.raavmemory", "a")
	fileMEM.write(">>>" + addMEM)
	fileMEM.write("\n")
	fileMEM.close()
	fileQST = open("Questiontest.raavmemory", "a")
	fileQST.write(">>>" + MEMquestion)
	fileQST.write("\n")
	fileQST.close()


memoryStorageWrite("raav", "raav2")
memoryStorageReadValues()
memoryStorageReadValuesX()
xtest = memoryStorageReadgetValues("raav")
print(xtest)



'''projectName: makeSrt
projectStartDate: 2020/02/21
projectAuthor: Bahman-Ahmadi
projectProgrammingLanguage: python3
projectInfo: a program for help user in making srt files!
projectVersion: 1.0.0Alpha'''

def add(fileName, count, start, finish, text):
	startTime, startMS = start[0], start[1]
	finishTime, finishMS = finish[0], finish[1]
	tamplate = f"{count}\n{startTime},{startMS} --> {finishTime},{finishMS}\n{text}\n\n"
	
	try:
		open(fileName,"a+").write(tamplate)
	except:
		open(fileName,"x")
		open(fileName,"a+").write(tamplate)
	
	return tamplate
		
		
if __name__ == "__main__":
	from langlib1 import style
	print(style("","white"),end="")
	
	writeAs = input(">>> enter file name (filename.srt): ")
	line = 1
	addLoop = "y"
	result = ""
	
	while addLoop:
		selectedStartTime = input(">>> enter start time(h:m:s:ms): ")
		selectedFinishTime = input(">>> enter finish time(h:m:s:ms): ")
		selectedText = input(">>> enter text of this part: ")
		
		result += add(writeAs, line, [":".join(selectedStartTime.split(":")[:-1]),selectedStartTime.split(":")[-1]], [":".join(selectedFinishTime.split(":")[:-1]),selectedFinishTime.split(":")[-1]], selectedText)
		line += 1
		
		addLoop = input(">>> do u want add new part? (y/n): ") == "y"
	
	from os import system
	system("clear")
	print(style(result,"lyellow"))
	input()
	print(style(f"data was saved at {writeAs}","lgreen"))
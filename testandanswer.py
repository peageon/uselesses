def start():
	qnum = int(input("How many questions are there?"))
	my_answers = []
	real_answers = []
	for question in range(qnum):
		my_answers.append(input("Q"+ str((question+1)) + ":"))
	print("-------------------------------------------")
	print("Text book answers")
	for question in range(qnum):
		real_answers.append(input("Q" + str(question+1) + ":"))
	print("-------------------------------------------")
	for q in range(qnum):
		if my_answers[q] != real_answers[q]:
			print("Q"+str(q+1)+" answer is " + real_answers[q])
	return 

start()
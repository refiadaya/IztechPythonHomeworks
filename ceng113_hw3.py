
def getScore():
    
    midtermScore= float(input("Enter your midterm score: "))
    finalScore= float(input("Enter your final score: "))
    quizScores= []
    for i in range(1,5):
        quizScores.append(float(input("Enter your quiz {} result: ".format(i))))
    homeworkScores= []
    for i in range(1,5):
        homeworkScores.append(float(input("Enter your homework {} result: ".format(i))))
    
    scores= [midtermScore, finalScore, quizScores, homeworkScores]
    
    print("Your scores are saved :)")
    
    return scores
    
    
def calculateTotalScore(scores):
    
    MS= scores[0]
    FS= scores[1]
    QS= sum(scores[2])/len(scores[2])
    HS= sum(scores[3])/len(scores[3])
    
    totalScore= MS*0.25 + FS*0.35 + QS*0.20 + HS*0.20
    
    print("Your total score is", totalScore)
    
    return totalScore


def calculateAbsenteeismRate():
    
    numOfCourses= 14
    numOfAbsences= int(input("Enter the number of absences: "))
    absenteeismRate= numOfAbsences/numOfCourses
    
    print("Your absenteeism rate is", absenteeismRate)
    
    return absenteeismRate


def displayLetterGrade(absenteeismRate, totalScore):
    
    if absenteeismRate > 0.25:
        letterGrade= "NA"
   
    else:
        
        if totalScore >= 90 and totalScore <= 100:
            letterGrade= "AA"
        elif totalScore >= 85 and totalScore <= 89:
            letterGrade= "BA"
        elif totalScore >= 80 and totalScore <= 84:
            letterGrade= "BB"
        elif totalScore >= 75 and totalScore <= 79:
            letterGrade= "CB"
        elif totalScore >= 70 and totalScore <= 74:
            letterGrade= "CC"
        elif totalScore >= 65 and totalScore <= 69:
            letterGrade= "DC"
        elif totalScore >= 60 and totalScore <= 64:
            letterGrade= "DD"
        elif totalScore >= 50 and totalScore <= 60:
            letterGrade= "FD"
        else:
            letterGrade= "DD"
        
    print("Your letter grade is", letterGrade)
            
            
def main():
    scores= getScore()
    totalScore= calculateTotalScore(scores)
    absenteeismRate= calculateAbsenteeismRate()
    displayLetterGrade(totalScore, absenteeismRate)
    
    
main()
    
    
    
    
    
    
    
    
    
    


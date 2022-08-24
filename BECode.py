"""Program by Thabang Segodi for SPAN Digital technical assessement
    Published on the 19/08/2022"""
"""Function to get the scores as user Input or read from a file and return the scores as a list"""
def get_score_contents(ans):
    teamScores = [] #list to carry the list of the scores

    """ First conditional statement for if the user typed in no
        The statement will then proceed to take the results as input until the user types done"""
    if (ans == "no"):
        print("Please enter the results in this format: 'Team_name(e.g. Chiefs) score(e.g. 1), Team_name(Pirates) score 0' NB: do not forget the comma in between the scores ")
        userInput = " "
        while userInput.lower() != "done":
            userInput = input()
            if userInput.lower() != "done":
                teamScores.append(userInput)
    else:
        fileName = input("Please enter your .txt file (with the .txt extension included) ")
        fileOutput = open(fileName)
        teamScores = fileOutput.readlines()
        fileOutput.close()
    """ Above is the Second conditional statement for if the user typed in 'yes'
        The statement will then proceed to take the filename as user input, 
        opens and reads the lines of the file into a list and close it"""   

    return teamScores
    """This returns the desired scores as a list"""

"""Function to get the scores as a list and then calculates the points of the teams and returns
 a list with the team and the points it acquired"""
def point_calculation(ans):
    results = get_score_contents(ans) #This gets the list of scores
    teamPoints = [] #list to carry the list of the scores
    """This is used to used to search through the list of scores and allocate points accordingly to the correct team"""
    for p in results:
        num1 = ""
        num2 = ""
        found1 = False
        for c in p:
            if c.isdigit() and not found1:
                num1 = num1 + c
                found1 = True
            elif c.isdigit():
                num2 = num2 + c
        p = p.replace(",", "")
        score = p.split(" ")
        """For a draw"""
        if int(num1) == int(num2):
            count = 0
            found1 = False
            found2 = False
            s = ""
            for line in teamPoints:
                if score[0] == "FC":
                    if score[0] in line and not found1:
                        found1 = True
                        temp = line
                        rank = line.split(" ")
                        point = int(rank[2]) + 1
                        temp = line.replace(rank[2], str(point))
                        teamPoints[count] = temp
                else:
                    if (score[0] + ",") in line and not found1:
                        found1 = True
                        temp = line
                        rank = line.split(" ")
                        point = int(rank[1]) + 1
                        temp = line.replace(rank[1], str(point))
                        teamPoints[count] = temp
                if score[2] == "FC":
                    if score[2] in line and not found2:
                        found2 = True
                        temp = line
                        rank = line.split(" ")
                        point = int(rank[2]) + 1
                        temp = line.replace(rank[2], str(point))
                        teamPoints[count] = temp
                else:
                    if (score[2] + ",") in line and not found2:
                        found2 = True
                        temp = line
                        rank = line.split(" ")
                        point = int(rank[1]) + 1
                        temp = line.replace(rank[1], str(point))
                        teamPoints[count] = temp
                if found1 and found2:
                    break
                count += 1
            if not found1 and not found2:
                if score[0] == "FC":
                    s = score[0] +  " " + score[1] + ", " +  str(1) + " pt"
                    teamPoints.append(s)                    
                else:
                    s = score[0] + ", " +  str(1) + " pt"
                    teamPoints.append(s)
                if score[2] == "FC":
                    s = score[2] +  " " + score[3] + ", " +  str(1) + " pt"
                    teamPoints.append(s)                    
                else:
                    s = score[2] + ", " +  str(1) + " pt"
                    teamPoints.append(s)
            elif not found1 or not found2: 
                if not found1:
                    if score[0] == "FC":
                        s = score[0] +  " " + score[1] + ", " +  str(1) + " pt"
                        teamPoints.append(s)                    
                    else:
                        s = score[0] + ", " +  str(1) + " pt"
                        teamPoints.append(s)
                if not found2:
                    if score[2] == "FC":
                        s = score[2] +  " " + score[3] + ", " +  str(1) + " pt"
                        teamPoints.append(s)                    
                    else:
                        s = score[2] + ", " +  str(1) + " pt"
                        teamPoints.append(s)
        #For home win
        elif num1 > num2:
            count = 0
            found1 = False
            found2 = False
            for line in teamPoints:
                if score[0] == "FC":
                    if score[0] in line and not found1:
                        found1 = True
                        temp = line
                        rank = line.split(" ")
                        point = int(rank[2]) + 3
                        temp = line.replace(rank[2], str(point))
                        teamPoints[count] = temp
                else:
                    if (score[0] + ",") in line and not found1:
                        found1 = True
                        temp = line
                        rank = line.split(" ")
                        point = int(rank[1]) + 3
                        temp = line.replace(rank[1], str(point))
                        teamPoints[count] = temp
                if (score[2] + ",") in line and not found2:
                    found2 = True
                if found1 and found2:
                    break
                count += 1
            if not found1 and not found2:
                if score[0] == "FC":
                    s = score[0] +  " " + score[1] + ", " +  str(3) + " pts"
                    teamPoints.append(s)                    
                else:
                    s = score[0] + ", " +  str(3) + " pts"
                    teamPoints.append(s)
                if score[2] == "FC":
                    s = score[2] +  " " + score[3] + ", " +  str(0) + " pts"
                    teamPoints.append(s)                    
                else:
                    s = score[2] + ", " +  str(0) + " pts"
                    teamPoints.append(s)
            elif not found1 or not found2: 
                if not found1:
                    if score[0] == "FC":
                        s = score[0] +  " " + score[1] + ", " +  str(3) + " pts"
                        teamPoints.append(s)                    
                    else:
                        s = score[0] + ", " +  str(3) + " pts"
                        teamPoints.append(s)
                if not found2:
                    if score[2] == "FC":
                        s = score[2] +  " " + score[3] + ", " +  str(0) + " pts"
                        teamPoints.append(s)                    
                    else:
                        s = score[2] + ", " +  str(0) + " pts"
                        teamPoints.append(s)
        #For away win
        else:
            count = 0
            found1 = False
            found2 = False
            for line in teamPoints:
                if (score[0] + ",") in line and not found1:
                    found = True
                if (score[2] + ",") in line and not found2:
                    found = True
                    temp = line
                    rank = line.split(" ")
                    point = int(rank[1]) + 3
                    temp = line.replace(rank[1], str(point))
                    teamPoints[count] = temp
            if not found1 and not found2:
                if score[0] == "FC":
                    s = score[0] + score[1] + ", " +  str(0) + " pts"
                    teamPoints.append(s)                    
                else:
                    s = score[0] + ", " +  str(0) + " pts"
                    teamPoints.append(s)
                if score[2] == "FC":
                    s = score[2] + score[3] + ", " +  str(3) + " pts"
                    teamPoints.append(s)                    
                else:
                    s = score[2] + ", " +  str(3) + " pts"
                    teamPoints.append(s)
            elif not found1 or not found2: 
                if not found1:
                    if score[0] == "FC":
                        s = score[0] + score[1] + ", " +  str(0) + " pts"
                        teamPoints.append(s)                    
                    else:
                        s = score[0] + ", " +  str(3) + " pts"
                        teamPoints.append(s)
                if not found2:
                    if score[2] == "FC":
                        s = score[2] + score[3] + ", " +  str(3) + " pts"
                        teamPoints.append(s)                    
                    else:
                        s = score[2] + ", " +  str(3) + " pts"
                        teamPoints.append(s)
    return teamPoints
    """This returns the desired list of the teams and the points they acquired"""  

"""Function to sort the list of the teams in a log where the team with the most points 
    will be on top of the league and the returns the sorted list"""        
def sort_league(teams):
    num = ""
    size = len(teams)
    numbers = []
    """Bubble sort algorithm was used to sort the list"""
    for i in teams:
        num = ""
        for c in i:
            if c.isdigit():
                num = num + c
        numbers.append(int(num))
    size_Of_nums = len(numbers)
    for i in range(size_Of_nums):
        for j in range(size_Of_nums - i -1):
            if numbers[j] < numbers[j+1]:
               temp = teams[j]
               temp1 = numbers[j]
               teams[j] = teams[j + 1]
               numbers[j] = numbers[j+1]
               teams[j+1] = temp
               numbers[j+1] = temp1
    return teams

"""Main function which will be used to get the user input of how to get the scores and also to displayed the sorted scores"""
if __name__ == "__main__":
    option = input("Do you want use to use a file for your input (Type 'yes' or 'no')? ")
    scores = point_calculation(option)
    league = sort_league(scores)
    count = 1
    for i in league:
        print(str(count) + ". " + i)
        count += 1
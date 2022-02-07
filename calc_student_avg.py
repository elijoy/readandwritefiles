def main():

    import csv
    
    student_avg = open("student_scores.csv", "r")

    student_file = csv.reader(student_avg, delimiter=',')

    avg_outfile = open("student_avg.csv", "w")


    for student in student_file:
        score1 = int(student[1])
        score2 = int(student[2])
        score3 = int(student[3])
        average = (score1 + score2 + score3)/3
        average = (format(average, ',.2f'))
        avg_outfile.write(student[0] + ' ')
        avg_outfile.write(average + '\n')

    student_file.close()
    avg_outfile.close()





main()
def main():

#Opened a file named philosophers.txt with write
    outfile = open('philosophers.txt', "w")
    
#Write the names to the file
    outfile.write("John Locke" + '\n')
    outfile.write("David Hume" + '\n')
    outfile.write("Edmund Burke" + '\n')

#Closed the file
    outfile.close()


def add_my_name():
    outfile = open('philosophers.txt', "a")

    outfile.write("Elizabeth Reyes\n")

    outfile.close()

#Call the main function
main()
add_my_name()

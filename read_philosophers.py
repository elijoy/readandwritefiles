#Thi program reads and displays the contents of the
#philosophers.txt file

def main():

#Open a file
    infile = open('philosophers.txt', "r")

    #file_contents = infile.read()

#Print the data that was read into memory
    #print(file_contents)

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    print(line1)
    print(line2)
    print(line3)


main()
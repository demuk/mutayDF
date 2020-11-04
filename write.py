# creates a variable that stores to the file
keep_track = open('tracker_file.txt', 'a+')
# asks for user input, that writes it to the variable
keep_track.writelines(input('What day is it ?: '))
# adds a new line to the text file
keep_track.writelines('\n')


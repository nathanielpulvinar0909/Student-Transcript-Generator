import time
import numpy as np
import os

# Function to start the feature
def startFeature():
  print("Please select your student level.\nU - Undergraduate\nG - Graduate\nB - Both")
  level = input("Enter your student level: ").upper()
  degree = ""

# Check if the student is graduate or both
  if level == "G" or level == "B":
      print("Please select your degree:\nM - Master\nD - Doctorate\nB0 - Both")
      degree = input("Enter your degree: ")

  stdID = input("Enter student ID: ")

# Validate the student ID
  while len(stdID) != 9:
      print("Invalid student ID")
      stdID = input("\nEnter student ID: ")

  print("\nLoading...\n")
  time.sleep(3)
  print(menuFeature(stdID))

  return level, degree, stdID

# Function to  display the menu
def menuFeature(stdID):
  print("Student Transcript Generation System")
  print("=" * 47)
  print("1. Student details")
  print("2. Statistics")
  print("3. Transcript based on major courses")
  print("4. Transcript based on minor courses")
  print("5. Full transcript")
  print("6. Previous transcript requests")
  print("7. Select another student")
  print("8. Terminate the system")
  print("=" * 47)
  option = input("Enter Your Feature:")
  print("\n")

# Check which option was selected
  if option == '1':
      detailsFeature(stdID)
  elif option == '2':
      statisticsFeature(stdID)
  elif option == '3':
      majorTrascriptFeature(stdID)
  elif option == '4':
      minorTranscriptFeature(stdID)
  elif option == '5':
      fullTrascriptFeature(stdID)
  elif option == '6':
      previousRequestFeature(stdID)
  elif option == '7':
      newStudentFeature(stdID)
  elif option == '8':
      terminateFeature(stdID)

# Function to display student details
def detailsFeature(stdID):
    # Check if student ID is valid
  if stdID == '202306000':
      studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')

      print("Name:", *studentDetails_data[1, 2:3])
      print("stdID:", *studentDetails_data[1, 1:2])
      print("Level(s):", *studentDetails_data[1, 5:6])
      print("Number of terms:", *studentDetails_data[1, 9:])
      print("College(s):", *studentDetails_data[1, 4:5])

      # Save student details to file
      output_str = f"Name: {studentDetails_data[1, 2]}\nstdID: {studentDetails_data[1, 1]}\nLevel(s): {studentDetails_data[1, 5]}\nNumber of terms: {studentDetails_data[1, 9]}\nCollege(s): {studentDetails_data[1, 4]}"
      np.savetxt(r"C:\Users\ASUS DEMO\Downloads\std202306000studentdetails.txt", [output_str], fmt="%s")
      print("\nLoading...\n")
      time.sleep(3)
      print(menuFeature(stdID))
  startFeature()

      # Check if student ID is valid
  if stdID == '202307000':
      studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')

      # Display student details
      print("Name:", *studentDetails_data[2, 2:3])
      print("stdID:", *studentDetails_data[2, 1:2])
      print("Level(s):", *studentDetails_data[2, 5:6])
      print("Number of terms:", *studentDetails_data[2, 9:])
      print("College(s):", *studentDetails_data[2, 4:5])

      studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')

      # Save student details to file
      output_str = f"Name: {studentDetails_data[2, 2]}\nstdID: {studentDetails_data[2, 1]}\nLevel(s): {studentDetails_data[2, 5]}\nNumber of terms: {studentDetails_data[2, 9]}\nCollege(s): {studentDetails_data[2, 4]}"
      np.savetxt(r"C:\Users\ASUS DEMO\Downloads\std202307000studentdetails.txt", [output_str], fmt="%s")

  else:
      print("File not found")
      print("\nLoading...\n")
      time.sleep(3)
      print(menuFeature(stdID))
  startFeature()

# Function to display student statistics
def statisticsFeature(stdID):
    # check if the student ID is 202306000
   if stdID == '202306000':

       # load data from the CSV file for student 202306000
       stdIDStatistics_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202300600.csv", dtype=str, delimiter=',')

       # calculate the overall average grade for all terms
       overall_average_all_term = (int(*stdIDStatistics_data[1, 7:8]) + int(*stdIDStatistics_data[2, 7:8]) + int(
           *stdIDStatistics_data[3, 7:8]) + int(*stdIDStatistics_data[4, 7:8]) + int(
           *stdIDStatistics_data[5, 7:8]) + int(*stdIDStatistics_data[6, 7:8]) + int(
           *stdIDStatistics_data[7, 7:8]) + int(*stdIDStatistics_data[8, 7:8])) / 8
       # calculate the average grade for the first term
       average_first_term = (int(*stdIDStatistics_data[1, 7:8]) + int(*stdIDStatistics_data[2, 7:8]) + int(
           *stdIDStatistics_data[3, 7:8]) + int(*stdIDStatistics_data[4, 7:8])) / 4
       # calculate the average grade for the first term
       average_second_term = (int(*stdIDStatistics_data[5, 7:8]) + int(*stdIDStatistics_data[6, 7:8]) + int(
           *stdIDStatistics_data[7, 7:8]) + int(*stdIDStatistics_data[8, 7:8])) / 4
       # load grades data from the CSV file for student 202306000
       grades = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202306000.csv", delimiter=',', skiprows=1, usecols=(7,))
       # find the maximum grade
       max_grade = np.max(grades)
       # find the minimum grade
       min_grade = np.min(grades)

       # print the header for the output
       print("=" * 55)
       print("*" * 10 + " " * 7, "Undergraduate Level", " " * 7 + "*" * 10)
       print("=" * 55)

       # print the calculated statistics
       print("Overall average (major and minor) for all terms:", overall_average_all_term)
       print("Average (major and minor) for each terms:  \n ""    Term 1:", average_first_term, "\n ""    Term 2:",
             average_second_term)
       print("Maximum grade(s) and in which term(s):", max_grade)
       print("Minimum grade(s) and in which term(s):", min_grade)
       # ask if the student has any repeated courses
       repeated_courses = input("Do you have any repeated course(s)? (yes/no): ")

       # write the calculated statistics to a text file
       with open(r"C:\Users\ASUS DEMO\Downloads\std202330600Statistics.txt", "w") as f:
           f.write("=" * 55 + "\n")
           f.write("*" * 10 + " " * 7 + "Undergraduate Level" + " " * 7 + "*" * 10 + "\n")
           f.write("=" * 55 + "\n")
           f.write("Overall average (major and minor) for all terms: {}\n".format(overall_average_all_term))
           f.write("Average (major and minor) for each terms:  \n")
           f.write("        Term 1 : {}\n".format(average_first_term))
           f.write("        Term 2 : {}\n".format(average_second_term))
           f.write("Maximum grade(s) and in which term(s) {} \n".format(max_grade))
           f.write("Minimum grade(s) and in which term(s) {}\n".format(min_grade))
           f.write("Do you have any repeated course(s)? {}\n".format(repeated_courses))
           f.write("\n")

    # check if the student ID is 202306000
   elif stdID == '202307000':

       # load data from the CSV file for student 202306000
       stdIDStatistics_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202307000.csv", dtype=str, delimiter=',')

       # calculate the overall average grade for all terms
       overall_average_all_term = (int(*stdIDStatistics_data[1, 7:8]) + int(*stdIDStatistics_data[2, 7:8]) + int(
           *stdIDStatistics_data[3, 7:8]) + int(*stdIDStatistics_data[4, 7:8]) + int(
           *stdIDStatistics_data[5, 7:8]) + int(*stdIDStatistics_data[6, 7:8]) + int(
           *stdIDStatistics_data[7, 7:8]) + int(*stdIDStatistics_data[8, 7:8])) / 8

       # calculate the average grade for the first term
       average_first_term = (int(*stdIDStatistics_data[1, 7:8]) + int(*stdIDStatistics_data[2, 7:8]) + int(
           *stdIDStatistics_data[3, 7:8]) + int(*stdIDStatistics_data[4, 7:8])) / 4

       # calculate the average grade for the second term
       average_second_term = (int(*stdIDStatistics_data[5, 7:8]) + int(*stdIDStatistics_data[6, 7:8]) + int(
           *stdIDStatistics_data[7, 7:8]) + int(*stdIDStatistics_data[8, 7:8])) / 4

       # load grades data from the CSV file for student 202306000
       grades = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202307000.csv", delimiter=',', skiprows=1, usecols=(7,))
       # find the maximum grade
       max_grade = np.max(grades)
       # find the minimum grade
       min_grade = np.min(grades)

       # print the header for the output
       print("=" * 55)
       print("*" * 10 + " " * 7, "Undergraduate Level", " " * 7 + "*" * 10)
       print("=" * 55)

       # print the calculated statistics
       print("Overall average (major and minor) for all terms:", overall_average_all_term)
       print("Average (major and minor) for each terms:  \n ""    Term 1:", average_first_term, "\n ""    Term 2:",
             average_second_term)
       print("Maximum grade(s) and in which term(s):", max_grade)
       print("Minimum grade(s) and in which term(s):", min_grade)

       # ask if the student has any repeated courses
       repeated_courses = input("Do you have any repeated course(s)? (yes/no): ")

       # ask if the student has any repeated courses
       with open(r"C:\Users\ASUS DEMO\Downloads\std20230700Statistics.txt", "w") as f:
           f.write("=" * 55 + "\n")
           f.write("*" * 10 + " " * 7 + "Undergraduate Level" + " " * 7 + "*" * 10 + "\n")
           f.write("=" * 55 + "\n")
           f.write("Overall average (major and minor) for all terms: {}\n".format(overall_average_all_term))
           f.write("Average (major and minor) for each terms:  \n")
           f.write("        Term 1 : {}\n".format(average_first_term))
           f.write("        Term 2 : {}\n".format(average_second_term))
           f.write("Maximum grade(s) and in which term(s) {} \n".format(max_grade))
           f.write("Minimum grade(s) and in which term(s) {}\n".format(min_grade))
           f.write("Do you have any repeated course(s)? {}\n".format(repeated_courses))
           f.write("\n")

       print("\nLoading...\n")
       time.sleep(3)

   menuFeature(stdID)

# defining the majorTranscriptFeature function that takes stdID as an argument
def majorTrascriptFeature(stdID):
   # checking if the given stdID is equal to '202306000'
  if stdID == '202306000':
      # checking if the given stdID is equal to '202306000'
     studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')
      # printing the student details
     print("Name:", *studentDetails_data[1, 2:3],   "    stdID:", *studentDetails_data[1, 1:2])
     print("College:", *studentDetails_data[1, 4:5], "      Department:", *studentDetails_data[1, 4:5])
     print("Major:", *studentDetails_data[1, 7:8], "     Minor", *studentDetails_data[1, 8:9])
     print("Level:", *studentDetails_data[1, 5:6], " " * 18, "Number of terms: ", *studentDetails_data[1, 9:10])

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 1", " " * 10 + "*" * 14)
     print("=" * 56)

      # loading the major transcript data for term 1 and calculating the averages
     stdIDMajorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202306000.csv", dtype=str, delimiter=',')
     major_average_first_term = (int(*stdIDMajorTranscript_data[1, 7:8]) + int(*stdIDMajorTranscript_data[2, 7:8])) / 2
     major_average_second_term = (int(*stdIDMajorTranscript_data[5, 7:8]) + int(*stdIDMajorTranscript_data[6, 7:8])) / 2
     overall_average = (major_average_first_term + major_average_second_term) / 2

      # printing the major transcript data for term 1
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMajorTranscript_data[1, 4:5], " " * 9, *stdIDMajorTranscript_data[1, 3:4], "      ", *stdIDMajorTranscript_data[1, 6:7], " " * 13, *stdIDMajorTranscript_data[1, 7:8])
     print(*stdIDMajorTranscript_data[2, 4:5], " " * 9, *stdIDMajorTranscript_data[2, 3:4], "      ", *stdIDMajorTranscript_data[2, 6:7], " " * 13, *stdIDMajorTranscript_data[2, 7:8])
     print("Major Average = ", major_average_first_term, " " * 7,    "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 2", " " * 10 + "*" * 14)
     print("=" * 56)

      # printing the major transcript data for term 2
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMajorTranscript_data[5, 4:5], " " * 9, *stdIDMajorTranscript_data[5, 3:4], "      ", *stdIDMajorTranscript_data[5, 6:7], " " * 13, *stdIDMajorTranscript_data[5, 7:8])
     print(*stdIDMajorTranscript_data[6, 4:5], " " * 9, *stdIDMajorTranscript_data[6, 3:4], "      ", *stdIDMajorTranscript_data[6, 6:7], " " * 13, *stdIDMajorTranscript_data[6, 7:8])
     print("Major Average = ", major_average_second_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 10, "End of Transcript for Level", "(", *studentDetails_data[1, 5:6], ")", "*" * 10)
     print("=" * 56)

      # Open a file in write mode and write student details and transcript data to it
     with open(r"C:\Users\ASUS DEMO\Downloads\std202306000MajorTranscript.txt", "w") as f:

         # Write student details to the file
         f.write("Name: {}    stdID:{}\n".format(*studentDetails_data[1, 2:3], *studentDetails_data[1, 1:2]))
         f.write("College: {}      Department: {}\n".format(*studentDetails_data[1, 4:5], *studentDetails_data[1, 4:5]))
         f.write("Major: {}     Minor {}\n".format(*studentDetails_data[1, 7:8], *studentDetails_data[1, 8:9]))
         f.write("Level: {}                   Number of terms: {}\n".format(*studentDetails_data[1, 5:6], *studentDetails_data[1, 9:10]))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 1" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[1, 4:5], *stdIDMajorTranscript_data[1, 3:4], *stdIDMajorTranscript_data[1, 6:7], *stdIDMajorTranscript_data[1, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[2, 4:5], *stdIDMajorTranscript_data[2, 3:4], *stdIDMajorTranscript_data[2, 6:7], *stdIDMajorTranscript_data[2, 7:8]))
         f.write("Major Average = {}        Overall Average = {}\n".format(major_average_first_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 2" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[5, 4:5], *stdIDMajorTranscript_data[5, 3:4],  *stdIDMajorTranscript_data[5, 6:7], *stdIDMajorTranscript_data[5, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[6, 4:5], *stdIDMajorTranscript_data[6, 3:4], *stdIDMajorTranscript_data[6, 6:7], *stdIDMajorTranscript_data[6, 7:8]))
         f.write("Major Average = {}        Overall Average = {}\n".format(major_average_second_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 10 + "End of Transcript for Level" + "(U)" + "*" * 10 + "\n")
         f.write("=" * 56 + "\n")

     print("\nLoading...\n")
     time.sleep(3)
     menuFeature(stdID)

  # check if the student ID matches
  elif stdID == '202307000':
      # load student details from a CSV file
     studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')
      # print out student details
     print("Name:", *studentDetails_data[2, 2:3],   "       stdID:", *studentDetails_data[2, 1:2])
     print("College:", *studentDetails_data[2, 4:5], "      Department:", *studentDetails_data[2, 4:5])
     print("Major:", *studentDetails_data[2, 7:8], "      Minor", *studentDetails_data[2, 8:9])
     print("Level:", *studentDetails_data[2, 5:6], " " * 18, "Number of terms: ", *studentDetails_data[2, 9:10])

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 1", " " * 10 + "*" * 14)
     print("=" * 56)

      # load the student's transcript for the major from a CSV file
     stdIDMajorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\DEMO\202307000.csv", dtype=str, delimiter=',')
     major_average_first_term = (int(*stdIDMajorTranscript_data[1, 7:8]) + int(*stdIDMajorTranscript_data[2, 7:8])) / 2
     major_average_second_term = (int(*stdIDMajorTranscript_data[5, 7:8]) + int(*stdIDMajorTranscript_data[6, 7:8])) / 2
     overall_average = (major_average_first_term + major_average_second_term) / 2

      # print out the courses for the first term and their grades
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMajorTranscript_data[1, 4:5], " " * 9, *stdIDMajorTranscript_data[1, 3:4], "      ", *stdIDMajorTranscript_data[1, 6:7], " " * 13, *stdIDMajorTranscript_data[1, 7:8])
     print(*stdIDMajorTranscript_data[2, 4:5], " " * 9, *stdIDMajorTranscript_data[2, 3:4], "      ", *stdIDMajorTranscript_data[2, 6:7], " " * 13, *stdIDMajorTranscript_data[2, 7:8])
     print("Major Average = ", major_average_first_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 2", " " * 10 + "*" * 14)
     print("=" * 56)

      # print out the courses for the second term and their grades
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMajorTranscript_data[5, 4:5], " " * 9, *stdIDMajorTranscript_data[5, 3:4], "      ", *stdIDMajorTranscript_data[5, 6:7], " " * 13, *stdIDMajorTranscript_data[5, 7:8])
     print(*stdIDMajorTranscript_data[6, 4:5], " " * 9, *stdIDMajorTranscript_data[6, 3:4], "      ", *stdIDMajorTranscript_data[6, 6:7], " " * 13, *stdIDMajorTranscript_data[6, 7:8])
     print("Major Average = ", major_average_second_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 10, "End of Transcript for Level", "(", *studentDetails_data[1, 5:6], ")", "*" * 10)
     print("=" * 56)

      # Open a file in write mode and write student details and transcript data to it
     with open(r"C:\Users\ASUS DEMO\Downloads\std202307000MajorTranscript.txt", "w") as f:

         # Write student details to the file
         f.write("Name: {}       stdID:{}\n".format(*studentDetails_data[2, 2:3], *studentDetails_data[2, 1:2]))
         f.write(
             "College: {}      Department: {}\n".format(*studentDetails_data[2, 4:5], *studentDetails_data[2, 4:5]))
         f.write("Major: {}      Minor {}\n".format(*studentDetails_data[2, 7:8], *studentDetails_data[2, 8:9]))
         f.write("Level: {}                   Number of terms: {}\n".format(*studentDetails_data[2, 5:6],*studentDetails_data[2, 9:10]))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 1" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[1, 4:5], *stdIDMajorTranscript_data[1, 3:4], *stdIDMajorTranscript_data[1, 6:7], *stdIDMajorTranscript_data[1, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[2, 4:5], *stdIDMajorTranscript_data[2, 3:4], *stdIDMajorTranscript_data[2, 6:7], *stdIDMajorTranscript_data[2, 7:8]))
         f.write("Major Average = {}        Overall Average = {}\n".format(major_average_first_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 2" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[5, 4:5], *stdIDMajorTranscript_data[5, 3:4], *stdIDMajorTranscript_data[5, 6:7], *stdIDMajorTranscript_data[5, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[6, 4:5], *stdIDMajorTranscript_data[6, 3:4], *stdIDMajorTranscript_data[6, 6:7], *stdIDMajorTranscript_data[6, 7:8]))
         f.write(
             "Major Average = {}        Overall Average = {}\n".format(major_average_second_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 10 + "End of Transcript for Level" + "(U)" + "*" * 10 + "\n")
         f.write("=" * 56 + "\n")

     print("\nLoading...\n")
     time.sleep(3)
     menuFeature(stdID)

# define a function named minorTranscriptFeature that takes a student ID as input
def minorTranscriptFeature(stdID):
    # if the student ID is equal to '202306000', proceed with the following code
 if stdID == '202306000':
     # load student details data from a CSV file and store it in a variable named studentDetails_data
     studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')
     # print the student's name and ID, college, department, major, level, and number of terms
     print("Name:", *studentDetails_data[1, 2:3],   "    stdID:", *studentDetails_data[1, 1:2])
     print("College:", *studentDetails_data[1, 4:5], "      Department:", *studentDetails_data[1, 4:5])
     print("Major:", *studentDetails_data[1, 7:8], "     Minor", *studentDetails_data[1, 8:9])
     print("Level:", *studentDetails_data[1, 5:6], " " * 18, "Number of terms: ", *studentDetails_data[1, 9:10])

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 1", " " * 10 + "*" * 14)
     print("=" * 56)

     # load minor transcript data for the student from a CSV file and store it in a variable named stdIDMinorTranscript_data
     stdIDMinorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202306000.csv", dtype=str, delimiter=',')
     minor_average_first_term = (int(*stdIDMinorTranscript_data[3, 7:8]) + int(*stdIDMinorTranscript_data[4, 7:8])) / 2
     minor_average_second_term = (int(*stdIDMinorTranscript_data[7, 7:8]) + int(*stdIDMinorTranscript_data[8, 7:8])) / 2
     overall_average = (minor_average_first_term + minor_average_second_term) / 2

     # print the header for the transcript table, including course ID, course name, credit hours, and grade for first term
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMinorTranscript_data[3, 4:5], " " * 9, *stdIDMinorTranscript_data[3, 3:4], "      ", *stdIDMinorTranscript_data[3, 6:7], " " * 13, *stdIDMinorTranscript_data[3, 7:8])
     print(*stdIDMinorTranscript_data[4, 4:5], " " * 9, *stdIDMinorTranscript_data[4, 3:4], "      ", *stdIDMinorTranscript_data[4, 6:7], " " * 13, *stdIDMinorTranscript_data[4, 7:8])
     print("Minor Average = ", minor_average_first_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 2", " " * 10 + "*" * 14)
     print("=" * 56)

     # print the header for the transcript table, including course ID, course name, credit hours, and grade for second term
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMinorTranscript_data[7, 4:5], " " * 9, *stdIDMinorTranscript_data[7, 3:4], "      ", *stdIDMinorTranscript_data[7, 6:7], " " * 13, *stdIDMinorTranscript_data[7, 7:8])
     print(*stdIDMinorTranscript_data[8, 4:5], " " * 9, *stdIDMinorTranscript_data[8, 3:4], "      ", *stdIDMinorTranscript_data[8, 6:7], " " * 13, *stdIDMinorTranscript_data[8, 7:8])
     print("Minor Average = ", minor_average_second_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 10, "End of Transcript for Level", "(", *studentDetails_data[1, 5:6], ")", "*" * 10)
     print("=" * 56)

     # Open a file in write mode and write student details and transcript data to it
     with open(r"C:\Users\ASUS DEMO\Downloads\std202306000MinorTranscript.txt", "w") as f:

         # Write student details to the file
         f.write("Name: {}    stdID:{}\n".format(*studentDetails_data[1, 2:3], *studentDetails_data[1, 1:2]))
         f.write("College: {}      Department: {}\n".format(*studentDetails_data[1, 4:5], *studentDetails_data[1, 4:5]))
         f.write("Minor: {}     Minor {}\n".format(*studentDetails_data[1, 7:8], *studentDetails_data[1, 8:9]))
         f.write("Level: {}                   Number of terms: {}\n".format(*studentDetails_data[1, 5:6], *studentDetails_data[1, 9:10]))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 1" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[3, 4:5], *stdIDMinorTranscript_data[3, 3:4], *stdIDMinorTranscript_data[3, 6:7], *stdIDMinorTranscript_data[3, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[4, 4:5], *stdIDMinorTranscript_data[4, 3:4], *stdIDMinorTranscript_data[4, 6:7], *stdIDMinorTranscript_data[4, 7:8]))
         f.write("Minor Average = {}        Overall Average = {}\n".format(minor_average_first_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 2" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[7, 4:5], *stdIDMinorTranscript_data[7, 3:4],  *stdIDMinorTranscript_data[7, 6:7], *stdIDMinorTranscript_data[7, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[8, 4:5], *stdIDMinorTranscript_data[8, 3:4], *stdIDMinorTranscript_data[8, 6:7], *stdIDMinorTranscript_data[8, 7:8]))
         f.write("Minor Average = {}        Overall Average = {}\n".format(minor_average_second_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 10 + "End of Transcript for Level" + "(U)" + "*" * 10 + "\n")
         f.write("=" * 56 + "\n")

     print("\nLoading...\n")
     time.sleep(3)
     menuFeature(stdID)

 # if the student ID is equal to '202307000', proceed with the following code
 elif stdID == '202307000':
     # load student details data from a CSV file and store it in a variable named studentDetails_data
     studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')
     print("Name:", *studentDetails_data[2, 2:3],   "       stdID:", *studentDetails_data[2, 1:2])
     print("College:", *studentDetails_data[2, 4:5], "      Department:", *studentDetails_data[2, 4:5])
     print("Major:", *studentDetails_data[2, 7:8], "      Minor", *studentDetails_data[2, 8:9])
     print("Level:", *studentDetails_data[2, 5:6], " " * 18, "Number of terms: ", *studentDetails_data[2, 9:10])

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 1", " " * 10 + "*" * 14)
     print("=" * 56)

     # load minor transcript data for the student from a CSV file and store it in a variable named stdIDMinorTranscript_data
     stdIDMinorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202307000.csv", dtype=str, delimiter=',')
     minor_average_first_term = (int(*stdIDMinorTranscript_data[3, 7:8]) + int(*stdIDMinorTranscript_data[4, 7:8])) / 2
     minor_average_second_term = (int(*stdIDMinorTranscript_data[7, 7:8]) + int(*stdIDMinorTranscript_data[8, 7:8])) / 2
     overall_average = (minor_average_first_term + minor_average_second_term) / 2

     # print the header for the transcript table, including course ID, course name, credit hours, and grade for first term
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMinorTranscript_data[3, 4:5], " " * 8, *stdIDMinorTranscript_data[3, 3:4], "      ", *stdIDMinorTranscript_data[3, 6:7], " " * 13, *stdIDMinorTranscript_data[3, 7:8])
     print(*stdIDMinorTranscript_data[4, 4:5], " " * 9, *stdIDMinorTranscript_data[4, 3:4], "      ", *stdIDMinorTranscript_data[4, 6:7], " " * 13, *stdIDMinorTranscript_data[4, 7:8])
     print("Minor Average = ", minor_average_first_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 2", " " * 10 + "*" * 14)
     print("=" * 56)

     # print the header for the transcript table, including course ID, course name, credit hours, and grade for second term
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMinorTranscript_data[7, 4:5], " " * 9, *stdIDMinorTranscript_data[7, 3:4], "      ", *stdIDMinorTranscript_data[7, 6:7], " " * 13, *stdIDMinorTranscript_data[7, 7:8])
     print(*stdIDMinorTranscript_data[8, 4:5], " " * 9, *stdIDMinorTranscript_data[8, 3:4], "      ", *stdIDMinorTranscript_data[8, 6:7], " " * 13, *stdIDMinorTranscript_data[8, 7:8])
     print("Minor Average = ", minor_average_second_term, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 10, "End of Transcript for Level", "(", *studentDetails_data[1, 5:6], ")", "*" * 10)
     print("=" * 56)

     # Open a file in write mode and write student details and transcript data to it
     with open(r"C:\Users\ASUS DEMO\Downloads\std202307000MinorTranscript.txt", "w") as f:
         # Write student details to the file
         f.write("Name: {}       stdID:{}\n".format(*studentDetails_data[2, 2:3], *studentDetails_data[2, 1:2]))
         f.write("College: {}      Department: {}\n".format(*studentDetails_data[2, 4:5], *studentDetails_data[2, 4:5]))
         f.write("Major: {}      Minor {}\n".format(*studentDetails_data[2, 7:8], *studentDetails_data[2, 8:9]))
         f.write("Level: {}                   Number of terms: {}\n".format(*studentDetails_data[2, 5:6],*studentDetails_data[2, 9:10]))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 1" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}         {}      {}             {}\n".format(*stdIDMinorTranscript_data[3, 4:5], *stdIDMinorTranscript_data[3, 3:4], *stdIDMinorTranscript_data[3, 6:7], *stdIDMinorTranscript_data[3, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[4, 4:5], *stdIDMinorTranscript_data[4, 3:4], *stdIDMinorTranscript_data[4, 6:7], *stdIDMinorTranscript_data[4, 7:8]))
         f.write("Minor Average = {}        Overall Average = {}\n".format(minor_average_first_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 2" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[7, 4:5], *stdIDMinorTranscript_data[7, 3:4], *stdIDMinorTranscript_data[7, 6:7], *stdIDMinorTranscript_data[7, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[8, 4:5], *stdIDMinorTranscript_data[8, 3:4], *stdIDMinorTranscript_data[8, 6:7], *stdIDMinorTranscript_data[8, 7:8]))
         f.write("Minor Average = {}        Overall Average = {}\n".format(minor_average_second_term, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 10 + "End of Transcript for Level" + "(U)" + "*" * 10 + "\n")
         f.write("=" * 56 + "\n")

 print("\nLoading...\n")
 time.sleep(3)
 menuFeature(stdID)

# This function is used to display the full transcript for a specific student ID.
# The implementation of this function may depend on the data format and storage used for student transcripts.
def fullTrascriptFeature(stdID):
    # check if the student ID is valid and matches a record in the studentDetails.csv file
  if stdID == '202306000':
      # load the student details from the studentDetails.csv file into a numpy array
     studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')
      # print the student's name, ID, college, department, major, level, and number of terms
     print("Name:", *studentDetails_data[1, 2:3],   "    stdID:", *studentDetails_data[1, 1:2])
     print("College:", *studentDetails_data[1, 4:5], "      Department:", *studentDetails_data[1, 4:5])
     print("Major:", *studentDetails_data[1, 7:8], "     Minor", *studentDetails_data[1, 8:9])
     print("Level:", *studentDetails_data[1, 5:6], " " * 18, "Number of terms: ", *studentDetails_data[1, 9:10])

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 1", " " * 10 + "*" * 14)
     print("=" * 56)

      # load the major and minor transcripts from the 202306000.csv file into numpy arrays
     stdIDMajorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202306000.csv", dtype=str, delimiter=',')
     stdIDMinorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202306000.csv", dtype=str, delimiter=',')

      # calculate the averages for the major and minor courses in the first and second terms
     major_average_first_term = (int(*stdIDMajorTranscript_data[1, 7:8]) + int(*stdIDMajorTranscript_data[2, 7:8])) / 2
     major_average_second_term = (int(*stdIDMajorTranscript_data[5, 7:8]) + int(*stdIDMajorTranscript_data[6, 7:8])) / 2
     minor_average_first_term = (int(*stdIDMinorTranscript_data[3, 7:8]) + int(*stdIDMinorTranscript_data[4, 7:8])) / 2
     minor_average_second_term = (int(*stdIDMinorTranscript_data[7, 7:8]) + int(*stdIDMinorTranscript_data[8, 7:8])) / 2

      # calculate the first term average, second term average, and overall average
     first_term_average = (minor_average_first_term + major_average_first_term) / 2
     second_term_average = (minor_average_second_term + major_average_second_term) / 2
     overall_average = (first_term_average + second_term_average) / 2

      # print the course ID, course name, credit hours, and grade for the major and minor courses in the first term
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMajorTranscript_data[1, 4:5], " " * 9, *stdIDMajorTranscript_data[1, 3:4], "      ", *stdIDMajorTranscript_data[1, 6:7], " " * 13, *stdIDMajorTranscript_data[1, 7:8])
     print(*stdIDMajorTranscript_data[2, 4:5], " " * 9, *stdIDMajorTranscript_data[2, 3:4], "      ", *stdIDMajorTranscript_data[2, 6:7], " " * 13, *stdIDMajorTranscript_data[2, 7:8])

     print(*stdIDMinorTranscript_data[3, 4:5], " " * 9, *stdIDMinorTranscript_data[3, 3:4], "      ", *stdIDMinorTranscript_data[3, 6:7], " " * 13, *stdIDMinorTranscript_data[3, 7:8])
     print(*stdIDMinorTranscript_data[4, 4:5], " " * 9, *stdIDMinorTranscript_data[4, 3:4], "      ", *stdIDMinorTranscript_data[4, 6:7], " " * 13, *stdIDMinorTranscript_data[4, 7:8])
     print("Major Average = ", major_average_first_term, " " * 7, "Minor Average = ", minor_average_first_term)
     print("Term Average = ", first_term_average, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 14 + " " * 10, "Term 2", " " * 10 + "*" * 14)
     print("=" * 56)

      # print the course ID, course name, credit hours, and grade for the major and minor courses in the second term
     print("Course ID", "    course name", "    credit hours", "   grade")
     print(*stdIDMajorTranscript_data[5, 4:5], " " * 9, *stdIDMajorTranscript_data[5, 3:4], "      ", *stdIDMajorTranscript_data[5, 6:7], " " * 13, *stdIDMajorTranscript_data[5, 7:8])
     print(*stdIDMajorTranscript_data[6, 4:5], " " * 9, *stdIDMajorTranscript_data[6, 3:4], "      ", *stdIDMajorTranscript_data[6, 6:7], " " * 13, *stdIDMajorTranscript_data[6, 7:8])

     print(*stdIDMinorTranscript_data[7, 4:5], " " * 9, *stdIDMinorTranscript_data[7, 3:4], "      ", *stdIDMinorTranscript_data[7, 6:7], " " * 13, *stdIDMinorTranscript_data[7, 7:8])
     print(*stdIDMinorTranscript_data[8, 4:5], " " * 9, *stdIDMinorTranscript_data[8, 3:4], "      ", *stdIDMinorTranscript_data[8, 6:7], " " * 13, *stdIDMinorTranscript_data[8, 7:8])
     print("Major Average = ", major_average_second_term, " " * 7, "Minor Average = ", minor_average_second_term)
     print("Term Average = ", second_term_average, " " * 7, "Overall Average = ", overall_average)

     print("=" * 56)
     print("*" * 10, "End of Transcript for Level", "(", *studentDetails_data[1, 5:6], ")", "*" * 10)
     print("=" * 56)

      # Open a file in write mode and write student details and transcript data to it
     with open(r"C:\Users\ASUS DEMO\Downloads\std202306000FullTranscript.txt", "w") as f:
         # Write student details to the file
         f.write("Name: {}    stdID:{}\n".format(*studentDetails_data[1, 2:3], *studentDetails_data[1, 1:2]))
         f.write("College: {}      Department: {}\n".format(*studentDetails_data[1, 4:5], *studentDetails_data[1, 4:5]))
         f.write("Major: {}     Minor {}\n".format(*studentDetails_data[1, 7:8], *studentDetails_data[1, 8:9]))
         f.write("Level: {}                   Number of terms: {}\n".format(*studentDetails_data[1, 5:6], *studentDetails_data[1, 9:10]))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 1" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[1, 4:5], *stdIDMajorTranscript_data[1, 3:4], *stdIDMajorTranscript_data[1, 6:7], *stdIDMajorTranscript_data[1, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[2, 4:5], *stdIDMajorTranscript_data[2, 3:4], *stdIDMajorTranscript_data[2, 6:7], *stdIDMajorTranscript_data[2, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[3, 4:5], *stdIDMinorTranscript_data[3, 3:4], *stdIDMinorTranscript_data[3, 6:7], *stdIDMinorTranscript_data[3, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[4, 4:5], *stdIDMinorTranscript_data[4, 3:4], *stdIDMinorTranscript_data[4, 6:7], *stdIDMinorTranscript_data[4, 7:8]))

         f.write("Major Average = {}        Minor Average = {}\n".format(major_average_first_term, minor_average_first_term))
         f.write("Term Average = {}        Overall Average = {}\n".format(first_term_average, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 14 + " " * 10 + "Term 2" + " " * 10 + "*" * 14 + "\n")
         f.write("=" * 56 + "\n")

         f.write("Course ID    course name    credit hours   grade\n")
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[5, 4:5], *stdIDMajorTranscript_data[5, 3:4], *stdIDMajorTranscript_data[5, 6:7], *stdIDMajorTranscript_data[5, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[6, 4:5], *stdIDMajorTranscript_data[6, 3:4], *stdIDMajorTranscript_data[6, 6:7], *stdIDMajorTranscript_data[6, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[7, 4:5], *stdIDMinorTranscript_data[7, 3:4], *stdIDMinorTranscript_data[7, 6:7], *stdIDMinorTranscript_data[7, 7:8]))
         f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[8, 4:5], *stdIDMinorTranscript_data[8, 3:4], *stdIDMinorTranscript_data[8, 6:7], *stdIDMinorTranscript_data[8, 7:8]))

         f.write("Major Average = {}        Minor Average = {}\n".format(major_average_second_term, minor_average_second_term))
         f.write("Term Average = {}        Overall Average = {}\n".format(second_term_average, overall_average))

         f.write("=" * 56 + "\n")
         f.write("*" * 10 + "    End of Transcript for Level    " + "(U)" + "*" * 10 + "\n")
         f.write("=" * 56 + "\n")

     print("\nLoading...\n")
     time.sleep(3)
     menuFeature(stdID)

    # check if the student ID is valid and matches a record in the studentDetails.csv file
  if stdID == '202307000':
      # load the student details from the studentDetails.csv file into a numpy array
      studentDetails_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\studentDetails.csv", dtype=str, delimiter=',')
      print("Name:", *studentDetails_data[1, 2:3], "    stdID:", *studentDetails_data[1, 1:2])
      print("College:", *studentDetails_data[1, 4:5], "      Department:", *studentDetails_data[1, 4:5])
      print("Major:", *studentDetails_data[1, 7:8], "     Minor", *studentDetails_data[1, 8:9])
      print("Level:", *studentDetails_data[1, 5:6], " " * 18, "Number of terms: ", *studentDetails_data[1, 9:10])

      print("=" * 56)
      print("*" * 14 + " " * 10, "Term 1", " " * 10 + "*" * 14)
      print("=" * 56)

      # load the major and minor transcripts from the 202306000.csv file into numpy arrays
      stdIDMajorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202307000.csv", dtype=str, delimiter=',')
      stdIDMinorTranscript_data = np.loadtxt(r"C:\Users\ASUS DEMO\Downloads\202307000.csv", dtype=str, delimiter=',')

      # calculate the averages for the major and minor courses in the first and second terms
      major_average_first_term = (int(*stdIDMajorTranscript_data[1, 7:8]) + int(
          *stdIDMajorTranscript_data[2, 7:8])) / 2
      major_average_second_term = (int(*stdIDMajorTranscript_data[5, 7:8]) + int(
          *stdIDMajorTranscript_data[6, 7:8])) / 2
      minor_average_first_term = (int(*stdIDMinorTranscript_data[3, 7:8]) + int(
          *stdIDMinorTranscript_data[4, 7:8])) / 2
      minor_average_second_term = (int(*stdIDMinorTranscript_data[7, 7:8]) + int(
          *stdIDMinorTranscript_data[8, 7:8])) / 2

      # calculate the first term average, second term average, and overall average
      first_term_average = (minor_average_first_term + major_average_first_term) / 2
      second_term_average = (minor_average_second_term + major_average_second_term) / 2
      overall_average = (first_term_average + second_term_average) / 2

      print("Course ID", "    course name", "    credit hours", "   grade")
      print(*stdIDMajorTranscript_data[1, 4:5], " " * 9, *stdIDMajorTranscript_data[1, 3:4], "      ",
            *stdIDMajorTranscript_data[1, 6:7], " " * 13, *stdIDMajorTranscript_data[1, 7:8])
      print(*stdIDMajorTranscript_data[2, 4:5], " " * 9, *stdIDMajorTranscript_data[2, 3:4], "      ",
            *stdIDMajorTranscript_data[2, 6:7], " " * 13, *stdIDMajorTranscript_data[2, 7:8])

      print(*stdIDMinorTranscript_data[3, 4:5], " " * 8, *stdIDMinorTranscript_data[3, 3:4], "     ",
            *stdIDMinorTranscript_data[3, 6:7], " " * 13, *stdIDMinorTranscript_data[3, 7:8])
      print(*stdIDMinorTranscript_data[4, 4:5], " " * 9, *stdIDMinorTranscript_data[4, 3:4], "      ",
            *stdIDMinorTranscript_data[4, 6:7], " " * 13, *stdIDMinorTranscript_data[4, 7:8])
      print("Major Average = ", major_average_first_term, " " * 7, "Minor Average = ", minor_average_first_term)
      print("Term Average = ", first_term_average, " " * 7, "Overall Average = ", overall_average)

      print("=" * 56)
      print("*" * 14 + " " * 10, "Term 2", " " * 10 + "*" * 14)
      print("=" * 56)

      print("Course ID", "    course name", "    credit hours", "   grade")
      print(*stdIDMajorTranscript_data[5, 4:5], " " * 9, *stdIDMajorTranscript_data[5, 3:4], "      ",
            *stdIDMajorTranscript_data[5, 6:7], " " * 13, *stdIDMajorTranscript_data[5, 7:8])
      print(*stdIDMajorTranscript_data[6, 4:5], " " * 9, *stdIDMajorTranscript_data[6, 3:4], "      ",
            *stdIDMajorTranscript_data[6, 6:7], " " * 13, *stdIDMajorTranscript_data[6, 7:8])

      print(*stdIDMinorTranscript_data[7, 4:5], " " * 9, *stdIDMinorTranscript_data[7, 3:4], "      ",
            *stdIDMinorTranscript_data[7, 6:7], " " * 13, *stdIDMinorTranscript_data[7, 7:8])
      print(*stdIDMinorTranscript_data[8, 4:5], " " * 9, *stdIDMinorTranscript_data[8, 3:4], "      ",
            *stdIDMinorTranscript_data[8, 6:7], " " * 13, *stdIDMinorTranscript_data[8, 7:8])
      print("Major Average = ", major_average_second_term, " " * 7, "Minor Average = ", minor_average_second_term)
      print("Term Average = ", second_term_average, " " * 7, "Overall Average = ", overall_average)

      print("=" * 56)
      print("*" * 10, "End of Transcript for Level", "(", *studentDetails_data[1, 5:6], ")", "*" * 10)
      print("=" * 56)

      # Open a file in write mode and write student details and transcript data to it
      with open(r"C:\Users\ASUS DEMO\Downloads\std202307000FullTranscript.txt", "w") as f:
          # Write student details to the file
          f.write("Name: {}    stdID:{}\n".format(*studentDetails_data[1, 2:3], *studentDetails_data[1, 1:2]))
          f.write(
              "College: {}      Department: {}\n".format(*studentDetails_data[1, 4:5], *studentDetails_data[1, 4:5]))
          f.write("Major: {}     Minor {}\n".format(*studentDetails_data[1, 7:8], *studentDetails_data[1, 8:9]))
          f.write("Level: {}                   Number of terms: {}\n".format(*studentDetails_data[1, 5:6],
                                                                             *studentDetails_data[1, 9:10]))

          f.write("=" * 56 + "\n")
          f.write("*" * 14 + " " * 10 + " Term 1 " + " " * 10 + "*" * 14 + "\n")
          f.write("=" * 56 + "\n")

          f.write("Course ID    course name    credit hours   grade\n")
          f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[1, 4:5], *stdIDMajorTranscript_data[1, 3:4], *stdIDMajorTranscript_data[1, 6:7], *stdIDMajorTranscript_data[1, 7:8]))
          f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[2, 4:5], *stdIDMajorTranscript_data[2, 3:4], *stdIDMajorTranscript_data[2, 6:7], *stdIDMajorTranscript_data[2, 7:8]))
          f.write("{}         {}      {}               {}\n".format(*stdIDMinorTranscript_data[3, 4:5], *stdIDMinorTranscript_data[3, 3:4], *stdIDMinorTranscript_data[3, 6:7], *stdIDMinorTranscript_data[3, 7:8]))
          f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[4, 4:5], *stdIDMinorTranscript_data[4, 3:4], *stdIDMinorTranscript_data[4, 6:7], *stdIDMinorTranscript_data[4, 7:8]))

          f.write("Major Average = {}        Minor Average = {}\n".format(major_average_first_term, minor_average_first_term))
          f.write("Term Average = {}        Overall Average = {}\n".format(first_term_average, overall_average))

          f.write("=" * 56 + "\n")
          f.write("*" * 14 + " " * 10 + " Term 2 " + " " * 10 + "*" * 14 + "\n")
          f.write("=" * 56 + "\n")

          f.write("Course ID    course name    credit hours   grade\n")
          f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[5, 4:5], *stdIDMajorTranscript_data[5, 3:4], *stdIDMajorTranscript_data[5, 6:7], *stdIDMajorTranscript_data[5, 7:8]))
          f.write("{}          {}       {}              {}\n".format(*stdIDMajorTranscript_data[6, 4:5], *stdIDMajorTranscript_data[6, 3:4], *stdIDMajorTranscript_data[6, 6:7], *stdIDMajorTranscript_data[6, 7:8]))
          f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[7, 4:5], *stdIDMinorTranscript_data[7, 3:4], *stdIDMinorTranscript_data[7, 6:7], *stdIDMinorTranscript_data[7, 7:8]))
          f.write("{}          {}       {}              {}\n".format(*stdIDMinorTranscript_data[8, 4:5], *stdIDMinorTranscript_data[8, 3:4], *stdIDMinorTranscript_data[8, 6:7], *stdIDMinorTranscript_data[8, 7:8]))

          f.write("Major Average = {}        Minor Average = {}\n".format(major_average_second_term, minor_average_second_term))
          f.write("Term Average = {}        Overall Average = {}\n".format(second_term_average, overall_average))

          f.write("=" * 56 + "\n")
          f.write("*" * 10 + "    End of Transcript for Level  " + "(U) " + "*" * 10 + "\n")
          f.write("=" * 56 + "\n")

      print("\nLoading...\n")
      time.sleep(3)
      menuFeature(stdID)

def previousRequestFeature(stdID):
        filename = f"std{stdID}PreviousRequests.txt"
        file_path = f"C:\\Users\\ASUS DEMO\\Downloads\\{filename}"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = f.readlines()
            prev_requests = [line.strip().split("\t") for line in lines]
        else:
            prev_requests = []

        # Sort previous requests by date and time
        prev_requests.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Print previous requests
        print("Previous Requests")
        print("=" * 47)
        print("Request\t\tDate\t\tTime")
        print("=" * 47)
        for req in prev_requests:
            print(f"{req[0]}\t\t{req[1]}\t{req[2]}")

        # Get current request information
        option = input("Enter your request type: ")
        date = time.strftime("%d/%m/%Y")
        curr_time = time.strftime("%H:%M")

        # Add current request to previous requests
        prev_requests.append([option, date, curr_time])
        with open(file_path, "w") as f:
            f.write("Previous Requests" + "\n")
            f.write("=" * 47 + "\n")
            f.write("Request\t\tDate\t\tTime" + "\n")
            f.write("=" * 47 + "\n")
            for req in prev_requests:
                f.write("\t".join(req) + "\n")

        # Clear screen, wait a few seconds, and redirect to menu
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        menuFeature(stdID)


# This function is used to implement new features for a specific student ID.
# If the student ID is 202306000 or 202307000, the console screen is cleared (depending on the OS) and a new line is printed
def newStudentFeature(stdID):
    # Check if the student ID is 202306000
  if stdID == '202306000':
      # If yes, clear the console screen (depending on the OS) and print a new line
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\n")
  startFeature()

    # Check if the student ID is 202307000
  if stdID == '202307000':
      # If yes, clear the console screen (depending on the OS) and print a new line
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\n")
  startFeature()

# This function is used to terminate the program for a specific student ID.
def terminateFeature(stdID):
    # Check if the student ID is 202306000
  if stdID == '202306000':

      # Force terminate the program
      os._exit(0)
      # Check if the student ID is 202307000
  if stdID == '202307000':

      # Force terminate the program
      os._exit(0)  # force terminate the program

startFeature()

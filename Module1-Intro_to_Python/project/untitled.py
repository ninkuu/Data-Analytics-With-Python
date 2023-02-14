'''python
Project for Module 1

Goals:
A) Calculate the following statistics for the first 10 columns of the data file:
    Maximum value
    Minimum value
    Average (Mean)
B) Calculate the same set of statistics but for each of the seven wilderness areas. The wilderness areas are identified in columns 11-14 of the data file.
C) Write a new file that contains a report of the statistics calculated.

Rules:
Your program must make use of the following:

1) arguments passed via the command-line
2) use of lists or dictionaries
3) use of functions
4) use of loops
5) proper commenting
6) Your program must not Use global variables (except the exceptions listed below)


'''













# def get_statistics(area_dictionary):
#     for column_number in area_dictionary.keys():
#         print("Minimum {}: {}".format(COLUMNS[column_number], min (area_dictionary[column_number])))
#         print("Maximum {}: {}".format(COLUMNS[column_number], max (area_dictionary[column_number])))
#         print("Mean {}: {}".format(COLUMNS[column_number], round((sum(area_dictionary[column_number])/len(area_dictionary[column_number])))))
#         print("\n")    



# for area in AREAS.keys():
#     if area != 0:
#         print(area)

# def pull_data(area_dictionary, line_cols):
#     for column_number in area_dictionary.keys():
#         area_dictionary[column_number].append(float(line_cols[column_number]))
        
# def call_report(area_dictionary):
#     for column_number in area_dictionary.keys():
#         print("Minimum {}: {}".format(COLUMNS[column_number], min (area_dictioanry[column_number])))
#         print("Maximum {}: {}".format(COLUMNS[column_number], max (area_dictioanry[column_number])))
#         print("Mean {}: {}".format(COLUMNS[column_number], round((sum(area_dictioanry[column_number])/len(area_dictionary[column_number])))))
#         print("\n")
        
# def main()        
#     for row in file:
#         cols = row.split(".")
#         rawah, neota, comanche, cache = int(cols[11]), int(cols[12]), int(cols[13]), int(cols[14])
#         if rawah == 1:
#             pull_data(cols)
#         elif neota == 1:
#             pull_data(cols)
#         elif comanche == 1:
#             pull_data(cols)
#         elif cache == 1:
#             pull_data(cols)
#     call_report(rawah)
#     call_report(neota)
#     call_report(comanche)
#     call_report(cache)
    
# file.close()
    
# if __name__ == "__main__":
#     main()

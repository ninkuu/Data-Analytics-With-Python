'''python
Project for Module 1 by Ninh Khuu

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


AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}
'''
#Global variables that are permitted and associated with the covtype.data file
AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}
COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}       
# Original functions for getting the statistics for each element at a time
# Would have required ten separate functions for each element
# def get_elevation_statistics(raw_data):
#     col1 = extract_column(raw_data, 0)
#     min_stats = min(col1)
#     max_stats = max(col1)
#     avg_stats = sum(col1)/len(col1)
#     return [min_stats,max_stats,avg_stats]
#function to pull the aspect statistics 
#def get_aspect_statistics(raw_data):
#     col2 = extract_column(raw_data, 1)
#     min_stats = min(col2)
#     max_stats = max(col2)
#     avg_stats = sum(col2)/len(col2)
#     return [min_stats,max_stats,avg_stats]

#New get_statistics function that uses two 
#variables so that we can replace the previous function
#stores output from extract_column to pull minimum
#maximum, and average value
def get_statistics(raw_data, column_number):
    column_values = extract_column(raw_data, column_number)
    min_stats = min(column_values)
    max_stats = max(column_values)
    avg_stats = sum(column_values)/len(column_values)
    return [min_stats,max_stats,avg_stats]


#extract_column function to pull each element out of our array for each 
#wilderness area that feeds into the get_statistics function
def extract_column(raw_data,column_number):
    return [item[column_number] for item in raw_data]

# Main function where the work is done.
# Created arrays for each wilderness area and stored them as 2-dimensional lists
# Basically creating a csv for each wilderness area with all 10 elements
def main():
    import sys
    file = open('covtype.data')
    
    rawah_array = []
    neota_array = []
    comanche_peak_array = []
    cache_array = []
    aggregate_array = []
    
    for row in file:
        cols = row.split(",")
        # if cols[10] == "0":
        #     all_array.append(list(map(int,cols[0:10])))
        if cols[10] == "1":
            rawah_array.append(list(map(int,cols[0:10])))
        elif cols[11] == "1":
            neota_array.append(list(map(int,cols[0:10])))
        elif cols[12] == "1":
            comanche_peak_array.append(list(map(int,cols[0:10])))
        elif cols[13] == "1":
            cache_array.append(list(map(int,cols[0:10])))
        aggregate_array.append(list(map(int,cols[0:10])))
    #
    # Original print functions to print out the statistics for each wilderness area
    # Would have had to copy and paste these 5 lines for each of elements
    # Print elevation statistics
    # print("Rawah min, max, and average elevation:",get_elevation_statistics(rawah_array))
    # print("Neota min, max, and average elevation:",get_elevation_statistics(neota_array))
    # print("Comanche peak min, max, and average elevation:",get_elevation_statistics(comanche_peak_array))
    # print("Cache la poudre min, max, and average elevation:",get_elevation_statistics(cache_array))
    # print("Min, max, and average statistics for elevation:",get_elevation_statistics(aggregate_array))
    # #Print aspect statistics for all areas
    # print("Rawah min, max, and average aspect:",get_aspect_statistics(rawah_array))
    # print("Neota min, max, and average aspect:",get_aspect_statistics(neota_array))
    # print("Comanche peak min, max, and average aspect:",get_aspect_statistics(comanche_array))
    # print("Cache la poudre min, max, and average aspect:",get_aspect_statistics(rawah_array))
    # print("Min, max, and average statistics for aspect:",get_aspect_statistics(aggregate_array))
    # Print stats using global variables
    # print("Rawah min, max, and average {}:".format(COLUMNS[0]),get_statistics(rawah_array,0))
    # print("Neota min, max, and average {}:".format(COLUMNS[0]),get_statistics(neota_array,0))
    # print("Comanche peak min, max, and average {}:".format(COLUMNS[0]),get_statistics(comanche_peak_array,0))
    # print("Cache la poudre min, max, and average {}:".format(COLUMNS[0]),get_statistics(cache_array,0))
    # print("Min, max, and average statistics for {}:".format(COLUMNS[0]),get_statistics(aggregate_array,0))    

    #New function to loop based on column number taking advantage of global variables
    with open('project_statistics_output.txt', 'w') as f:
        sys.stdout = f
        for column_number in range(0,10):
            print("Rawah min, max, and average {}:".format(COLUMNS[column_number]),get_statistics(rawah_array,column_number))
            print("Neota min, max, and average {}:".format(COLUMNS[column_number]),get_statistics(neota_array,column_number))
            print("Comanche peak min, max, and average {}:".format(COLUMNS[column_number]),get_statistics(comanche_peak_array,column_number))
            print("Cache la poudre min, max, and average {}:".format(COLUMNS[column_number]),get_statistics(cache_array,column_number))
            print("Total min, max, and average statistics for {}:".format(COLUMNS[column_number]),get_statistics(aggregate_array,column_number))  
            print("\n")

    file.close()                               
if __name__ == "__main__":
    main()

'''
when repeating the same functions, sign you may need to use variables in function.

For lines 121 to 125, use global variables to loop over. 
'''
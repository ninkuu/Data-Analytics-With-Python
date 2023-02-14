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

file = open('covtype.data')
        

def get_elevation_statistics(raw_data):
    col1 = extract_column(raw_data, 0)
    min_stats = min(col1)
    max_stats = max(col1)
    avg_stats = sum(col1)/len(col1)
    return [min_stats,max_stats,avg_stats]

def get_aspect_statistics(raw_data):
    col2 = extract_column(raw_data, 1)
    min_stats = min(col2)
    max_stats = max(col2)
    avg_stats = sum(col2)/len(col2)
    return [min_stats,max_stats,avg_stats]

def extract_column(raw_data,column_number):
    return [item[column_number] for item in raw_data]

def main():
    all_array = []
    rawah_array = []
    neota_array = []
    comanche_peak_array = []
    cache_array = []
    aggregate_array = []
    for row in file:
        cols = row.split(",")
        if cols[10] == "0":
            all_array.append(list(map(int,cols[0:9])))
        elif cols[10] == "1":
            rawah_array.append(list(map(int,cols[0:9])))
        elif cols[10] == "2":
            neota_array.append(list(map(int,cols[0:9])))
        elif cols[10] == "3":
            comanche_peak_array.append(list(map(int,cols[0:9])))
        elif cols[10] == "4":
            cache_array.append(list(map(int,cols[0:9])))
        aggregate_array.append(list(map(int,cols[0:9])))
    
    #Print elevation statistics
    print("Rawah min, max, and average elevation:",get_elevation_statistics(rawah_array))
    print("Neota min, max, and average elevation:",get_elevation_statistics(rawah_array))
    print("Comanche peak min, max, and average elevation:",get_elevation_statistics(rawah_array))
    print("Cache la poudre min, max, and average elevation:",get_elevation_statistics(rawah_array))
    print("Min, max, and average statistics for elevation:",get_elevation_statistics(aggregate_array))
    
    #Print aspect statistics for all areas
    print("Rawah min, max, and average aspect:",get_aspect_statistics(rawah_array))
    print("Neota min, max, and average aspect:",get_aspect_statistics(rawah_array))
    print("Comanche peak min, max, and average aspect:",get_aspect_statistics(rawah_array))
    print("Cache la poudre min, max, and average aspect:",get_aspect_statistics(rawah_array))
    print("Min, max, and average statistics for aspect:",get_aspect_statistics(aggregate_array))
                               
if __name__ == "__main__":
    main()

file.close()

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    bob = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return bob

def read_data_from_web():
    print("Reading data from the Web")
    banana = "Data from the web"
    return banana

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
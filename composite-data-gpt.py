import csv
import copy

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

myInventoryList = []

try:
    with open('car_fleet.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  
        lineCount = 0  
        for row in csvReader:
            if lineCount == 0:
                print(f'Column names are: {", ".join(row)}')  
                lineCount += 1  
            else:  
                print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
                currentVehicle = copy.deepcopy(myVehicle)  
                currentVehicle["vin"] = row[0]  
                currentVehicle["make"] = row[1]  
                currentVehicle["model"] = row[2]  
                currentVehicle["year"] = int(row[3])  # Convert year to integer
                currentVehicle["range"] = int(row[4])  # Convert range to integer
                currentVehicle["topSpeed"] = int(row[5])  # Convert topSpeed to integer
                currentVehicle["zeroSixty"] = float(row[6])  # Convert zeroSixty to float
                currentVehicle["mileage"] = int(row[7])  # Convert mileage to integer
                myInventoryList.append(currentVehicle)  
                lineCount += 1  
        print(f'Processed {lineCount} lines.')

except FileNotFoundError:
    print("Error: The file 'car_fleet.csv' was not found.")
except ValueError as ve:
    print(f"Error: Value error occurred - {ve}")
except Exception as e:
    print(f"An error occurred: {e}")

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
        print("-----")

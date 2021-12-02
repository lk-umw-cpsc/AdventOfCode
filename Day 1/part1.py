inputFileName = "input.txt"
measurement = None
increasedCount = 0
with open(inputFileName) as f:
    for line in f:
        nextMeasurement = int(line)
        if measurement is not None and measurement < nextMeasurement:
            increasedCount += 1
        measurement = nextMeasurement

print(increasedCount)

inputFileName = "input.txt"

sums = [0, 0, 0]
index = 0
poppedSum = 9999999
increasedWindowCount = 0

with open(inputFileName) as f:
    measurement = int(f.readline())
    sums[0] += measurement
    measurement = int(f.readline())
    sums[0] += measurement
    sums[1] += measurement
    for line in f:
        measurement = int(line)
        # Ugly but it works
        sums[0] += measurement
        sums[1] += measurement
        sums[2] += measurement

        sumToBePopped = sums[index]
        
        if poppedSum == 9999999:
            print(sumToBePopped)
        if sumToBePopped > poppedSum:
            increasedWindowCount += 1
        
        poppedSum = sumToBePopped
        sums[index] = 0

        index += 1
        if index > 2:
            index = 0

print(increasedWindowCount)
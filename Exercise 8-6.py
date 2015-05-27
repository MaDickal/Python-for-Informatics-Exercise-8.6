numbers = []
while True:
    numinput = raw_input('Enter a number: ')
# repeatedly reads numbers until 'done' is entered
    if numinput == 'done': break
    else:
        try:
            numinput = int(numinput)
            numinput = float(numinput)
            numbers.append(numinput)
# error message if input is not 'done' or a number
        except:
            print 'Invalid input'
            exit()

print 'Maximum:', max(numbers)
print 'Minimum:', min(numbers)
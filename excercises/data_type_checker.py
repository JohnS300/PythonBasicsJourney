def dataTypeCheck():
    dataForProcessing = input('Input data that you desire to be checked : ')
    dataType = type(dataForProcessing)
    print(f'The data you have inputed are of the following type {dataType}')

if __name__ == '__main__':
    dataTypeCheck()
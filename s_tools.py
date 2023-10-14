from cgi import print_directory
import re

def regDateTester(dataStr):
    regex = re.search("^\d{4}-{1}(0[1-9]|1[0-2])-{1}\d{2}$", dataStr)
    if regex:
        return True
    else:
        print(" >>> failure with data input: '" + dataStr + "'")
        return False

def regValueTester(dataStr):
    regex = re.search("^\d{6}$", dataStr)
    if regex:
        return True
    else:
        print(" >>> failure with data input: '" + dataStr + "'")
        return False
    
def main():
    testData = input("Testdata:")
    regDateTester(testData)

if __name__ == "__main__":
    main()
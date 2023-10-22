from cProfile import label
import datetime
from enum import IntEnum
import json
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from datetime import datetime
from s_statistik import *
from s_tools import *

def addValuesNow(nDate, nValue, fileName = 'strom.json'):
    jsonList = []
    #check if file is exist
    if os.path.isfile(fileName) is False:
        with open(fileName, 'w') as cf:
            json.dump(jsonList, cf, indent=4)
    #read data from file
    with open(fileName) as outfile:
        jsonList = json.load(outfile)
    #append key value pair
    jsonList.append({"Date" : nDate, "Value" : nValue})
    #save into the file
    with open(fileName, 'w') as json_file:
        json.dump(jsonList, json_file, indent=4, separators=(',',':'))
    
    print("\ndata added successfully!")
    
    if __name__ == "__main__":
        main()

def inputNewData(fileName = 'strom.json'):
    newDate = input("date (e.g. '1990-12-04'):")
    if regDateTester(newDate) is False:
        if __name__ == "__main__":
            main()
        else:
            inputNewData(fileName=fileName)
    newValue = input("value (e.g. '001122'):")
    if regValueTester(newValue) is False:
        if __name__ == "__main__":
            main()
        else:
            inputNewData(fileName=fileName)

    print("\nIs this data pair correct?: date: '" + newDate + "' value: '" + newValue + "'")
    print("Press 'y' to save data or 'n' to cancel")

    dataCorrect = input()
    if dataCorrect == 'y':
        addValuesNow(newDate, newValue, fileName=fileName)
    elif dataCorrect == 'n':
        if __name__ == "__main__":
            main()
    else:
        print(" >>> user input error")
        inputNewData(fileName=fileName)

def showPlot(fileName = 'strom.json'):
    dataList = []
    #check if file is exist
    if os.path.isfile(fileName) is False:
        print("- - - There is NO file to load data for a grid! - - -")
        if __name__ == "__main__":
            main()
    elif os.path.isfile(fileName):
        with open(fileName) as outfile:
            #read data -> put into list
            dataList = json.load(outfile)
            dataListLength = len(dataList)

            xpoints = []
            ypoints = []
            for count, dataListResult in enumerate(dataList):
                dateStr = dataList[count]["Date"]
                valueStr = dataList[count]["Value"]
                dateFormat = '%Y-%m-%d'
                dateObject = datetime.strptime(dateStr, dateFormat)
                #dateObjectStr = str(dateObject)

                xpoints.append(np.datetime64(dateStr))
                ypoints.append(int(valueStr))
            
            ypointres = [0]
            #ypointresNorm = [0]

            kwhProY = 2000
            kwhProD = kwhProY / 365
            kwhRes = [0]

            for count, dataVal in enumerate(dataList):
                if count + 1 < dataListLength:
                    d0 = xpoints[count]
                    d1 = xpoints[count + 1]
                    delta = d1-d0
                    delta /= np.timedelta64(1, "D")
                    #print(delta)
                    res = ypoints[count + 1] - ypoints[count]
                    kwhRes.append(delta * kwhProD)
                    #ypointresNorm.append(res * delta / 31)
                    ypointres.append(res)

            fig = plt.figure('''figsize=(10, 10)''')
            fig.set_figwidth(10)
            fig.set_figheight(4)
            fig = plt.gcf()
            fig.canvas.manager.set_window_title('EAT - Electricity Analysis Tool')

            ax1 = fig.add_subplot(1, 1, 1)
            
            ax1.plot_date(xpoints, ypointres, fmt="g--", marker = "o")
            for x,y in zip(xpoints,ypointres):
                ax1.annotate("{:.2f}".format(y) , (x,y), textcoords='data')

            ax1.plot_date(xpoints, kwhRes, fmt="r--", marker="o")
            for x,y in zip(xpoints,kwhRes):
                ax1.annotate("{:.2f}".format(y) , (x,y), textcoords='data')

            ax1.set_xlabel("meter reading date")
            ax1.set_ylabel("consumption / kWh")
            ax1.set_xticks(xpoints)
            ax1.grid()
            ax1.set_title("Electricity")
            ax1.legend(['current electricity consumption', str(kwhProY) + ' kWh/year'])
            plt.tick_params("x", labelbottom = True)
            
            '''
            ax2 = fig.add_subplot(2, 1, 2, sharex = ax1)
            #print(ypointresNorm)
            ax2.grid()
            ax2.plot_date(xpoints, std_difference(ypointresNorm), fmt="b--", marker = "o")
            ax2.axhline( 0 )
            ax2.set_xticks(xpoints)
            '''
            plt.subplots_adjust(hspace=0)
            plt.setp(plt.gca().xaxis.get_majorticklabels(), 'rotation', 75)
            fig.tight_layout()
            plt.show()
        exit()

def main():
    fileName = 'strom.json'
    print("\n[Electricity Analysis Tool - EAT]")
    print('\nWhat do you want to do?')
    print("Choose:\n")
    print("'add'  - to add new values")
    print("'show' - to show the datagrid")
    print("'exit' - to exit the program")

    userInput = input("\ncommand:")
    if userInput == 'show':
        showPlot(fileName=fileName)
    elif userInput == 'add':
        inputNewData(fileName = fileName)
    elif userInput == 'exit' or userInput == 'end':
        os.system('cls')
        sys.exit()
    else:
        print(" >>> can't find given command -", "'" + userInput + "'")
    main()

if __name__ == "__main__":
    main()

    
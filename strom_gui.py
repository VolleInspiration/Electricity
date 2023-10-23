from tkinter.simpledialog import askstring
import tkinter as tk
from tkinter import *
from strom import *
from s_tools import *

main_window = tk.Tk()

main_window.geometry("400x200")
main_window.title("EAT - Electricity Analysis Tool")
main_window.eval('tk::PlaceWindow . center')

def inputNewDataOnGUI(date, value, self):
   isDataValid = True
   if regDateTester(date) is False:
      isDataValid = False
      tk.messagebox.showwarning(title="Error", message="Date format not valid! Please try again... '" + date + "'")
        
   if regValueTester(value) is False:
      isDataValid = False
      tk.messagebox.showwarning(title="Error", message="Value format not valid! Please try again... '" + value + "'")
   
   if isDataValid:
      addValuesNow(date, value, fileName=fileName)
      self.destroy()
      

def OnClickButtonAddFromData(date, value, self):
   inputNewDataOnGUI(date, value, self)

def OpenAddElectricityPoint():
   addForm = tk.Toplevel()
   addForm.geometry("400x100")
   addForm.title("add meter data")

   Label(addForm, text = "Input here the meter date (e.g. '1990-12-04'):").grid(row=0)
   Label(addForm, text = "Input here the meter value (e.g. '001188'):").grid(row=1)
   e1 = Entry(addForm)
   e2 = Entry(addForm)
   e1.grid(row=0,column=1)
   e2.grid(row=1,column=1)

   AddFormBtn = Button(addForm, text = "addData", command=lambda:OnClickButtonAddFromData(e1.get(),e2.get(),addForm))
   AddFormBtn.place(x = 300, y = 55)

   addForm.focus()
   addForm.grab_set()

def ShowElectricityData():
   showPlot()
   
AddElectricityPoint = Button(main_window, text ="Add electricity meter", command = OpenAddElectricityPoint)
AddElectricityPoint.place(x=50,y=50)

ShowElectricity = Button(main_window, text="Show meter data", command = ShowElectricityData)
ShowElectricity.place(x=50, y=85)

main_window.mainloop()
"""
    Some Clock I Made

    By Hubsik
    04.05.2022
"""

#! Imports
import tkinter as GUI
import datetime as DATETIME
import os as OS
import re as REGULAR_EXPRESSION

#! Variables
Settings = {
        "Foreground": "white",
        "Background": "black",

        "Window_On_Top": True,
        "Resizable": False,

        "No Alarms Message": "No Alarms Set",
    }
Days = ["Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota"]
Months = ["Grudzień", "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Grudzień"]
Allowed_Colors = [ #Source: https://htmlcolorcodes.com/color-names/
    # Red
    "indianred", "lightcoral", "salmon", "darksalmon", "lightsalmon", "crimson", "red", "firebrick", "darkred",
    # Pink
    "pink", "lightpink", "hotpink", "deeppink", "mediumvioletred", "palevioletred",
    # Orange
    "lightsalmon", "coral", "tomato", "orangered", "darkorange", "orange",
    # Yellow
    "gold", "yellow", "lightyellow", "lemonchiffon", "lightgoldenrodyellow", "papayawhip", "moccasin", "peachpuff", "palegoldenrod", "khaki", "darkkhaki",
    # Purple
    "lavender", "thistle", "plum", "violet", "orchid", "fuchsia", "magenta", "mediumorchid", "mediumpurple", "rebeccapurple", "blueviolet", "darkviolet", "darkorchid", "darkmagenta", "purple", "indigo", "slateblue", "darkslateblue", "mediumslateblue",
    # Green
    "greenyellow", "chartreuse", "lawngreen", "lime", "limegreen", "palegreen", "lightgreen", "mediumspringgreen", "springgreen", "mediumseagreen", "seagreen", "forestgreen", "green", "darkgreen", "yellowgreen", "olivedrab", "olive", "darkolivegreen", "mediumaquamarine", "darkseagreen", "lightseagreen", "darkcyan", "teal",
    # Blue
    "aqua", "cyan", "lightcyan", "paleturquoise", "aquamarine", "turquoise", "mediumturquoise", "darkturquoise", "cadetblue", "steelblue", "lightsteelblue", "powderblue", "lightblue", "skyblue", "lightskyblue", "deepskyblue", "dodgerblue", "cornflowerblue", "royalblue", "blue", "mediumblue", "darkblue", "navy", "midnightblue",
    # Brown
    "cornsilk", "blanchedalmond", "bisque", "navajowhite", "wheat", "burlywood", "tan", "rosybrown", "sandybrown", "goldenrod", "darkgoldenrod", "peru", "chocolate", "saddlebrown", "sienna", "brown", "maroon",
    # White
    "white", "snow", "honeydew", "mintcream", "azure", "aliceblue", "ghostwhite", "whitesmoke", "seashell", "beige", "oldlace", "floralwhite", "ivory", "antiquewhite", "linen", "lavenderblush", "mistyrose",
    # Gray
    "gainsboro", "lightgray", "silver", "darkgray", "gray", "dimgray", "lightslategray", "slategray", "darkslategray", "black"]


#! Functions
def Load_Settings():
    """
        Loading Data From Text File (if Exists) And Updating Settings
    """
    #! If File Exists
    if (OS.path.exists("Clock_Config.txt")):
        File = open("Clock_Config.txt", "r")
    
        #! Loading File To Array
        temp = File.read().splitlines()
        # print(temp)
        if (len(temp) <= 3):
            #! Default Settings
            #Settings["Foreground"] = Settings["Default_Foreground"]
            #Settings["Background"] = Settings["Default_Background"]
            return

        #! Validate Loaded Data
        Regex = "^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
        temp2 = REGULAR_EXPRESSION.compile(Regex)

        if (REGULAR_EXPRESSION.search(temp2, temp[0])): #! Foreground
            Settings["Foreground"] = temp[0]
            # print("1-1")
        elif (temp[0].lower() in Allowed_Colors):
            Settings["Foreground"] = temp[0]
            # print("1-2")
        else:
            Settings["Foreground"] = Settings["Default_Foreground"]
            # print("1-3")

        if (REGULAR_EXPRESSION.search(temp2, temp[1])): #! Background
            Settings["Background"] = temp[1]
            # print("2-1")
        elif (temp[1].lower() in Allowed_Colors):
            Settings["Background"] = temp[1]
            # print("2-2")
        else:
            Settings["Background"] = Settings["Default_Background"]
            # print("2-3")

        #! Window On Top
        if (temp[2] == "True"):
            Settings["Window_On_Top"] = True
            # print("3-1")
        else:
            Settings["Window_On_Top"] = False
            # print("3-2")

        #! Resizable Window
        if (temp[3] == "True"):
            Settings["Resizable"] = True
            # print("4-1")
        else:
            Settings["Resizable"] = False
            # print("4-2")

        #! End
        File.close()

def Open_Settings_Menu():
    """
        Processing Opening New Window With Settings
    """
    #! New Window Settings
    Window_Settings = GUI.Toplevel(Window)
    Window_Settings.title("Clock Settings")
    Window_Settings.resizable(Settings["Resizable"], Settings["Resizable"])
    # Window_Settings.geometry("200x250")

    #! Functions
    def Save_Settings():
        """
            Save Settings To Text File
            Requires Restarting APP To Take Effect
        """
        #! Create File
        File = open("Clock_Config.txt", "w")

        #! Save Data To File
        File.write(Entry_FG.get() + "\n")
        File.write(Entry_BG.get() + "\n")

        File.write(str(Checkbox_OnTop_Value.get()) + "\n")
        File.write(str(Checkbox_Resizable_Value.get()) + "\n")

        #! End
        Label.config(text="Settings Will Change On Restarting App")
        File.close()

    #! Defining GUI Elements
    Label = GUI.Label(Window_Settings, text="Settings:")
    Label.grid(row=0, column=0, columnspan=2)

    Label_FG = GUI.Label(Window_Settings, text="Foreground: ")
    Label_BG = GUI.Label(Window_Settings, text="Background: ")
    Label_OnTop = GUI.Label(Window_Settings, text="Window On Top: ")
    Label_Resizable = GUI.Label(Window_Settings, text="Resizable Window: ")

    Entry_FG = GUI.Entry(Window_Settings)
    Entry_BG = GUI.Entry(Window_Settings)

    Label = GUI.Label(Window_Settings, text="Enter Colors As HTML Color Names OR HEX Value")

    Button_Save = GUI.Button(Window_Settings, text="Save", command=Save_Settings)

    Checkbox_OnTop_Value = GUI.BooleanVar()
    Checkbox_Resizable_Value = GUI.BooleanVar()
    Checkbox_OnTop = GUI.Checkbutton(Window_Settings, onvalue=True, offvalue=False, variable=Checkbox_OnTop_Value)
    Checkbox_Resizable = GUI.Checkbutton(Window_Settings, onvalue=True, offvalue=False, variable=Checkbox_Resizable_Value)

    #! Default Values For Entry/Checkbox/Whatever
    Entry_FG.insert(0, Settings["Foreground"])
    Entry_BG.insert(0, Settings["Background"])
    if (Settings["Window_On_Top"]):
        Checkbox_OnTop.select()
    if (Settings["Resizable"]):
        Checkbox_Resizable.select()


    #! Placing GUI Elements
    Label.grid(row=0, column=0, columnspan=2)

    Label_FG.grid(row=1, column=0)
    Entry_FG.grid(row=1, column=1)

    Label_BG.grid(row=2, column=0)
    Entry_BG.grid(row=2, column=1)

    Label_OnTop.grid(row=3, column=0)
    Checkbox_OnTop.grid(row=3, column=1)

    Label_Resizable.grid(row=4, column=0)
    Checkbox_Resizable.grid(row=4, column=1)

    Button_Save.grid(row=5, column=0, columnspan=2)

    Label.grid(row=6, column=0, columnspan=2)

def Update_Clock():
    """"
        Get time/date and edit label
    """
    #! Update Time / Weekday / Month / Year
    Clock = DATETIME.datetime.now()
    Clock_Combined = Clock.strftime("%H:%M:%S   ")  + Days[int(Clock.strftime("%w"))] + "\n" + Clock.strftime("%d ") + Months[int(Clock.strftime("%m"))] + Clock.strftime(" %Y")

    Label_1.config(text=Clock_Combined)

    #! Update Alarms
    # FIXME: Redundant???

    #! End
    Window.after(100, Update_Clock)

def Open_Alarm_Menu():
    #! New Window Settings
    Window_Alarms = GUI.Toplevel(Window)
    Window_Alarms.title("Clock Alarms")
    Window_Alarms.resizable(Settings["Resizable"], Settings["Resizable"])

    #! Functions
    def Display_Alarms():
        if (len(Alarms) == 0): # If There Is No Alarms
            Label_3.config(text="No Set Alarms")
        else: # If There Are Alarms Set
            WIP_TEXT = "Alarms: \n"
            for x in range(len(Alarms)):
                WIP_TEXT += str(Alarms[x]) + "\n"
            
            Label_3.config(text=WIP_TEXT)
        
    def Remove_All_Alarms():
        #! Empty Array With Alarms
        global Alarms
        Alarms = []

        #! End
        Display_Alarms()
        Actual_Alarm()

    def Add_Alarm():
        #! Walidacja TODO: Dokończyć to coś
        Regex = "^[0-9]{2}[:,-, ][0-9]{2}$" # FIXME: dopracować, żeby np 25:62 nie działało
        temp = REGULAR_EXPRESSION.compile(Regex)

        if (REGULAR_EXPRESSION.search(temp, Entry_1.get())):
            #print("T")
            Alarms.append(Entry_1.get())

            Actual_Alarm()

            print(Alarms)
            #sorted(Alarms)
            Alarms.sort()
            print(Alarms)

        #else:
            #print("N")

        #! End
        Display_Alarms()

    def Actual_Alarm():
        #! FIXME: Everything lol

        #! Checking For Alarms
        if (len(Alarms) == 0):
            Label_5.config(text=Settings["No Alarms Message"])
        else:
            #! v2
            Next_Alarm = ""
            Alarm_Hours = 0
            Alarm_Minutes = 0
            Alarm_In_X_Minutes = 0
            Alarms.sort()

            #! Calculating Closest Time FIXME:
            """
                Clock = DATETIME.datetime.now()
                Clock_Combined = Clock.strftime("%H:%M:%S   ")
            """
            print(Alarms)
            WIP_0 = []
            Now_1 = DATETIME.datetime.now()
            Now_2 = Now_1.strftime("%H:%M")

            print("1: " + str(Now_1))
            print("2: " + str(Now_2))

            WIP_1 = DATETIME.datetime.strptime(Now_2, "%H:%M")
            WIP_2 = DATETIME.datetime.strptime(Alarms[0], "%H:%M")

            print("3: " + str(WIP_1))
            print("4: " + str(WIP_2))

            for x in Alarms:
                #print(x)
                WIP_1 = DATETIME.datetime.strptime(Now_2, "%H:%M")
                WIP_2 = DATETIME.datetime.strptime(Alarms[0], "%H:%M")
                WIP_0.append(abs(WIP_1- WIP_2))

            print(f"5: {WIP_0}")
            print(f"6: {min(WIP_0)}")


            #! End
            #Label_5.config(text=f"Next Alarm: {Alarms[0]}\nIn: {Alarm_In_X_Minutes} m")
            Label_5.config(text=f"Next Alarm: {Alarms[0]}\n")

    #! Defining GUI Elements
    Label = GUI.Label(Window_Alarms, text="Alarms:")
    Label_1 = GUI.Label(Window_Alarms, text="Add New Alarm (hh:mm format): ")
    Entry_1 = GUI.Entry(Window_Alarms)
    Button_1 = GUI.Button(Window_Alarms, text="Add Alarm", command=Add_Alarm)
    Button_2 = GUI.Button(Window_Alarms, text="Remove All Alarms", command=Remove_All_Alarms)
    #Label_2 = GUI.Label(Window_Alarms, text="Alarms Dont Persist After Closing App\n(Close App To Remove Alarms)")
    Label_3 = GUI.Label(Window_Alarms, text="")

    #! Default Values For Entry/Checkbox/Whatever

    #! Placing GUI Elements
    Label.grid(row=0, column=0, columnspan=2)
    Label_1.grid(row=1, column=0)
    Entry_1.grid(row=1, column=1)
    Button_1.grid(row=2, column=1)
    Button_2.grid(row=2, column=0)
    #Label_2.grid(row=3, column=0, columnspan=2)
    Label_3.grid(row=3, column=0, columnspan=2)

    #! End
    Display_Alarms()

#! Main
Load_Settings()

Window = GUI.Tk()
Window.title("Clock")
#Window.geometry("200x35")
Window.geometry("200x60")
Window.attributes('-topmost', Settings["Window_On_Top"])
Window.resizable(Settings["Resizable"], Settings["Resizable"])
#Window.iconbitmap("Letter_P.ico") # FIXME: Something wrong with this line ---> idk correct command for it to work in .exe
Window.configure(bg=Settings["Background"])

Alarms = []

Label_1 = GUI.Label(text="", fg=Settings["Foreground"], bg=Settings["Background"])
Label_1.grid(row=0, column=0)

Button_1 = GUI.Button(Window, text="   ...   ", command=Open_Settings_Menu, fg=Settings["Foreground"], bg=Settings["Background"], border=0)
Button_1.grid(row=0, column=1, sticky='nesw')

Button_2 = GUI.Button(Window, text="New\nAlarm", command=Open_Alarm_Menu, fg=Settings["Foreground"], bg=Settings["Background"], border=0)
Button_2.grid(row=0, column=2, sticky='nesw')

Label_2 = GUI.Label(text="", fg=Settings["Foreground"], bg=Settings["Background"])
Label_2.grid(row=1, column=0, columnspan=3)

Label_5 = GUI.Label(Window, text=Settings["No Alarms Message"], fg=Settings["Foreground"], bg=Settings["Background"])
Label_5.grid(row=1, column=0, columnspan=3)

Update_Clock()
Window.mainloop()
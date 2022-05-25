import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg ### NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib import style

from scipy.signal import find_peaks
import serial as sr

import pandas as pd
import numpy as np
import time

import tkinter as tk
from tkinter import ttk


import pygame 

pygame.init()
sound = pygame.mixer.Sound('mixkit-retro-game-notification-212.wav')


#--- Global variables --- 
result_list = []

playsound = True
audio= False
visual = False 
both=False
cond = False

angle=0
angle_procent=0.1

x_data=np.array([])
y_data=np.array([])
data=np.array([])
t=np.array([])
x_lower_limit = 0
x_upper_limit = 500
y_upper_limit = 110
x_c=0
theta_1_list = []
theta_2_list = []

angle_1 = angle_2 = 0.0
alpha = 0.02
ti = 1/104

index = 0

#Grafen
LARGE_FONT= ("Verdana", 10)
style.use("ggplot")

#----Plot ----
f = Figure()#figsize=(5,4)
ax = f.add_subplot(111)
ax.set_title("Sportssensor data")
ax.set_xlabel('Sample')
ax.set_ylabel('Knee Angle')
ax.axhline(y=90)

### Creating static band of green area on the plots
# ax.axhspan(72, 90, facecolor='lightgreen')
# ax.axhspan(0, 18, facecolor='lightgreen')
# ax.axhspan(94.5, 85.5, facecolor='lightgreen')
# ax.axhspan(0, 4.5, facecolor='lightgreen')

ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')  
ax.tick_params(axis='y', colors='white')  
ax.set_xlim(x_lower_limit,x_upper_limit)
ax.set_ylim(-15,y_upper_limit)
lines=ax.plot([],[], linewidth=2)[0] #linewidth=4, marker='o'



def animate(i): #slettet i
    global x_lower_limit, x_upper_limit, y_upper_limit, data, x_data, y_data, angle_1, angle_2, alpha, ti, playsound,t, result_list, index, angle_procent
    if(cond==True):
        s1.flushInput()
        s2.flushInput()
        s1_bytes = s1.readline()
        s2_bytes = s2.readline()
        a1 = [float(d) for d in s1_bytes.decode('ascii').split(",")]
        a2 = [float(d) for d in s2_bytes.decode('ascii').split(",")]
            
        theta_1 = np.arctan2(a1[3], a1[2])
        theta_2 = np.arctan2(a2[3], a2[2])

        angle_1 = 0.8*(angle_1 + a1[7]*ti) + (0.2 * theta_1)
        angle_2 = 0.8*(angle_2 + a2[7]*ti) + (0.2 * theta_2)
        
        final_angle = angle_1 - angle_2
        final_angle *= (180/np.pi) 
        
        data = np.append(data, final_angle)
        result_list.append(final_angle)
        data[0:len(data)-1] = data[1:len(data)]
            
            
        
        if (len(data)+250 >= x_upper_limit):
            x_lower_limit+=1
            x_upper_limit+=1
            ax.set_xlim(x_lower_limit,x_upper_limit)
            lines.set_ydata(data)
            lines.set_xdata(np.arange(0,len(data)))
        else:
            lines.set_ydata(data)
            lines.set_xdata(np.arange(0,len(data)))


        ### THRESHOLDS BELOW
        if audio == True: 
            ax.axhspan((angle - (angle*(angle_procent*0.5))), (angle + (angle*(angle_procent*0.5))), facecolor='lightgreen')
            ax.axhspan(0, angle*(angle_procent*0.5), facecolor='lightgreen')
            
            if((final_angle > angle + (angle*(angle_procent*0.5))) or (final_angle < angle - (angle*(angle_procent*0.5))) and (final_angle > (angle*angle_procent))): 
                f.patch.set_facecolor('red')
                # lines.set_color('red')
                playsound = True
            elif(((final_angle > angle*(angle_procent*0.5)) and (final_angle < angle - (angle*(angle_procent*0.5)))) or final_angle < 0):
                f.patch.set_facecolor('red')
                # lines.set_color('red')
                playsound = True
            else:
                f.patch.set_facecolor('green')
                # lines.set_color('green')
                if playsound: 
                    pygame.mixer.Sound.play(sound)
                    playsound = False
        
        
        if visual == True: 
            if((final_angle > angle) or (final_angle < angle - (angle*angle_procent)) and (final_angle > (angle*angle_procent))): 
                f.patch.set_facecolor('red')
                # lines.set_color('red')
            elif(((final_angle > angle*angle_procent) and (final_angle < angle - (angle*angle_procent))) or final_angle < 0):
                f.patch.set_facecolor('red')
                # lines.set_color('red')
            else:
                f.patch.set_facecolor('green')
                # lines.set_color('green')

def plot_start():
    global cond 
    cond= True #sætter den til true, så plotting starter
    # s1.reset_input_buffer()
    # s2.reset_input_buffer()
def plot_stop():
    global cond,t 
    cond = False
    print(np.amax(t))
def show_results():
    global cond, result_list, peaks
    cond = False
    
    peaks_index, _ = find_peaks(result_list, height=(angle - (angle*angle_procent)), distance=52)
    peaks = list(result_list[i] for i in peaks_index)
    
    
    peak_results = [x - angle for x in peaks]
    average_peak = sum(peak_results) / len(peak_results)

    
    print('Deviation of the peaks: {}'.format(peaks))
    print('The average deviation of the peaks is: {}'.format(average_peak))
    # print('Peak properties: {}'.format(properties))

  

class SportSensor(tk.Tk):

    def __init__(self, *args, **kwargs): #init-method- initialize within the class - starter altid, når man kalder den class
        
        tk.Tk.__init__(self, *args, **kwargs)
       
        
        self.container = tk.Frame(self) #Frame skaber en window - dermed har man en container

        self.container.pack(side="top", fill="both", expand = True)

        self.container.grid_rowconfigure(0, minsize=500, weight=1)
        self.container.grid_columnconfigure(0, minsize=500, weight=1) #ændre på størrelsen https://stackoverflow.com/questions/4399180/how-to-set-the-min-and-max-height-or-width-of-a-frame
        

        self.frames = {}

        for F in (PageOne, PageTwo, ResultPage):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=50,padx=50)

        # change the tk to ttk

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        
        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=50,padx=50)
        
        text=tk.Text(self, height=3, width=20)
        text.pack()
        
        def printInput(): #https://www.geeksforgeeks.org/how-to-get-the-input-from-tkinter-text-box/
            global angle
            inp = text.get(1.0, "end-1c")
            angle=int(inp)
            print(angle)
            lbl.config(text = "Angle is: "+inp)
            # ax.axhline(y=angle)
        
        Button_submit = tk.Button(self, bg="White",text="Submit angle",
                                  command = lambda: printInput())
        Button_submit.pack()
        
        lbl = tk.Label(self, text = "")
        lbl.pack()
        
        #Biofeedback
       
       
        def which_button(button_press):
            # Printing the text when a button is clicked
            global audio, visual, both
            if(button_press=="audio"):
                Button_audio.configure(bg="green")
                Button_visual.configure(bg="White")
                Button_Both.configure(bg="White")
                audio=True 
                visual= False
                both= False
                #print(audio, visual, both)
            elif(button_press=="visual"):
                Button_visual.configure(bg="green")
                Button_audio.configure(bg="White")
                Button_Both.configure(bg="White")
                audio=False
                visual= True
                both= False
                #print(audio, visual, both)
            elif(button_press=="both"):
                Button_Both.configure(bg="green")
                Button_visual.configure(bg="White")
                Button_audio.configure(bg="White")
                audio=False
                visual= False
                both= True
                #print(audio, visual, both)
        
        Button_audio = tk.Button(self, text="Audio feedback", bg="White", 
                                 command=lambda m="audio": which_button(m))
        Button_audio.pack()
        
        Button_visual = tk.Button(self, text="Visual feedback", bg="White",
                                  command=lambda m="visual": which_button(m))
        Button_visual.pack()
        
        Button_Both = tk.Button(self, text="Both audio and visual feedback", 
                                bg="White",
                                command=lambda m="both": which_button(m))
        Button_Both.pack()
        
        
        #Plot data
        label_plot = tk.Label(self, text="Plot data", font=LARGE_FONT)
        label_plot.pack()
        
        Button_plot=tk.Button(self, text="Plot", bg="White", font=LARGE_FONT,
                              command=lambda: controller.show_frame(PageTwo))
        Button_plot.pack()
        #Back to start 

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        
        
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack()
        
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        #self.after(1, plot_data)
        # change the tk to ttk
        
        start=tk.Button(self, text ="Start", font=('calbiri',12), command = lambda: plot_start())
        start.pack()
        
        stop=tk.Button(self, text ="Stop", font=('calbiri',12), command = lambda: plot_stop())
        #stop.place(x=start.winfo_x()+start.winfo_reqwidth()+20, y=start.winfo_y())
        stop.pack()
        
        button = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        #button.place(x=500, y=500)
        button.pack()
        
        button_results = tk.Button(self, text="results", bg="White", font=LARGE_FONT,
                              command=lambda: [save_txt(), controller.show_frame(ResultPage)])

        button_results.pack()
        
        #Save on file 
        def save_txt():
            global cond, result_list
            cond=False
            text_file=open('sampleText.txt', 'w')
            for elem in result_list:
                val = str(elem) + ","
                text_file.write(val)
            text_file.close()
        
        
class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        # global peak_results, average_peak
        tk.Frame.__init__(self,parent)
        
        def convert(float_str): 
            def is_float(s): 
                try: 
                  float(s)
                  return True
                except: 
                  return False
            new_float=[]  
            for x in float_str:
                if is_float(x)==1:
                  f=float(x)
                  new_float.append(f)
                  
                
            return new_float
        
        def open_txt():
            text_file=open('sampleText.txt', 'r')
            a = text_file.read().split(',')
           
            a = convert(a)
            # peaks_index, _ = find_peaks(result_list, height=(angle - (angle*angle_procent)), distance=52)
            peaks_index, _ = find_peaks(a, height=angle - (angle*angle_procent), distance=52)
            peaks = list(a[i] for i in peaks_index)
            freq_of_peaks = np.diff(peaks_index)
            peak_results = [abs(np.round(x - angle, 3)) for x in peaks]
            average_peak = sum(peak_results) / len(peak_results)
            final_result = 'User inputted angle {} deg \n Peak differences: \t'.format(angle) + ' deg '.join(str(e) for e in peak_results) + ' deg \n Avg Peak difference: {} deg'.format(str(np.round(average_peak, 3))) + ' \n Frequency of the peaks: {}'.format(freq_of_peaks)
            lbl.config(text = final_result)
            text_file.close()
        
        button = tk.Button(self, text="Show peaks",
                            command=lambda: open_txt())
        button.pack(pady=20)
        lbl = tk.Label(self, text = "")
        lbl.pack()
       # label = ttk.Label(self, text="Results", font=LARGE_FONT)
       # label.pack()
        


        
        
        #self.after(1, plot_data)
        # change the tk to ttk
        
        # start=tk.Button(self, text ="ben", font=('calbiri',12), command = lambda: plot_start())
        # start.pack()
        
        # stop=tk.Button(self, text ="benis", font=('calbiri',12), command = lambda: plot_stop())
        # #stop.place(x=start.winfo_x()+start.winfo_reqwidth()+20, y=start.winfo_y())
        # stop.pack()
        
        button = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageTwo))
        #button.place(x=500, y=500)
        button.pack()
        
        
        
     
s1 = sr.Serial('COM7', 115200)
s2 = sr.Serial('COM12', 115200)
app = SportSensor()
ani = FuncAnimation(f, animate, interval=9.5)
app.mainloop()






### LINKS
# https://stackoverflow.com/questions/50731915/switching-frames-in-tkinter
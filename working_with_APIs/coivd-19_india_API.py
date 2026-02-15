from tkinter import *
from tkinter import messagebox
import requests
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


w = Tk()
w.title("COVID-19 Tracker")
w.resizable(True, True)
w.attributes("-fullscreen", True)

Label(w, text="COVID-19 Data India", font=("Arial", 20)).grid(row=0, column=3, columnspan=2, pady=20)

Label(w, text="State Name:", font=("Roboto", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")

state_entry = Entry(w, width=15, font=("Arial", 14))
state_entry.grid(row=1, column=1, padx=10, pady=10)

Label(w, text="Confirmed:", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=10, pady=10)

confirmed = Label(w, text="")
confirmed.grid(row=3, column=1, sticky="w")

Label(w, text="Active:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=10, pady=10)

active = Label(w, text="")
active.grid(row=4, column=1, sticky="w")

Label(w, text="Recovered:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=10, pady=10)

recovered = Label(w, text="")
recovered.grid(row=5, column=1, sticky="w")

Label(w, text="Deaths:", font=("Arial", 12, "bold")).grid(row=6, column=0, sticky="w", padx=10, pady=10)

deaths = Label(w, text="")
deaths.grid(row=6, column=1, sticky="w")

Label(w, text="Total cases:", font=("Arial", 12, "bold")).grid(row=1, column=2, sticky="w", padx=10, pady=10)

Label(w, text="Average cases per state:", font=("Arial", 12, "bold")).grid(row=2, column=2, sticky="w", padx=10, pady=10)

Label(w, text="Number of states:", font=("Arial", 12, "bold")).grid(row=3, column=2, sticky="w", padx=10, pady=10)

Label(w, text="Maximum cases registered:", font=("Arial", 12, "bold")).grid(row=4, column=2, sticky="w", padx=10, pady=10)

Label(w, text="Minimum cases registered:", font=("Arial", 12, "bold")).grid(row=5, column=2, sticky="w", padx=10, pady=10)

Label(w, text="total deaths:", font=("Arial", 12, "bold")).grid(row=1, column=4, sticky="w", padx=10, pady=10)

Label(w, text="Average deaths per state:", font=("Arial", 12, "bold")).grid(row=2, column=4, sticky="w", padx=10, pady=10)

Label(w, text="Maximum deaths registered:", font=("Arial", 12, "bold")).grid(row=3, 
column=4, sticky="w", padx=10, pady=10)

Label(w, text="Minimum deaths registered:", font=("Arial", 12, "bold")).grid(row=4, column=4, sticky="w", padx=10, pady=10)

Label(w, text="Recovery %:", font=("Arial", 12, "bold")).grid(row=1, column=6, sticky="w", padx=10, pady=10)

Label(w, text="Death %:", font=("Arial", 12, "bold")).grid(row=2, column=6, sticky="w", padx=10, pady=10)

Label(w, text="Max Recovery%:", font=("Arial", 12, "bold")).grid(row=3, column=6, 
sticky="w", padx=10, pady=10)

Label(w, text="Max Death%:", font=("Arial", 12, "bold")).grid(row=4, column=6, sticky="w", padx=10, pady=10)

graph_frame = Frame(w, bd=2, relief="ridge")
graph_frame.grid(row=6, column=2, columnspan=6, rowspan=6, padx=10, pady=10, sticky="nsew")

total_cases_lbl = Label(w, text="")
total_cases_lbl.grid(row=1, column=3, sticky="w")

avg_cases_lbl = Label(w, text="")
avg_cases_lbl.grid(row=2, column=3, sticky="w")

state_count_lbl = Label(w, text="")
state_count_lbl.grid(row=3, column=3, sticky="w")

max_cases_lbl = Label(w, text="")
max_cases_lbl.grid(row=4, column=3, sticky="w")

min_cases_lbl = Label(w, text="")
min_cases_lbl.grid(row=5, column=3, sticky="w")

total_deaths_lbl = Label(w, text="")
total_deaths_lbl.grid(row=1, column=5, sticky="w")

avg_deaths_lbl = Label(w, text="")
avg_deaths_lbl.grid(row=2, column=5, sticky="w")

max_deaths_lbl = Label(w, text="")
max_deaths_lbl.grid(row=3, column=5, sticky="w")

min_deaths_lbl = Label(w, text="")
min_deaths_lbl.grid(row=4, column=5, sticky="w")

def clear_data():
    state_entry.delete(0, END)
    for lbl in [confirmed, active, recovered, deaths]:
        lbl.config(text="")

def analytics():
    try:
        with open("covid_data.csv","r") as f1:
            fileReader=csv.reader(f1)
            next(fileReader)
            all_cases = list(fileReader)

            for i in range(len(all_cases)):
                for j in range(i+1,len(all_cases)):
                    x = float(all_cases[i][1])
                    y = float(all_cases[j][1])
                    if x < y:
                        temp = all_cases[i]
                        all_cases[i] = all_cases[j]
                        all_cases[j] = temp

            states=[]
            confirmed_cases=[]
            for i in range(10):
                states.append(all_cases[i][0])
                confirmed_cases.append(all_cases[i][1])

            for i in range(len(all_cases)):
                for j in range(i+1,len(all_cases)):
                    x=float(all_cases[i][4])
                    y=float(all_cases[j][4])
                    if x<y:
                        temp = all_cases[i]
                        all_cases[i]=all_cases[j]
                        all_cases[j]=temp

            states=[]
            death_cases=[]
            for i in range(10):
                states.append(all_cases[i][0])
                death_cases.append(all_cases[i][4])

            states=[]
            recovery_cases=[]
            for i in range(10):
                states.append(all_cases[i][0])
                recovery_cases.append(all_cases[i][3])

            states=[]
            death_percentage_cases=[]
            for i in range(5):
                states.append(all_cases[i][0])
                death_percentage_cases.append(all_cases[i][6])
            
            states=[]
            recovery_percentage_cases=[]
            for i in range(5):
                states.append(all_cases[i][0])
                recovery_percentage_cases.append(all_cases[i][5])

        if len(all_cases)<=1:
            messagebox.showerror("Error", "No data available")
            return

        i=1
        while i<len(all_cases) and not all_cases[i][1].isdigit():
            i += 1

        if i==len(all_cases):
            messagebox.showerror("Error", "No valid numeric data")
            return

        max_cases=int(all_cases[i][1])
        min_cases=int(all_cases[i][1])
        max_case_state=all_cases[i][0]
        min_case_state=all_cases[i][0]

        max_deaths=int(all_cases[i][4])
        min_deaths=int(all_cases[i][4])
        max_death_state=all_cases[i][0]
        min_death_state=all_cases[i][0]

        total_cases=0
        total_deaths=0
        count=0

        max_recovery_pct=-1
        max_recovery_state=""
        max_death_pct=-1
        max_death_state=""

        for a in all_cases[i:]:
            if a[1].isdigit() and a[4].isdigit() and a[3].isdigit():
                cases = int(a[1])
                recovered_val = int(a[3])
                deaths_val = int(a[4])

                total_cases += cases
                total_deaths += deaths_val
                count += 1

                if cases > max_cases:
                    max_cases = cases
                    max_case_state = a[0]

                if cases < min_cases:
                    min_cases = cases
                    min_case_state = a[0]

                if deaths_val > max_deaths:
                    max_deaths = deaths_val
                    max_death_state = a[0]

                if deaths_val < min_deaths:
                    min_deaths = deaths_val
                    min_death_state = a[0]

                recovery_pct = (recovered_val / cases) * 100
                death_pct = (deaths_val / cases) * 100

                if recovery_pct > max_recovery_pct:
                    max_recovery_pct = recovery_pct
                    max_recovery_state = a[0]

                if death_pct > max_death_pct:
                    max_death_pct = death_pct
                    max_death_state = a[0]

        total_cases_lbl.config(text=total_cases)
        avg_cases_lbl.config(text=round(total_cases / count, 2))
        state_count_lbl.config(text=count)

        max_cases_lbl.config(text=f"{max_cases} ({max_case_state})")
        min_cases_lbl.config(text=f"{min_cases} ({min_case_state})")

        total_deaths_lbl.config(text=total_deaths)
        avg_deaths_lbl.config(text=round(total_deaths / count, 2))

        max_deaths_lbl.config(text=f"{max_deaths} ({max_death_state})")
        min_deaths_lbl.config(text=f"{min_deaths} ({min_death_state})")

        recovery_percentage = round((total_cases - total_deaths) / total_cases * 100, 2)
        death_percentage = round((total_deaths / total_cases) * 100, 2)

        recovery_pct_lbl = Label(w, text=recovery_percentage)
        recovery_pct_lbl.grid(row=1, column=7, sticky="w")

        death_pct_lbl = Label(w, text=death_percentage)
        death_pct_lbl.grid(row=2, column=7, sticky="w")

        max_recovery_pct_lbl = Label(w, text=f"{max_recovery_state} ({round(max_recovery_pct,2)}%)")
        max_recovery_pct_lbl.grid(row=3, column=7, sticky="w")

        max_death_pct_lbl = Label(w, text=f"{max_death_state} ({round(max_death_pct,2)}%)")
        max_death_pct_lbl.grid(row=4, column=7, sticky="w")

        for widget in graph_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(6, 4), dpi=100)

        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)

        ax1.bar(states[:5], list(map(float, confirmed_cases[:5])))
        ax1.set_title("Top 5 Confirmed", fontsize=10)
        ax1.tick_params(axis='x', rotation=45, labelsize=8)

        ax2.bar(states[:5], list(map(float, death_cases[:5])))
        ax2.set_title("Top 5 Deaths", fontsize=10)
        ax2.tick_params(axis='x', rotation=45, labelsize=8)

        ax3.bar(states[:5], list(map(float, recovery_percentage_cases[:5])))
        ax3.set_title("Top 5 Recovery %", fontsize=10)
        ax3.tick_params(axis='x', rotation=45, labelsize=8)

        ax4.bar(states[:5], list(map(float, death_percentage_cases[:5])))
        ax4.set_title("Top 5 Death %", fontsize=10)
        ax4.tick_params(axis='x', rotation=45, labelsize=8)

        fig.tight_layout(pad=1.2)

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    except FileNotFoundError:
        messagebox.showerror("Error", "CSV file not found. Save data first.")

    btn_get.config(state=DISABLED)
    btn_clear.config(state=DISABLED)
    btn_save.config(state=DISABLED)

def get_covid_data():
    state_name = state_entry.get().strip().title()
    if state_name == "":
        messagebox.showerror("Error", "Please enter state name")
        return

    try:
        url = "https://data.covid19india.org/data.json"
        data = requests.get(url).json()
        state_list = data["statewise"]

        found = False
        for state in state_list:
            if state["state"] == state_name:
                confirmed.config(text=state["confirmed"])
                active.config(text=state["active"])
                recovered.config(text=state["recovered"])
                deaths.config(text=state["deaths"])
                found = True
                break

        if not found:
            messagebox.showerror("Error", "State not found")
            clear_data()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data\n{e}")
        clear_data()

def save_to_csv():
    if state_entry.get() == "" or confirmed.cget("text") == "":
        messagebox.showerror("Error", "No data to save")
        return

    file_exists = os.path.isfile("covid_data.csv")
    with open("covid_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["State", "Confirmed", "Active", "Recovered", "Deaths","Recovery %","Death %"])
        writer.writerow([
            state_entry.get().title(),
            confirmed.cget("text"),
            active.cget("text"),
            recovered.cget("text"),
            deaths.cget("text"),
            round((float(recovered.cget("text")) / float(confirmed.cget("text"))) * 100, 2),
            round((float(deaths.cget("text")) / float(confirmed.cget("text"))) * 100, 2)
        ])
    messagebox.showinfo("Saved","Data saved to covid data.csv")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        w.destroy()

btn_get=Button(w,text="Get COVID Data",command=get_covid_data,font=("Arial",12,"bold"))
btn_get.grid(row=2,column=0,columnspan=2,pady=10)

btn_clear=Button(w,text="Clear Data",command=clear_data,font=("Arial",12,"bold"))
btn_clear.grid(row=7,column=0,columnspan=2,pady=15)

btn_save=Button(w,text="Save to CSV",command=save_to_csv,font=("Arial",12,"bold"))
btn_save.grid(row=9,column=0,columnspan=2,pady=15)

btn_analysis=Button(w,text="Display Analysis",command=analytics,font=("Arial",12,"bold"))
btn_analysis.grid(row=8,column=0,columnspan=2,pady=10)

Button(w,text="Exit",command=exit_app,font=("Arial",12,"bold")).grid(row=11,column=0,columnspan=2,pady=15)
Button(w,text="Save to PDF",font=("Arial",12,"bold")).grid(row=10,column=0,columnspan=2,pady=15)

for i in range(8):
    w.grid_columnconfigure(i, weight=2)
w.grid_rowconfigure(5, weight=2)

w.mainloop()
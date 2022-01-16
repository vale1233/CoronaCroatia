from tkinter import *
import backend

def center_tkinter(self):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    root.geometry("+{}+{}".format(positionRight, positionDown))

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        casesButton = Button(self, text='Active cases by region', command=self.corona_cases)
        deathButton = Button(self, text='Number of deaths by region', command=self.corona_deaths)
        totalButton = Button(self, text='Active cases number', command=self.total_cases)
        umrliButton = Button(self, text='Number of deaths', command=self.last_info)
        omjerButton = Button(self, text='Deaths/Active cases rating', command=self.omjeri_rating)
        graphButton = Button(self, text='Croatia deaths graph per 100.000 people', command=self.grafikon_umrli)

        # place button at (0,0)
        exitButton.place(x=350, y=10)
        casesButton.place(x=10, y=115)
        deathButton.place(x=10, y=80)
        totalButton.place(x=10, y=10)
        umrliButton.place(x=10, y=45)
        omjerButton.place(x=10, y=150)
        graphButton.place(x=10, y=185)


    def clickExitButton(self):
        exit()

    def corona_cases(self):
        backend.cases_per_regions(self)

    def corona_deaths(self):
        backend.deaths_per_regions(self)

    def total_cases(self):
        ukupanBroj = backend.sum_cases(self)
        text = Label(self, text=f'Active cases in Croatia = {ukupanBroj}')
        text.place(x=150, y=12)

    def last_info(self):
        umrliHr = backend.last_info(self)
        text = Label(self, text=f'Total deaths in Croatia = {umrliHr}')
        text.place(x=150, y=47)

    def omjeri_rating(self):
        backend.urmli_zarazeni(self)

    def grafikon_umrli(self):
        backend.deaths_per_population(self)

texttwo = backend.updated_date(self='info')
root = Tk()
app = Window(root)
root.wm_title(f"Covid-19: Croatia (last update: {texttwo[0:10]})")
center_tkinter(root)
root.geometry("400x270")
root.mainloop()
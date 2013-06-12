from Tkinter import Tk,  Entry, Text, Label

app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text = "Depot:").pack()
depot = Entry(app)
Label(app, text = "Address:").pack()
depot.pack()
description = Text(app)
description.pack()

app.mainloop()
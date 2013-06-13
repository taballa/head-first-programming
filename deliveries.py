from Tkinter import Tk,  Entry, Text, Label, Button, Radiobutton, StringVar

def save_data():
    file_deliveries = open("deliveries.txt", "a")
    file_deliveries.write( "Despot: \n")
    file_deliveries.write("%s\n" % depot.get())
    file_deliveries.write( "Description \n")
    file_deliveries.write( "%s \n" % description.get())
    file_deliveries.write( "Address: \n")
    file_deliveries.write( "%s \n" % address.get("1.0", 'end'))
    # clear up before data
    depot.set(None)
    description.delete(0, 'end')
    address.delete('1.0', 'end')

app = Tk()
app.title('Head-Ex Deliveries')

depot = StringVar()
depot.set(None)

Label(app, text = "Depot:").pack()
Radiobutton(app, text = 'Cambridge, MA', value = "Cambridge, MA", variable = depot).pack()
Radiobutton(app, text = 'Cambridge, UK', value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text = "Seattle, WA", value = "Seattle, WA", variable = depot).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", width = 10, command = save_data).pack()

app.mainloop()
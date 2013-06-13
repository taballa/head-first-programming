from Tkinter import Tk,  Entry, Text, Label, Button, Radiobutton, StringVar, OptionMenu
import Tkinter.messagebox

def save_data():
    try:
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
    except Exception, e:
        app.title("Can't write to the file %s" % e)

def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

app = Tk()
app.title('Head-Ex Deliveries')

depot = StringVar()
depot.set(None)

Label(app, text = "Depot:").pack()
Radiobutton(app, text = 'Cambridge, MA', value = "Cambridge, MA", variable = depot).pack()
Radiobutton(app, text = 'Cambridge, UK', value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text = "Seattle, WA", value = "Seattle, WA", variable = depot).pack()

# options = ["Cambridge", "MA Cambridge", "UK Seattle", "WA New York", "NY Dallas", "TX Boston", "MA Rome", "Italy Male", "Maldives Luxor", "Egypt Rhodes", "Greece Edinburgh", "Scotland"]
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", width = 10, command = save_data).pack()

app.mainloop()
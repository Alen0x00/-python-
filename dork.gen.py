import random
import subprocess
from tkinter import *
from tkinter import filedialog as fd


icon = '''
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
'''
icons = '''
R0lGODlhEAAQALMJAABdAA6fBhmqETW1GlLFKQBHAP//AABIAEy1Kf///wAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAkALAAAAAAQABAAAARHMMlJq70SAFyB2VxmECDnEUJ5nUKgdmM7gBrFBkOREZ+I4roEICDgaWLACWBA5CFzlQKz+INapERZ8HJABJKhw8AaShS2lggAOw==
'''
mix = '''
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAhdEVYdENyZWF0aW9uIFRpbWUAMjAxODoxMToxOCAxNjo1MToxNBYGYWAAAANvSURBVDhPjZJNbBtFGIbfnR2v98eOnfVvfprEQNKEuDGRCEkLBFSoVNTgokoVKIUILhVcqLiEggQI9QLqkUMj4AKInxuiogokagtqlULaJpSqdUMdkpQmwcTe2PE69nq9u0xoL1wQ72hGc/i+d0bP93LRw6f7//zwiZ9xVw1vzNwXCknJlkbvy4roamoKinbFtHnNRupmyT5BCPf5xSG1fLccnG/4lEMd63juy+Ro45Gp1xvbAu+1dQXQ3qLALxAIlCAqEtTzQM2w8cn8ppYuWAdmk+qP/xh4XrtgUH+9QFPzlUjfvWI4HoEicADhoEoUqkxBWbPEc+ioc2GnDxi7vokzt41dM/vVC5x7ZLIoPtLtqavVEAi4oUgEnVEJO/w8FjMVLKwZCERltDcpcNiqY8Z7gwRHpzeqq7pdz/O9I2+67gkJisyDI8COBgn12QLef3fiq0snpw8v/LJy7MbFP8gtwx1PbPcLFsehAg59XspPrBqLxLJtlMoOMkUTuukgna+h5JfRNXh/q9zbkymdeX5p45sDRwzLfnjics7wywSaA4R8PLrr+WMchsf1yP4HlYGgCz1NbkQcB17LxFS64IzPalMSpXvn3orrW8Daj887HdujsB0RIgO8mGYQW1897Qw9+xC8moHr17Qbv+WMsZvr+auM45XyR4/mthr/Swz3/9BnwQD0bAIdUk+fp/PFmNqWeK71SXyqnQfHvRP/GvG/onzYNeASJCAT/aL8zPlDW33+2T2efCr93e5tsV0vdR7kimIZjR4fe1WEws7R5bESAc31O7HigBPQ4TSboCF5WBofSmwZ5HsndV4QRy6vrfx0tjqNq2IWk8Yczhm/YglZ1KrE4bGvpQC3kXTCgFVjiQlVQTT+BWdQjZCDzSlRlBvKptXZJYTjajSIhXKWjZExpRauZZaqHD5+QIamrePpDQGiG+AFuCjbeS9okY1TbcZjkRhmyCpWKxoINbBZySKmhpG6sqLfgXgisRPS+hQeNwCR/cIg4HkXi7AAznbBAkUduwu0huJcEfr3a5XwPq9o80qVVTOdytzG7m0/4JaQhI9I8Nhw3BVYJsscMUBtCxYLmH7JgPk7d9QeXX6qEnMr1aw5+O8xftAtwS0egsd8BZuFLtCqhSIhPMgy1ugYKDlpvT3P4nNH8rd9/X8DGwdOt57oFosAAAAASUVORK5CYII=
'''
broom = '''
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAArBJREFUeNqkk19I01EUx793zj9tOrc2nK7pXPNP5nDT5UTFylk0XVJEIUT0UEI+1EP0EIhUhA+9FAglFdVDQQWaEW2oGWhRGulkEToqTVamiC6nLt3/2/3lfAop8AcfzuH8u+d37rmEUoqNfPzWeh64ElwdDkJWHZw8fZdiv4HAUrTqizB8Too4PszhCJoDQTTx/uOQUpZ3h4PpO1kh87IPzWXVhwy/VtDM/0dyltVOC1puXTnJtWC90ShlSelG0y5D2/0Oeyi8fgdiFn+Gyb1jY+M3O98lwj8zg5r6iweTtGTqyeNX9slZNEUi6OI6iGUkM2SMNJZYnCAUF2fqyvQjdQVqm82KqiozOrv9qFR9wb5j52oDoas2luzj5sJng7mQIJQUxwtFAkGSVCRLz5ZL5EpZcCnAX5p0o9ooQIf1KUwmC2zdy6hSj8N04ISlu/3eAivQx2OVerwL8/5cY01Fmsag83lo6sSAk++dnYdAKcHP0e+oLVqE1dqGigoLno+kYdG1iFAIPAZizDri6rdTT3/vYF4ihUKYLERKthIxcbGYdnyFRJOKkNePPPEyHr50ICenBHVnLz8q17CboZhYu4WuQi1ZmXMPn88t1VaPDTvBpzxkFGTBO+cB9YUhVslxPN8DY0NdO4tvZb//hluZGMI2ZsELaBTE5Ril7sG3H/JKynWKLdszMeV0IeQPQqSUYf7TFNqePXhtSMe1oW+kL2Mz8PEHW7i1e1OnEKiEFOVaUsnm0pidU7onwhSNPhdzLLmrt2eAbd8l9wpeWEcI1n0CKinBbjXMR/Ix1Hn9ML19agc9qsd701aY5Ul/x3MdcMskZIgYXMgmzqZXoHCbFA3c/n92o8UxjV5mDzD8jGBUD5NokThGfBR+1Mb1GIkSZoSico0/PrLR5/xbgAEAmn8aHZdeMI4AAAAASUVORK5CYII=
'''
help = '''
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAghJREFUeNqUk02rEmEUx8+MjZp6Jw03InlXiVYELpyQAne6yY2ug8BaRItc9B3atM0Whdt2lz5AS0VUMKgs8aogIbrRhYr5Mvr0P8MYF5l7oQM/npfzMuec54xE1hIDz8Ed8/wTfABfjw0lC+dHLpfrbTwevx0IBFS+GI1Gs0ajcb5cLl/jWL5obLMI8OYhxO/3e7GX9/u9fB3i8/nUwWBwA3dnF43lI+c4iHi93pPNZkPMdrs1QIAT1pk2l8p3TdMW6XRaTKfTf5TLZZFKpQTr2OaqEh4Eg8G7brdbabfbBEfa7XYUi8Wo1WrRcDjUwRfYfb6shKf1er0qSZLe7/ep1+vRbDaj8XhMk8lEZx3bXNUDlmKn05nwJhKJUDKZpFKpRLVaje+Kx8ZWAc663e5CURTK5/PEpSBtzmZx/AIs1yzOLw+9KRQKhHIIr3jo1yvwDuhWL6CBT+A8l8uJTCYjMECiUqkY+2w2K1hn2mjHr/AE01cMhUL3E4lEQNd1kmWZotEoN4+azaYxE+Fw+CYGK7Rerx9jNqbw+3YY5R9wjMJJttvtRsq8zudzQ+nxeIwAq9XKGCo87b5arf6C6h7X7AKnTqeT/cnhcBgBeFVVlYQQxBnZbDajH2yDO27+KftK5p/3AjwDf8DCZAk2ZoYO80Me4Abc1Y/gPQdQwC1z/R/Zgt9/BRgANHrYMn3ClUIAAAAASUVORK5CYII=
'''

root = Tk()
__version__ = 'Version: 1.0'
root.resizable(False, False)
root.title("** GenDorks by explorer **    " + __version__)
root.geometry("664x350")


def insert_url():
    file_name = fd.askopenfilename()
    try:
        f = open(file_name)
        s = f.read()
        url_name.insert(1.0, s)
        count_url.delete('0', END)
        y = url_name.get(1.0, END)
        line = (len(y.split()))
        count_url.insert(END, line)
        f.close()
    except FileNotFoundError:
        pass


def normal():
    name.delete(1.0, END)
    type.delete(1.0, END)
    para.delete(1.0, END)
    pattern = r"\b\w+="
    pattern2 = r"\.\w+\?"
    pattern3 = r"\/\w+\."

    x = url_name.get(1.0, END)
    host = x[0:-2].replace('\n', ',').split(',')

    one = []
    two = []
    trio = []
    for item in host:
        string = item.replace('://', '')
        result3 = re.findall(pattern3, string)
        result2 = re.findall(pattern2, string)
        result = re.findall(pattern, string)
        one += result3
        two += result2
        trio += result
    a = set(one)
    b = set(two)
    c = set(trio)
    for n in a:
        name.insert(END, n[1:-1] + '\n')
    for p in b:
        type.insert(END, p + '\n')
    for r in c:
        para.insert(END, r + '\n')

    count_name.delete('0', END)
    count_type.delete('0', END)
    count_para.delete('0', END)
    count_url.delete('0', END)

    s = name.get(1.0, END)
    line = len(s.split())
    count_name.insert(END, line)

    s = type.get(1.0, END)
    line = len(s.split())
    count_type.insert(END, line)

    s = para.get(1.0, END)
    line = len(s.split())
    count_para.insert(END, line)

    y = url_name.get(1.0, END)
    line = (len(y.split()))
    count_url.insert(END, line)


def gen():
    count_name.delete('0', END)
    count_type.delete('0', END)
    count_para.delete('0', END)
    count_dork.delete('0', END)
    dorks_name.delete(1.0, END)

    s = name.get(1.0, END)
    line = len(s.split())
    count_name.insert(END, line)

    s = type.get(1.0, END)
    line = len(s.split())
    count_type.insert(END, line)

    s = para.get(1.0, END)
    line = len(s.split())
    count_para.insert(END, line)

    one = name.get(1.0, END)
    a = one[0:-2].replace('\n', ',').split(',')
    two = type.get(1.0, END)
    b = two[0:-2].replace('\n', ',').split(',')
    trio = para.get(1.0, END)
    c = trio[0:-2].replace('\n', ',').split(',')

    for x in a:
        for y in b:
            for z in c:
                dork = (x + y + z)
                dorks_name.insert(END, dork + '\n')
    count_dork.delete('0', END)
    s = dorks_name.get(1.0, END)
    line = len(s.split())
    count_dork.insert(END, line)


def helpmy():
    subprocess.call(['notepad.exe', 'help.txt'])


def clean():
    count_url.delete('0', END)
    count_name.delete('0', END)
    count_type.delete('0', END)
    count_para.delete('0', END)
    count_dork.delete('0', END)
    url_name.delete(1.0, END)
    dorks_name.delete(1.0, END)
    name.delete(1.0, END)
    type.delete(1.0, END)
    para.delete(1.0, END)


def ran():
    s = dorks_name.get(1.0, END)
    mix = s[0:-2].replace('\n', ',').split(',')
    random.shuffle(mix)
    dorks_name.delete(1.0, END)
    for z in mix:
        a = z + '\n'
        dorks_name.insert(END, a)


def save():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                    ("HTML files", "*.html;*.htm"),
                                    ("All files", "*.*")), defaultextension='')
    try:
        f = open(file_name, 'w')
        s = dorks_name.get(1.0, END)
        f.write(s)
        f.close()
    except FileNotFoundError:
        pass


savebtn = PhotoImage(data=icons)
mixbtn = PhotoImage(data=mix)
broombtn = PhotoImage(data=broom)
helpbtn = PhotoImage(data=help)
img = PhotoImage(data=icon)

name_label = Label(text="Name :")
name_label.grid(row=5, column=1, pady=5, sticky="sw")

type_label = Label(text="Type :")
type_label.grid(row=5, column=3, pady=5, sticky="sw")

para_label = Label(text="Parameter :")
para_label.grid(row=5, column=5, pady=5, sticky="sw")

dork_label = Label(text="Dorks :")
dork_label.grid(row=5, column=7, pady=5, sticky="sw")

open_button = Button(text="Open URLs", width=10, command=insert_url)
open_button.grid(row=1, column=0, padx=10, pady=5, sticky="n")

norm_button = Button(text="Normal", width=10, command=normal)
norm_button.grid(row=2, column=0, padx=10, pady=5, sticky="n")

gens_button = Button(text="Generate", width=10, command=gen)
gens_button.grid(row=3, column=0, padx=10, pady=5, sticky="n")

gens_button = Button(text="  Clean    ", width=10, image=broombtn, compound="left", command=clean)
gens_button.grid(row=6, column=0, padx=10, pady=12, sticky="swe")

help_button = Button(text="   Help     ", width=10, image=helpbtn, compound="left", command=helpmy)
help_button.grid(row=6, column=0, padx=10, pady=47, sticky="swe")

open_button = Button(text="  Random  ", width=10, image=mixbtn, compound="left", command=ran)
open_button.grid(row=6, column=7, pady=47, padx=32, sticky="swe")

save_button = Button(text="    Save       ", width=10, image=savebtn, compound="left", command=save)
save_button.grid(row=6, column=7, pady=12, padx=32, sticky="swe")

count_url = Entry(width=12, justify=CENTER)
count_url.grid(row=0, column=0, padx=10, pady=5, sticky="n")

count_name = Entry(width=4, justify=CENTER)
count_name.grid(row=5, column=1, pady=5, sticky="se")

count_type = Entry(width=4, justify=CENTER)
count_type.grid(row=5, column=3, pady=5, sticky="se")

count_para = Entry(width=4, justify=CENTER)
count_para.grid(row=5, column=5, pady=5, sticky="se")

count_dork = Entry(width=8, justify=CENTER)
count_dork.grid(row=5, column=7, pady=5, sticky="s")

url_name = Text(root, wrap=NONE, font="Courier 9", width=52, height=1)
url_name.grid(row=0, column=1, columnspan=5, rowspan=4, sticky='nswe')
scrollb = Scrollbar(root, orient=VERTICAL, command=url_name.yview)
scrollb.grid(row=0, column=6, rowspan=4, sticky='nse')
url_name.configure(yscrollcommand=scrollb.set)
sc = Scrollbar(root, orient=HORIZONTAL, command=url_name.xview)
sc.grid(row=4, columnspan=5, column=1, sticky='sew')
url_name.configure(xscrollcommand=sc.set)

dorks_name = Text(root, wrap=NONE, font="Courier 9", width=22, height=1)
dorks_name.grid(row=0, column=7, rowspan=4, sticky='nswe')
scroll = Scrollbar(root, orient=VERTICAL, command=dorks_name.yview)
scroll.grid(row=0, column=8, rowspan=4, sticky='nse')
dorks_name.configure(yscrollcommand=scroll.set)
scroli = Scrollbar(root, orient=HORIZONTAL, command=dorks_name.xview)
scroli.grid(row=4, column=7, sticky='sew')
dorks_name.configure(xscrollcommand=scroli.set)

name = Text(root, wrap=NONE, font="Courier 9", width=14, height=8)
name.grid(row=6, column=1, sticky='nswe')
scrols = Scrollbar(root, command=name.yview)
scrols.grid(row=6, column=2, sticky='nsw')
name.configure(yscrollcommand=scrols.set)
scrolt = Scrollbar(root, orient=HORIZONTAL, command=name.xview)
scrolt.grid(row=7, column=1, sticky='sew')
name.configure(xscrollcommand=scrolt.set)

type = Text(root, wrap=NONE, font="Courier 9", width=10, height=8)
type.grid(row=6, column=3, sticky='nswe')
scro = Scrollbar(root, command=type.yview)
scro.grid(row=6, column=4, sticky='nsw')
type.configure(yscrollcommand=scro.set)
scroltt = Scrollbar(root, orient=HORIZONTAL, command=type.xview)
scroltt.grid(row=7, column=3, sticky='sew')
type.configure(xscrollcommand=scroltt.set)

para = Text(root, wrap=NONE, font="Courier 9", width=14, height=8)
para.grid(row=6, column=5, sticky='nswe')
scr = Scrollbar(root, command=para.yview)
scr.grid(row=6, column=6, sticky='nse')
para.configure(yscrollcommand=scr.set)
scroltz = Scrollbar(root, orient=HORIZONTAL, command=para.xview)
scroltz.grid(row=7, column=5, sticky='sew')
para.configure(xscrollcommand=scroltz.set)

root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()

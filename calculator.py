from cProfile import label
from logging import exception
from msilib.schema import Binary
from tkinter import *
import math
from tkinter.tix import InputOnly
import coden as code
import tkinter.messagebox
import numpy as np
import threading

root = Tk()
root.title("Scientific Calculator")
root.configure(background="white")
root.resizable(width=False, height=False)
root.geometry("480x568")  # 450+90

calc = Frame(root)
calc.grid()


# icon code
# icon = PhotoImage(file="icon.png")
# root.iconphoto(True, icon)


# function using class and object
class Calc:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    # def module(self):
    #     self.a=txtDisplay.get()

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()

        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        try:
            if self.op == "add":
                self.total += self.current

            if self.op == "sub":
                self.total -= self.current

            if self.op == "multi":
                self.total *= self.current

            if self.op == "divide":
                self.total /= self.current

            if self.op == "mod":
                self.total %= self.current

            self.input_value = True
            self.check_sum = False
            self.display(self.total)

        except Exception:
            e = "invalid"
            self.display(e)
            self.total = 0
            self.current = ""
            self.input_value = True
            self.check_sum = False
            self.op = ""
            self.result = False

    def operation(self, op):
        self.current = float(self.current)

        if self.check_sum:
            self.valid_function()

        elif not self.result:
            self.total = self.current
            self.input_value = True

        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

        # next entry clear box
        set = ""
        input_text.set(set)
        a1.set(set)
        b1.set(set)
        c1.set(set)
        d1.set(set)

        a2.set(set)
        b2.set(set)
        c2.set(set)
        d2.set(set)

        a3.set(set)
        b3.set(set)
        c3.set(set)
        d3.set(set)

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        # if self.current==1.0:
        #     self.a=1.5
        #     self.display(self.a)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    # conversion funtion
    def DTB(self):
        # self.expression
        # self.expression = float(txtDisplay.get())
        # input_text.set(self.expression)
        set = bin(int(input.get()))
        input_text.set(set)

    def DTO(self):
        # self.expression
        # expression = expression + str(item)
        # input_text.set(expression)
        set = oct(int(input.get()))
        input_text.set(set)

    def DTH(self):
        # self.expression
        # expression = expression + str(item)
        # input_text.set(expression)
        set = hex(int(input.get()))
        input_text.set(set)

    def BTD(self):
        # self.expression
        # expression = expression + str(item)
        # input_text.set(expression)

        set = code.bin_to_int(input.get())
        input_text.set(set)

        # def decimal(n):
        #     if self.n==0:
        #         self.a=0
        #         input_text.set(self.a)

        #     else:
        #         self.t=decimal(self.n//10)
        #         self.a=self.n%2 + 2*self.t
        #         input_text.set(self.a)

        # decimal(int(input.get()))

    def BTO(self):
        pass

    def BTH(self):
        set = code.bin_to_hex(int(input.get()))
        input_text.set(set)

    def OTD(self):
        # self.expression
        # expression = expression + str(item)
        # input_text.set(expression)
        def octal_to_decimal(n):
            decimal = 0
            multiplier = 1

            while n:
                digit = n % 10
                n = int(n / 10)
                decimal += digit * multiplier
                multiplier = multiplier * 8
            return decimal

        no = int(int(input.get()))
        input_text.set(octal_to_decimal(no))

    def OTB(self):
        set = bin(int(input.get()))
        input_text.set(set)

    def OTH(self):
        set = hex(int(input.get()))
        input_text.set(set)

    def HTD(self):
        # self.expression
        # expression = expression + str(item)
        # input_text.set(expression)
        set = code.hex_to_int(str(input.get()))
        input_text.set(set)

    def HTB(self):
        # self.expression
        # expression = expression + str(item)
        # input_text.set(expression)
        set = code.hex_to_bin(str(input.get()))
        input_text.set(set)

    def HTO(self):
        set = oct(int(input.get()))
        input_text.set(set)

    # equation function
    # submit button
    def submit(self):
        if (
            a1.get()
            and b1.get()
            and c1.get()
            and d1.get()
            and a2.get()
            and b2.get()
            and c2.get()
            and d2.get()
            and a3.get()
            and b3.get()
            and c3.get()
            and d3.get()
        ):
            try:
                self.a1 = eval(a1.get())
                self.b1 = eval(b1.get())  # -->first equation
                self.c1 = eval(c1.get())
                self.d1 = eval(d1.get())

                self.a2 = eval(a2.get())
                self.b2 = eval(b2.get())  # -->second equation
                self.c2 = eval(c2.get())
                self.d2 = eval(d2.get())

                self.a3 = eval(a3.get())
                self.b3 = eval(b3.get())
                self.c3 = eval(c3.get())  ##-->third equation
                self.d3 = eval(d3.get())

                A = np.array(
                    [
                        [self.a1, self.b1, self.c1],
                        [self.a2, self.b2, self.c2],
                        [self.a3, self.b3, self.c3],
                    ]
                )
                b = np.array([self.d1, self.d2, self.d3])
                z = np.linalg.solve(A, b)
                list = z.tolist()
                x = format(float(list[0]), ".2f")
                y = format(float(list[1]), ".2f")
                z = format(float(list[2]), ".2f")
                om = "x=", x, "y=", y, "z=", z
                input.set(om)

            except Exception:
                e = "invalid input"
                input.set(e)

        elif a1.get() and b1.get() and c1.get() and a2.get() and b2.get() and c2.get():
            try:
                self.a1 = eval(a1.get())
                self.b1 = eval(b1.get())  # -->first equation
                self.c1 = eval(c1.get())

                self.a2 = eval(a2.get())
                self.b2 = eval(b2.get())  # -->second equation
                self.c2 = eval(c2.get())

                A = np.array([[self.a1, self.b1], [self.a2, self.b2]])
                b = np.array([self.c1, self.c2])
                z = np.linalg.solve(A, b)
                list = z.tolist()
                x = format(float(list[0]), ".2f")
                y = format(float(list[1]), ".2f")
                om = "x=", x, "y=", y
                input.set(om)

            except Exception:
                e = "invalid input"
                input.set(e)
        else:
            e = "invalid input"
            input.set(e)

    # temperature conversion function
    def CTF(self):
        self.cel = float(input.get())
        self.Fer = (self.cel * 9 / 5) + 32
        input_text.set(self.Fer)

    def CTK(self):
        self.cel = float(input.get())
        self.kel = self.cel + 273.15
        input_text.set(self.kel)

    def FTC(self):
        self.fer = float(input.get())
        self.cel = 5 / 9 * (self.fer - 32)
        input_text.set(self.cel)

    def FTK(self):
        self.fer = float(input.get())
        self.kel = (self.fer * 9 / 5) + 32
        input_text.set(self.kel)

    def KTC(self):
        self.kel = float(input.get())
        self.cel = self.kel - 273.15
        input_text.set(self.cel)

    def KTF(self):
        self.kel = float(input.get())
        self.Fer = (self.kel - 273.15) * 9 / 5 + 32
        input_text.set(self.Fer)

    # unit conversion funtion
    def MTC(self):
        self.meter = float(input.get())
        self.cen = self.meter * 100
        input.set(self.cen)

    def MTK(self):
        self.meter = float(input.get())
        self.kilo = self.meter / 1000
        input.set(self.kilo)

    def KTG(self):
        self.kilo = float(input.get())
        self.gram = self.kilo * 1000
        input.set(self.gram)

    def KTP(self):
        self.kilo = float(input.get())
        self.pound = self.kilo * 2.2
        input.set(self.pound)

    def LTM(self):
        self.litter = float(input.get())
        self.mililitter = self.litter / 1000
        input.set(self.mililitter)

    def LTK(self):
        self.litter = float(input.get())
        self.kilolitter = self.litter / 1000
        input.set(self.kilolitter)

    def FTI(self):
        self.ft = float(input.get())
        self.inch = self.ft * 12
        input.set(self.inch)

    def STH(self):
        self.second = float(input.get())
        self.hour = (self.second / 60) / 60
        input.set(self.hour)

    def STM(self):
        self.second = float(input.get())
        self.minute = self.second / 60
        input.set(self.minute)

    def MTH(self):
        self.minute = float(input.get())
        self.hour = self.minute / 60
        input.set(self.hour)

    def MTS(self):
        self.minute = float(input.get())
        self.second = self.minute * 60
        input.set(self.second)

    def HTS(self):
        self.hour = float(input.get())
        self.second = self.hour * 60 * 60
        input.set(self.second)


# third screen entry box
input_text = StringVar()
ConDisplay = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="black",
    fg="white",
    textvariable=input_text,
    bd=30,
    width=18,
    justify=RIGHT,
)
ConDisplay.grid(row=0, column=7, columnspan=7, pady=1)


lblDisplay = Label(
    calc,
    text="Conversion",
    font=("Helvetica", 30, "bold"),
    bg="black",
    fg="white",
    justify=CENTER,
)

lblDisplay.grid(row=1, column=8, columnspan=3)


# conversion button
DecimalToBinary = Button(
    calc,
    text="DTB",
    width=6,
    height=2,
    bg="Blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.DTB(),
).grid(row=2, column=8, columnspan=1, padx=1)

DecimalToOctal = Button(
    calc,
    text="DTO",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.DTO(),
).grid(row=2, column=9, columnspan=1, padx=1)

DecimalToHexa = Button(
    calc,
    text="DTH",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.DTH(),
).grid(row=2, column=10, columnspan=1, padx=1)


BinaryToDecimal = Button(
    calc,
    text="BTD",
    width=6,
    height=2,
    bg="Blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.BTD(),
).grid(row=3, column=8, columnspan=1, padx=1)

BinaryToOctal = Button(
    calc,
    text="BTO",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.BTO(),
).grid(row=3, column=9, columnspan=1, padx=1)

BinaryToHexa = Button(
    calc,
    text="BTH",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.BTH(),
).grid(row=3, column=10, columnspan=1, padx=1)

OctalToDecimal = Button(
    calc,
    text="OTD",
    width=6,
    height=2,
    bg="Blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.OTD(),
).grid(row=4, column=8, columnspan=1, padx=1)

OctalToBinary = Button(
    calc,
    text="OTB",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.OTB(),
).grid(row=4, column=9, columnspan=1, padx=1)

OctalToHexa = Button(
    calc,
    text="OTH",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.OTH(),
).grid(row=4, column=10, columnspan=1, padx=1)

HexaToDecimal = Button(
    calc,
    text="HTD",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.HTD(),
).grid(row=5, column=8, columnspan=1, padx=1)

HexaToBinary = Button(
    calc,
    text="HTB",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.HTB(),
).grid(row=5, column=9, columnspan=1, padx=1)


HexaToOctal = Button(
    calc,
    text="HTO",
    width=6,
    height=2,
    bg="blue",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.HTO(),
).grid(row=5, column=10, columnspan=1, padx=1)


# four screen design
# temperature conversion conversion design
CelsiusToFahrenheit = Button(
    calc,
    text="CTF",
    width=6,
    height=2,
    bg="orange",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.CTF(),
).grid(row=0, column=11, columnspan=1)

CelsiusToKelvin = Button(
    calc,
    text="CTK",
    width=6,
    height=2,
    bg="orange",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.CTK(),
).grid(row=1, column=11, columnspan=1)

FahrenheitToCelsius = Button(
    calc,
    text="FTC",
    width=6,
    height=2,
    bg="orange",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.FTC(),
).grid(row=2, column=11, columnspan=1)

FahrenheitToKelvin = Button(
    calc,
    text="FTK",
    width=6,
    height=2,
    bg="orange",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.FTK(),
).grid(row=3, column=11, columnspan=1)

KelvinToCelsius = Button(
    calc,
    text="KTC",
    width=6,
    height=2,
    bg="orange",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.KTC(),
).grid(row=4, column=11, columnspan=1)

KelvinToFahrenheit = Button(
    calc,
    text="KTF",
    width=6,
    height=2,
    bg="orange",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.KTF(),
).grid(row=5, column=11, columnspan=1)


# fift screen design
# unit converson
MeterToCentimeter = Button(
    calc,
    text="MTC",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.MTC(),
).grid(row=6, column=0)


MeterToKilometer = Button(
    calc,
    text="MTK",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.MTK(),
).grid(row=6, column=1)


KilogramToGram = Button(
    calc,
    text="KTG",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.KTG(),
).grid(row=6, column=2)


KilogramToPound = Button(
    calc,
    text="KTP",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.KTP(),
).grid(row=6, column=3)


LitterToMillilitter = Button(
    calc,
    text="LTM",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.LTM(),
).grid(row=6, column=4)


LitterToKilolitter = Button(
    calc,
    text="LTK",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.LTK(),
).grid(row=6, column=5)


FeetToInches = Button(
    calc,
    text="FTI",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.FTI(),
).grid(row=6, column=6)


SecondToHour = Button(
    calc,
    text="STH",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.STH(),
).grid(row=6, column=7)


SecondToMinute = Button(
    calc,
    text="STM",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.STM(),
).grid(row=6, column=8)


MinuteToHour = Button(
    calc,
    text="MTH",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.MTH(),
).grid(row=6, column=9)


MinuteToSecond = Button(
    calc,
    text="MTS",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.MTS(),
).grid(row=6, column=10)


HourToSecond = Button(
    calc,
    text="HTS",
    width=6,
    height=1,
    bg="red",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=1,
    command=lambda: added_value.HTS(),
).grid(row=6, column=11)


# six screen design
# equation design

lblDisplay = Label(
    calc,
    text="Equation",
    font=("Helvetica", 25, "bold"),
    bg="black",
    fg="white",
    justify=CENTER,
)

lblDisplay.grid(row=7, column=4, columnspan=4)


# row 7 column 0
a1 = StringVar()
a = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=a1,
    justify=LEFT,
)
a.grid(row=8, column=0)

# row7 column 1
b1 = StringVar()
b = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    width=6,
    cursor="hand2",
    textvariable=b1,
    justify=LEFT,
)
b.grid(row=8, column=1)

# row7 column 2
c1 = StringVar()
c = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=c1,
    justify=LEFT,
)
c.grid(row=8, column=2)

# row7 column 3
d1 = StringVar()
d = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=d1,
    justify=LEFT,
)
d.grid(row=8, column=3)


# row 8 column 0
a2 = StringVar()
a = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=a2,
    justify=LEFT,
)
a.grid(row=9, column=0)

# row8 column 1
b2 = StringVar()
b = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    width=6,
    cursor="hand2",
    textvariable=b2,
    justify=LEFT,
)
b.grid(row=9, column=1)

# row8 column 2
c2 = StringVar()
c = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=c2,
    justify=LEFT,
)
c.grid(row=9, column=2)

# row8 column 3
d2 = StringVar()
d = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=d2,
    justify=LEFT,
)
d.grid(row=9, column=3)


# row 9 column 0
a3 = StringVar()
a = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=a3,
    justify=LEFT,
)
a.grid(row=10, column=0)


# row9 column 1
b3 = StringVar()
b = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    width=6,
    cursor="hand2",
    textvariable=b3,
    justify=LEFT,
)
b.grid(row=10, column=1)


# row9 column 2
c3 = StringVar()
c = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=c3,
    justify=LEFT,
)
c.grid(row=10, column=2)


# row9 column 3
d3 = StringVar()
d = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    bg="gray",
    fg="BLACK",
    bd=2,
    cursor="hand2",
    width=6,
    textvariable=d3,
    justify=LEFT,
)
d.grid(row=10, column=3)


# row 7 columb 5
x = Label(
    calc,
    text="a1X + b1Y + c1Z = d1",
    bg="gray",
    font=("Helvetica", 20, "bold"),
    fg="black",
    justify=CENTER,
)
x.grid(row=8, column=8, columnspan=8)


# row 8 columb 5
x = Label(
    calc,
    text="a2X + b2Y + c2Z = d2",
    bg="gray",
    font=("Helvetica", 20, "bold"),
    fg="black",
    justify=CENTER,
)
x.grid(row=9, column=8, columnspan=8)


# row 9 columb 5
x = Label(
    calc,
    text="a3X + b3Y + c3Z = d3",
    bg="gray",
    font=("Helvetica", 20, "bold"),
    fg="black",
    justify=CENTER,
)
x.grid(row=10, column=8, columnspan=8)


Submit = Button(
    calc,
    text="Submit",
    width=6,
    height=1,
    bg="black",
    fg="white",
    cursor="hand2",
    font=("Helvetica", 18, "bold"),
    bd=2,
    command=lambda: added_value.submit(),
).grid(row=9, column=4, columnspan=4)


# this is first Screen design

added_value = Calc()
input = StringVar()
txtDisplay = Entry(
    calc,
    font=("Helvetica", 20, "bold"),
    textvariable=input,
    bg="black",
    fg="white",
    bd=30,
    width=28,
    justify=RIGHT,
)

txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


# this is button using for loop
numberpad = "789456123"
i = 0
btn = []

for j in range(2, 5):
    for k in range(3):
        btn.append(
            Button(
                calc,
                width=6,
                height=2,
                bg="black",
                fg="white",
                font=("Helvetica", 20, "bold"),
                bd=4,
                text=numberpad[i],
            )
        )
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1


# button in first screen
btnClear = Button(
    calc,
    text=chr(67),
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.Clear_Entry,
).grid(row=1, column=0, pady=1)


btnAllClear = Button(
    calc,
    text=chr(67) + chr(69),
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.All_Clear_Entry,
).grid(row=1, column=1, pady=1)


btnsq = Button(
    calc,
    text="\u221A",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.squared,
).grid(row=1, column=2, pady=1)


btnAdd = Button(
    calc,
    text="+",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.operation("add"),
).grid(row=1, column=3, pady=1)


btnSub = Button(
    calc,
    text="-",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.operation("sub"),
).grid(row=2, column=3, pady=1)


btnMul = Button(
    calc,
    text="x",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.operation("multi"),
).grid(row=3, column=3, pady=1)


btnDiv = Button(
    calc,
    text="/",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.operation("divide"),
).grid(row=4, column=3, pady=1)


btnZero = Button(
    calc,
    text="0",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.numberEnter(0),
).grid(row=5, column=0, pady=1)


btnDot = Button(
    calc,
    text=".",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.numberEnter("."),
).grid(row=5, column=1, pady=1)

btnPM = Button(
    calc,
    text=chr(177),
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.mathPM,
).grid(row=5, column=2, pady=1)

btnEquals = Button(
    calc,
    text="=",
    width=6,
    height=2,
    bg="powder blue",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.sum_of_total,
).grid(row=5, column=3, pady=1)


# second screen button
# ROW 1 :
btnPi = Button(
    calc,
    text="pi",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.pi,
).grid(row=1, column=4, pady=1)


btnCos = Button(
    calc,
    text="Cos",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.cos,
).grid(row=1, column=5, pady=1)


btntan = Button(
    calc,
    text="tan",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.tan,
).grid(row=1, column=6, pady=1)


btnsin = Button(
    calc,
    text="sin",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.sin,
).grid(row=1, column=7, pady=1)

# ROW 2 :

btn2Pi = Button(
    calc,
    text="2pi",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.tau,
).grid(row=2, column=4, pady=1)


btnCosh = Button(
    calc,
    text="Cosh",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.cosh,
).grid(row=2, column=5, pady=1)


btntanh = Button(
    calc,
    text="tanh",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.tanh,
).grid(row=2, column=6, pady=1)


btnsinh = Button(
    calc,
    text="sinh",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.sinh,
).grid(row=2, column=7, pady=1)

# ROW 3 :

btnlog = Button(
    calc,
    text="log",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.log,
).grid(row=3, column=4, pady=1)


btnExp = Button(
    calc,
    text="exp",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.exp,
).grid(row=3, column=5, pady=1)


btnMod = Button(
    calc,
    text="Mod",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=lambda: added_value.operation("mod"),
).grid(row=3, column=6, pady=1)


btnE = Button(
    calc,
    text="e",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.e,
).grid(row=3, column=7, pady=1)

# ROW 4 :

btnlog10 = Button(
    calc,
    text="log10",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.log10,
).grid(row=4, column=4, pady=1)


btncos = Button(
    calc,
    text="log1p",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.log1p,
).grid(row=4, column=5, pady=1)


btnexpm1 = Button(
    calc,
    text="expm1",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.expm1,
).grid(row=4, column=6, pady=1)


btngamma = Button(
    calc,
    text="gamma",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.lgamma,
).grid(row=4, column=7, pady=1)
# ROW 5 :

btnlog2 = Button(
    calc,
    text="log2",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.log2,
).grid(row=5, column=4, pady=1)


btndeg = Button(
    calc,
    text="deg",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.degrees,
).grid(row=5, column=5, pady=1)


btnacosh = Button(
    calc,
    text="acosh",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.acosh,
).grid(row=5, column=6, pady=1)


btnasinh = Button(
    calc,
    text="asinh",
    width=6,
    height=2,
    bg="black",
    fg="white",
    font=("Helvetica", 20, "bold"),
    bd=4,
    command=added_value.asinh,
).grid(row=5, column=7, pady=1)


lblDisplay = Label(
    calc,
    text="Scientific Calculator",
    font=("Helvetica", 30, "bold"),
    bg="black",
    fg="white",
    justify=CENTER,
)

lblDisplay.grid(row=0, column=4, columnspan=4)


# exit message box function
def iExit():
    iExit = tkinter.messagebox.askyesno(
        "Scientific Calculator", "Do you want to exit ?"
    )

    if iExit > 0:
        root.destroy()
        return


# second screen
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


# first screen
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")


# third screen
def Conversion():
    root.resizable(width=False, height=False)
    root.geometry("1300x568")


# fift screen
def Temperature():
    root.resizable(width=False, height=False)
    root.geometry("1418x568+0+0")


def Unit_Conversion():
    root.resizable(width=False, height=False)
    root.geometry("1418x622+0+0")


# fourt screen function
def Equation():
    root.resizable(width=False, height=False)
    root.geometry("1418x808+0+0")


# menubar object
menubar = Menu(calc)

# ManuBar 1 :
filemenu = Menu(menubar)  # tearoff=0
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_command(label="Conversion", command=Conversion)
filemenu.add_command(label="Temperature", command=Temperature)
filemenu.add_command(label="Unit Conversion", command=Unit_Conversion)
filemenu.add_command(label="Equation", command=Equation)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)


# ManuBar 2 :
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")


if __name__ == "__main__":
    # Start Flask API in a separate thread
    threading.Thread(
        target=lambda: app.run(debug=False, host="0.0.0.0", port=5000)
    ).start()
    # # Start Tkinter GUI
    # start_gui()
    root.config(menu=menubar)
    root.mainloop()

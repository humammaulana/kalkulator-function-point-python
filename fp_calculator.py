from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Function Point Calculator")
root.geometry('770x710')

bobotRCAF = [
    "-- Pilih --",
    "(0) Tidak pengaruh",
    "(1) Insidental",
    "(2) Moderat",
    "(3) Rata-rata",
    "(4) Signifikan",
    "(5) Essential"
]


def hitung_fp():
    #RESET NILAI
    CFPtotal = 0
    rcafTotal = 0
    fpTotal = 0

    #HITUNG CFP
    CFPinput_low = int(entry_CFPinput_low.get())
    CFPinput_mid = int(entry_CFPinput_mid.get())
    CFPinput_hi = int(entry_CFPinput_hi.get())
    CFPoutput_low = int(entry_CFPoutput_low.get())
    CFPoutput_mid = int(entry_CFPoutput_mid.get())
    CFPoutput_hi = int(entry_CFPoutput_hi.get())
    CFPquery_low = int(entry_CFPquery_low.get())
    CFPquery_mid = int(entry_CFPquery_mid.get())
    CFPquery_hi = int(entry_CFPquery_hi.get())
    CFPfile_low = int(entry_CFPfile_low.get())
    CFPfile_mid = int(entry_CFPfile_mid.get())
    CFPfile_hi = int(entry_CFPfile_hi.get())
    CFPinterfaceExt_low = int(entry_CFPinterfaceExt_low.get())
    CFPinterfaceExt_mid = int(entry_CFPinterfaceExt_mid.get())
    CFPinterfaceExt_hi = int(entry_CFPinterfaceExt_hi.get())
    
    CFPinput_total = CFPinput_low*3 + CFPinput_mid*4 + CFPinput_hi*6
    CFPoutput_total = CFPoutput_low*4 + CFPoutput_mid*5 + CFPoutput_hi*7
    CFPquery_total = CFPquery_low*3 + CFPquery_mid*4 + CFPquery_hi*6
    CFPfile_total = CFPfile_low*7 + CFPfile_mid*10 + CFPfile_hi*15
    CFPinterfaceExt_total = CFPinterfaceExt_low*6 + CFPinterfaceExt_mid*7 + CFPinterfaceExt_hi*10

    CFPtotal = CFPinput_total + CFPoutput_total + CFPquery_total + CFPfile_total + CFPinterfaceExt_total
    
    entry_CFPtotal.config(state='normal')
    entry_CFPtotal.delete(0, 'end')
    entry_CFPtotal.insert(0, CFPtotal)
    entry_CFPtotal.config(state='readonly')


    #HITUNG RCAF
    #rcaf1
    if combo_RCAF1.get() == bobotRCAF[1]:
        rcaf1 = 0
    elif combo_RCAF1.get() == bobotRCAF[2]:
        rcaf1 = 1
    elif combo_RCAF1.get() == bobotRCAF[3]:
        rcaf1 = 2
    elif combo_RCAF1.get() == bobotRCAF[4]:
        rcaf1 = 3
    elif combo_RCAF1.get() == bobotRCAF[5]:
        rcaf1 = 4
    elif combo_RCAF1.get() == bobotRCAF[6]:
        rcaf1 = 5
    else:
        rcaf1 = 0

    #rcaf2
    if combo_RCAF2.get() == bobotRCAF[1]:
        rcaf2 = 0
    elif combo_RCAF2.get() == bobotRCAF[2]:
        rcaf2 = 1
    elif combo_RCAF2.get() == bobotRCAF[3]:
        rcaf2 = 2
    elif combo_RCAF2.get() == bobotRCAF[4]:
        rcaf2 = 3
    elif combo_RCAF2.get() == bobotRCAF[5]:
        rcaf2 = 4
    elif combo_RCAF2.get() == bobotRCAF[6]:
        rcaf2 = 5
    else:
        rcaf2 = 0

    #rcaf3
    if combo_RCAF3.get() == bobotRCAF[1]:
        rcaf3 = 0
    elif combo_RCAF3.get() == bobotRCAF[2]:
        rcaf3 = 1
    elif combo_RCAF3.get() == bobotRCAF[3]:
        rcaf3 = 2
    elif combo_RCAF3.get() == bobotRCAF[4]:
        rcaf3 = 3
    elif combo_RCAF3.get() == bobotRCAF[5]:
        rcaf3 = 4
    elif combo_RCAF3.get() == bobotRCAF[6]:
        rcaf3 = 5
    else:
        rcaf3 = 0

    #rcaf4
    if combo_RCAF4.get() == bobotRCAF[1]:
        rcaf4 = 0
    elif combo_RCAF4.get() == bobotRCAF[2]:
        rcaf4 = 1
    elif combo_RCAF4.get() == bobotRCAF[3]:
        rcaf4 = 2
    elif combo_RCAF4.get() == bobotRCAF[4]:
        rcaf4 = 3
    elif combo_RCAF4.get() == bobotRCAF[5]:
        rcaf4 = 4
    elif combo_RCAF4.get() == bobotRCAF[6]:
        rcaf4 = 5
    else:
        rcaf4 = 0

    #rcaf5
    if combo_RCAF5.get() == bobotRCAF[1]:
        rcaf5 = 0
    elif combo_RCAF5.get() == bobotRCAF[2]:
        rcaf5 = 1
    elif combo_RCAF5.get() == bobotRCAF[3]:
        rcaf5 = 2
    elif combo_RCAF5.get() == bobotRCAF[4]:
        rcaf5 = 3
    elif combo_RCAF5.get() == bobotRCAF[5]:
        rcaf5 = 4
    elif combo_RCAF5.get() == bobotRCAF[6]:
        rcaf5 = 5
    else:
        rcaf5 = 0

    #rcaf6
    if combo_RCAF6.get() == bobotRCAF[1]:
        rcaf6 = 0
    elif combo_RCAF6.get() == bobotRCAF[2]:
        rcaf6 = 1
    elif combo_RCAF6.get() == bobotRCAF[3]:
        rcaf6 = 2
    elif combo_RCAF6.get() == bobotRCAF[4]:
        rcaf6 = 3
    elif combo_RCAF6.get() == bobotRCAF[5]:
        rcaf6 = 4
    elif combo_RCAF6.get() == bobotRCAF[6]:
        rcaf6 = 5
    else:
        rcaf6 = 0

    #rcaf7
    if combo_RCAF7.get() == bobotRCAF[1]:
        rcaf7 = 0
    elif combo_RCAF7.get() == bobotRCAF[2]:
        rcaf7 = 1
    elif combo_RCAF7.get() == bobotRCAF[3]:
        rcaf7 = 2
    elif combo_RCAF7.get() == bobotRCAF[4]:
        rcaf7 = 3
    elif combo_RCAF7.get() == bobotRCAF[5]:
        rcaf7 = 4
    elif combo_RCAF7.get() == bobotRCAF[6]:
        rcaf7 = 5
    else:
        rcaf7 = 0

    #rcaf8
    if combo_RCAF8.get() == bobotRCAF[1]:
        rcaf8 = 0
    elif combo_RCAF8.get() == bobotRCAF[2]:
        rcaf8 = 1
    elif combo_RCAF8.get() == bobotRCAF[3]:
        rcaf8 = 2
    elif combo_RCAF8.get() == bobotRCAF[4]:
        rcaf8 = 3
    elif combo_RCAF8.get() == bobotRCAF[5]:
        rcaf8 = 4
    elif combo_RCAF8.get() == bobotRCAF[6]:
        rcaf8 = 5
    else:
        rcaf8 = 0

    #rcaf9
    if combo_RCAF9.get() == bobotRCAF[1]:
        rcaf9 = 0
    elif combo_RCAF9.get() == bobotRCAF[2]:
        rcaf9 = 1
    elif combo_RCAF9.get() == bobotRCAF[3]:
        rcaf9 = 2
    elif combo_RCAF9.get() == bobotRCAF[4]:
        rcaf9 = 3
    elif combo_RCAF9.get() == bobotRCAF[5]:
        rcaf9 = 4
    elif combo_RCAF9.get() == bobotRCAF[6]:
        rcaf9 = 5
    else:
        rcaf9 = 0

    #rcaf10
    if combo_RCAF10.get() == bobotRCAF[1]:
        rcaf10 = 0
    elif combo_RCAF10.get() == bobotRCAF[2]:
        rcaf10 = 1
    elif combo_RCAF10.get() == bobotRCAF[3]:
        rcaf10 = 2
    elif combo_RCAF10.get() == bobotRCAF[4]:
        rcaf10 = 3
    elif combo_RCAF10.get() == bobotRCAF[5]:
        rcaf10 = 4
    elif combo_RCAF10.get() == bobotRCAF[6]:
        rcaf10 = 5
    else:
        rcaf10 = 0

    #rcaf11
    if combo_RCAF11.get() == bobotRCAF[1]:
        rcaf11 = 0
    elif combo_RCAF11.get() == bobotRCAF[2]:
        rcaf11 = 1
    elif combo_RCAF11.get() == bobotRCAF[3]:
        rcaf11 = 2
    elif combo_RCAF11.get() == bobotRCAF[4]:
        rcaf11 = 3
    elif combo_RCAF11.get() == bobotRCAF[5]:
        rcaf11 = 4
    elif combo_RCAF11.get() == bobotRCAF[6]:
        rcaf11 = 5
    else:
        rcaf11 = 0

    #rcaf12
    if combo_RCAF12.get() == bobotRCAF[1]:
        rcaf12 = 0
    elif combo_RCAF12.get() == bobotRCAF[2]:
        rcaf12 = 1
    elif combo_RCAF12.get() == bobotRCAF[3]:
        rcaf12 = 2
    elif combo_RCAF12.get() == bobotRCAF[4]:
        rcaf12 = 3
    elif combo_RCAF12.get() == bobotRCAF[5]:
        rcaf12 = 4
    elif combo_RCAF12.get() == bobotRCAF[6]:
        rcaf12 = 5
    else:
        rcaf12 = 0

    #rcaf13
    if combo_RCAF13.get() == bobotRCAF[1]:
        rcaf13 = 0
    elif combo_RCAF13.get() == bobotRCAF[2]:
        rcaf13 = 1
    elif combo_RCAF13.get() == bobotRCAF[3]:
        rcaf13 = 2
    elif combo_RCAF13.get() == bobotRCAF[4]:
        rcaf13 = 3
    elif combo_RCAF13.get() == bobotRCAF[5]:
        rcaf13 = 4
    elif combo_RCAF13.get() == bobotRCAF[6]:
        rcaf13 = 5
    else:
        rcaf13 = 0

    #rcaf14
    if combo_RCAF14.get() == bobotRCAF[1]:
        rcaf14 = 0
    elif combo_RCAF14.get() == bobotRCAF[2]:
        rcaf14 = 1
    elif combo_RCAF14.get() == bobotRCAF[3]:
        rcaf14 = 2
    elif combo_RCAF14.get() == bobotRCAF[4]:
        rcaf14 = 3
    elif combo_RCAF14.get() == bobotRCAF[5]:
        rcaf14 = 4
    elif combo_RCAF14.get() == bobotRCAF[6]:
        rcaf14 = 5
    else:
        rcaf14 = 0
    
    rcafTotal = rcaf1+rcaf2+rcaf3+rcaf4+rcaf5+rcaf6+rcaf7+rcaf8+rcaf9+rcaf10+rcaf11+rcaf12+rcaf13+rcaf14
    entry_RCAFtotal.config(state='normal')
    entry_RCAFtotal.delete(0, 'end')
    entry_RCAFtotal.insert(0, rcafTotal)
    entry_RCAFtotal.config(state='readonly')


    #HITUNG FP
    fpTotal = round(CFPtotal * (0.65 + (0.01 *rcafTotal)), 2)
    entry_FPtotal.config(state='normal')
    entry_FPtotal.delete(0, 'end')
    entry_FPtotal.insert(0, fpTotal)
    entry_FPtotal.config(state='readonly')



#label judul CFP
label_CFP = Label(root, text="Crude Function Point (CFP)", font=('Arial 12 bold'))
label_CFPlow = Label(root, text="Sederhana")
label_CFPmid = Label(root, text="Menengah")
label_CFPhi = Label(root, text="Kompleks")
#grid judul CFP
label_CFP.grid(column=0, row=0, columnspan=3,sticky=W, pady=8)
label_CFPlow.grid(column=1, row=1)
label_CFPmid.grid(column=2, row=1)
label_CFPhi.grid(column=3, row=1)

#label input CFP
label_CFPinput = Label(root, text="Input:")
label_CFPoutput = Label(root, text="Output:")
label_CFPquery = Label(root, text="Query/Search/View:")
label_CFPfile = Label(root, text="File/Tabel/Data:")
label_CFPinterfaceExt = Label(root, text="Interface External:")
label_CFPtotal = Label(root, text="TOTAL CFP:", font=('Arial 9 bold'))
#grid input CFP
label_CFPinput.grid(column=0, row=2, sticky=W)
label_CFPoutput.grid(column=0, row=3, sticky=W)
label_CFPquery.grid(column=0, row=4, sticky=W)
label_CFPfile.grid(column=0, row=5, sticky=W)
label_CFPinterfaceExt.grid(column=0, row=6, sticky=W)
label_CFPtotal.grid(column=0, row=7, sticky=W)

#entry CFP
entry_CFPinput_low = Entry(root, width=12, justify='center')
entry_CFPinput_mid = Entry(root, width=12, justify='center')
entry_CFPinput_hi = Entry(root, width=12, justify='center')
entry_CFPoutput_low = Entry(root, width=12, justify='center')
entry_CFPoutput_mid = Entry(root, width=12, justify='center')
entry_CFPoutput_hi = Entry(root, width=12, justify='center')
entry_CFPquery_low = Entry(root, width=12, justify='center')
entry_CFPquery_mid = Entry(root, width=12, justify='center')
entry_CFPquery_hi = Entry(root, width=12, justify='center')
entry_CFPfile_low = Entry(root, width=12, justify='center')
entry_CFPfile_mid = Entry(root, width=12, justify='center')
entry_CFPfile_hi = Entry(root, width=12, justify='center')
entry_CFPinterfaceExt_low = Entry(root, width=12, justify='center')
entry_CFPinterfaceExt_mid = Entry(root, width=12, justify='center')
entry_CFPinterfaceExt_hi = Entry(root, width=12, justify='center')
entry_CFPtotal = Entry(root, width=12, justify='center', state='readonly')
#grid entry CFP
entry_CFPinput_low.grid(column=1, row=2, padx=5, pady=3)
entry_CFPinput_mid.grid(column=2, row=2, padx=5, pady=3)
entry_CFPinput_hi.grid(column=3, row=2, padx=5, pady=3)
entry_CFPoutput_low.grid(column=1, row=3, padx=5, pady=3)
entry_CFPoutput_mid.grid(column=2, row=3, padx=5, pady=3)
entry_CFPoutput_hi.grid(column=3, row=3, padx=5, pady=3)
entry_CFPquery_low.grid(column=1, row=4, padx=5, pady=3)
entry_CFPquery_mid.grid(column=2, row=4, padx=5, pady=3)
entry_CFPquery_hi.grid(column=3, row=4, padx=5, pady=3)
entry_CFPfile_low.grid(column=1, row=5, padx=5, pady=3)
entry_CFPfile_mid.grid(column=2, row=5, padx=5, pady=3)
entry_CFPfile_hi.grid(column=3, row=5, padx=5, pady=3)
entry_CFPinterfaceExt_low.grid(column=1, row=6, padx=5, pady=3)
entry_CFPinterfaceExt_mid.grid(column=2, row=6, padx=5, pady=3)
entry_CFPinterfaceExt_hi.grid(column=3, row=6, padx=5, pady=3)
entry_CFPtotal.grid(column=1, row=7, padx=5, pady=3)


#label judul RCAF
label_RCAF = Label(root, text="Relative Complexity Adjustment Factor (RCAF)", font=('Arial 12 bold'))
#grid judul CFP
label_RCAF.grid(column=0, row=8, columnspan=4,sticky=W, pady=(8))

#label input RCAF
label_RCAF1 = Label(root, text="Data communication")
label_RCAF2 = Label(root, text="Distributed data processing")
label_RCAF3 = Label(root, text="Performance")
label_RCAF4 = Label(root, text="Heavily used configuration")
label_RCAF5 = Label(root, text="Transaction rate")
label_RCAF6 = Label(root, text="On-Line data entry")
label_RCAF7 = Label(root, text="End-user efficiency")
label_RCAF8 = Label(root, text="On-Line update")
label_RCAF9 = Label(root, text="Complex processing")
label_RCAF10 = Label(root, text="Reusability")
label_RCAF11 = Label(root, text="Installation ease")
label_RCAF12 = Label(root, text="Operational ease")
label_RCAF13 = Label(root, text="Multiple sites")
label_RCAF14 = Label(root, text="Facilitate change")
label_RCAFtotal = Label(root, text="TOTAL RCAF:", font=('Arial 9 bold'))
#grid input RCAF
label_RCAF1.grid(column=0, row=9, columnspan=2, sticky=W)
label_RCAF2.grid(column=0, row=10, columnspan=2, sticky=W)
label_RCAF3.grid(column=0, row=11, columnspan=2, sticky=W)
label_RCAF4.grid(column=0, row=12, columnspan=2, sticky=W)
label_RCAF5.grid(column=0, row=13, columnspan=2, sticky=W)
label_RCAF6.grid(column=0, row=14, columnspan=2, sticky=W)
label_RCAF7.grid(column=0, row=15, columnspan=2, sticky=W)
label_RCAF8.grid(column=0, row=16, columnspan=2, sticky=W)
label_RCAF9.grid(column=0, row=17, columnspan=2, sticky=W)
label_RCAF10.grid(column=0, row=18, columnspan=2, sticky=W)
label_RCAF11.grid(column=0, row=19, columnspan=2, sticky=W)
label_RCAF12.grid(column=0, row=20, columnspan=2, sticky=W)
label_RCAF13.grid(column=0, row=21, columnspan=2, sticky=W)
label_RCAF14.grid(column=0, row=22, columnspan=2, sticky=W)
label_RCAFtotal.grid(column=0, row=23, columnspan=2, sticky=W)

#entry total RCAF
entry_RCAFtotal = Entry(root, width=22, justify='center')
entry_RCAFtotal.grid(column=2, row=23)

#combo RCAF
combo_RCAF1 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF1.current(0)
combo_RCAF2 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF2.current(0)
combo_RCAF3 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF3.current(0)
combo_RCAF4 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF4.current(0)
combo_RCAF5 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF5.current(0)
combo_RCAF6 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF6.current(0)
combo_RCAF7 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF7.current(0)
combo_RCAF8 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF8.current(0)
combo_RCAF9 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF9.current(0)
combo_RCAF10 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF10.current(0)
combo_RCAF11 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF11.current(0)
combo_RCAF12 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF12.current(0)
combo_RCAF13 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF13.current(0)
combo_RCAF14 = ttk.Combobox(root, value=bobotRCAF, justify='center', state='readonly')
combo_RCAF14.current(0)
#grid combo RCAF
combo_RCAF1.grid(column=2, row=9, pady=3)
combo_RCAF2.grid(column=2, row=10, pady=3)
combo_RCAF3.grid(column=2, row=11, pady=3)
combo_RCAF4.grid(column=2, row=12, pady=3)
combo_RCAF5.grid(column=2, row=13, pady=3)
combo_RCAF6.grid(column=2, row=14, pady=3)
combo_RCAF7.grid(column=2, row=15, pady=3)
combo_RCAF8.grid(column=2, row=16, pady=3)
combo_RCAF9.grid(column=2, row=17, pady=3)
combo_RCAF10.grid(column=2, row=18, pady=3)
combo_RCAF11.grid(column=2, row=19, pady=3)
combo_RCAF12.grid(column=2, row=20, pady=3)
combo_RCAF13.grid(column=2, row=21, pady=3)
combo_RCAF14.grid(column=2, row=22, pady=3)

#label judul FP
label_FP = Label(root, text="Total Function Point", font=('Arial 12 bold'))
label_FPtotal = Label(root, text="TOTAL FP:", font=('Arial 9 bold'))
entry_FPtotal = Entry(root, justify='center', width=12, state='readonly')
#grid judul CFP
label_FP.grid(column=4, row=8, columnspan=4,sticky=W, pady=8, padx=(16, 0))
label_FPtotal.grid(column=4, row=9, sticky=W)
entry_FPtotal.grid(column=5, row=9, padx=32 ,pady=3)

#label

#button
button_hitung = Button(root, text="Hitung", command=hitung_fp)
#grid button
button_hitung.grid(column=6, row=9)

root.mainloop()
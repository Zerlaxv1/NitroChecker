import filecmp
import tkinter
import requests

def get_data(path, params):
    if not params:
        with open('file.txt', 'r') as f:
            for line in f:
                requeste(line)

def requeste(code):
    req = requests.get('https://discord.com/api/v8/entitlements/gift-codes/' + code)


#req = requests.get('https://discord.com/api/v8/entitlements/gift-codes/nE8kFKSzzxJJBSYxGptUAmcW')
#add limite of request /s
def choose():
    global rep
    print("1: check by a file")
    print("2: check with your clipboard")
    print("3: check by a url")
    rep = input('choose 1 or 2 or 3 or 4 : ')

choose()

if rep == 1:
    if tkinter:
        import tkinter
        from tkinter import filedialog
        tkinter.Tk().withdraw()
        input_file = filedialog.askdirectory()
    else:
        input_file = input('enter the path of the file : ')
         
    get_data(input_file)
elif rep == 2:
    if not pyperclip:
        print('you need pyperclip')
        choose()
        
    import pyperclip
    pyperclip.copy(input('paste your code here : '))
    req = requests.get('https://discord.com/api/v8/entitlements/gift-codes/' + pyperclip.paste())
    print(req.text)
elif rep == 3:
    x = input('paste your url here : ')
    req = requests.get(x)
    print(req.text)
    req = requests.get('https://discord.com/api/v8/entitlements/gift-codes/' + input('paste your code here : '))
    print(req.text) 

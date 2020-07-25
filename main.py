import tkinter as tk
import urllib.request
import json

root = tk.Tk()
root.title('YouTube subs count checker')
frame = tk.Frame(root)

idVar = tk.StringVar()
APIvar = tk.StringVar()
subsCount = tk.StringVar(); subsCount.set('-')

def check():
    global idVar, APIvar, subsCount
    print('Checking...')

    idStr = idVar.get()
    APIstr = APIvar.get()

    print(f'ID: {idStr}\nAPI: {APIstr}')

    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+idStr+"&key="+APIstr).read()
    subs = json.loads(data)['items'][0]['statistics']['subscriberCount']
    print(f'Subscribers: {subs}')
    subsCount.set(subs)
    print('...done')

tk.Label(frame, text='Channel id:').grid(row=0, column=0, sticky='E', padx=5, pady=0)
tk.Label(frame, text='API key:').grid(row=1, column=0, sticky='E', padx=5, pady=0)

tk.Entry(frame, textvariable=idVar, width=40).grid(row=0, column=1, sticky='W', padx=5, pady=5)
tk.Entry(frame, textvariable=APIvar, width=40).grid(row=1, column=1, sticky='W', padx=5, pady=5)

tk.Button(frame, text='Check', command=check).grid(row=3, column=0, columnspan=2, sticky='WE', padx=5, pady=5)

frame2 = tk.Frame(root, relief='ridge', borderwidth=4)
tk.Label(frame2, text='Subscribers:').grid(row=4, column=0, sticky='E', padx=5, pady=5)
tk.Label(frame2, textvariable=subsCount).grid(row=4, column=1, sticky='W', padx=5, pady=5)
frame.grid(row=0, column=0, padx=5, pady=5)
frame2.grid(row=1, column=0, padx=5, pady=5)
root.resizable(False, False)
root.mainloop()
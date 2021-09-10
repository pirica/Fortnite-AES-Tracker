# importing required modules for the software

from tkinter import *
import requests
import webbrowser


def main_static():
    # pass
    mn_api = 'https://fortnite-api.com/v2/aes'
    mn_json = requests.get(mn_api).json()
    status = mn_json['status']
    build = mn_json['data']['build']
    main_key = mn_json['data']['mainKey']
    label_static.config(text=f"Server Status: {status}\nCurrent Build: {build}\nMain Static AES: {main_key}")
    label_static.configure(foreground="green")


def dynamic_window():
    window = Toplevel(master=App)
    window.title("Dyanmic Keys for currently decrypted pakchunks")
    window.geometry('1000x1000')
    label_dynamic = Label(window, font=font_tuple)
    label_dynamic.pack()

    def dynamic_keys():
        # pass
        dy_api = 'https://fortnite-api.com/v2/aes'
        dy_json = requests.get(dy_api).json()
        dynamickey = dy_json['data']['dynamicKeys']
        for data in dynamickey:
            name = data['pakFilename']
            guid = data['pakGuid']
            key = data['key']
            dynamic_text = label_dynamic.cget("text") + f"\nName: {name}\nGuid: {guid}\nAES: {key}"
            label_dynamic.config(text=dynamic_text)


    dynamic_keys()



# ui code starts here

ytURL = 'https://www.youtube.com/channel/UCdqFdOJpMbyXGYnSAZdCX_Q'
githubURL = 'https://github.com/Ne10-Neon'
twitterURL = 'https://twitter.com/Neon__DEV'

def github_open():
    webbrowser.open(githubURL)

def twitter_open():
    webbrowser.open(twitterURL)

def youtube_open():
    webbrowser.open(ytURL)



# writing tkinter ui code

App = Tk()
App.title("Fortnite AES Tracker")
App.geometry('1000x1000')
font_tuple = ("calibri", 17)

git_image = PhotoImage(file='githubimage.png')
yt_image = PhotoImage(file='ytimage.png')
twt_image = PhotoImage(file='twitterimage.png')
fnapi_image = PhotoImage(file='fortnite-api.png')

label_static = Label(App, font = font_tuple)
label_static.pack(pady=10)
button_dyanmic = Button(App, font = font_tuple, text ="Show Dynamic AES Keys", command = dynamic_window)
button_dyanmic.pack()
button_yt = Button(App, font = font_tuple, image = yt_image, border = 0, command = youtube_open)
button_yt.place(x=30, y=30)
button_twitter = Button(App, font = font_tuple, image = twt_image, border = 0, command = twitter_open)
button_twitter.place(x=30, y=110)
button_github = Button(App, font = font_tuple, image = git_image, border = 0, command = github_open)
button_github.place(x=30, y=190)
apicredit = Label(App, font = font_tuple, text ="Powered by Fortnite API", image = fnapi_image, compound = 'bottom')
apicredit.pack(side=BOTTOM)




main_static()

App.mainloop()

# AES Tracker made by Neon [a.k.a Neonツ, Neon__DEV, Ne10-Neon] powered by FortniteAPI.
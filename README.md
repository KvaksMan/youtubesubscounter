# YouTube subscribers counter

## Video tutorial
https://youtu.be/ZSp5U3ztLU8

## Links:
https://console.developers.google.com/apis/

https://www.googleapis.com/youtube/v3/channels?part=statistics&id= _YourID_ &key= _YourAPI_


## Notes:
root = tk.Tk() - GUI intilizate

root.mainloop() - show GUI window

_widget_.grid() - place _widget_ at window grid

root.resizable(False,False) - make root a fixed size

root.title(’_title_’) - set window title to _title_

_widget_(_frame_) - create _widget_ in frame

f’Subscribers: {subs}’ = ‘Subscribers ’ + str(subs)

"""
importing all required
         modules
"""

import time
import tkinter
from tkinter import *
    
#------------------------------------------------------------------------------------------

"""  colors  for   later   use"""

c1 = '#4cadf7'
c2 = '#9167d3'
c3 = '#597fa0'
c4 = '#913c62'
c5 = '#916a3d'

#-------------------------------------------------------------------------------------------

"""
getting data from entry of
        'Enter Name' page
"""
def info () :

    global myname
    myname = entry_user.get('1.0' , 'end-1c')
                                                                        
    global chatbot                           
    chatbot = entry_chat.get('1.0' , 'end-1c')
    
    entry_user.delete('1.0' , END)
    entry_chat.delete('1.0' , END)

    frame_info.pack_forget ()
    frame_topic.pack ()
    
#------------------------------------------------------------------------------------------

"""
opening files after selection of
        topic in topic selestion
                    page
"""

def topic_1():
    global no_topic
    no_topic = 1
    
    global top
    top = 'd1_technology.txt'

    global a
    a = open( top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()    

    topic = 'Technology'
    label_topic.config(text = topic)

    refresh_screen()
    
def topic_2():
    global no_topic
    no_topic = 2


    global top
    top = 'd2_pakistan.txt'
    a = open(top , 'r')


    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()

    topic = ' Pakistan  '
    label_topic.config(text = topic)

    refresh_screen()
            
def topic_3():
    global no_topic
    no_topic = 3

    global top
    top = 'd3_islamichistory.txt'
    a = open(top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()

    topic = 'Islamic History'
    label_topic.config(text = topic)

    refresh_screen()

def topic_4():
    global no_topic
    no_topic = 4

    global top
    top = 'd4_physics.txt'
    a = open(top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()
    
    topic = ' Units of physical Quantities '
    label_topic.config(text = topic)

    refresh_screen()
    
def topic_5():
    global no_topic
    no_topic = 5

    global top
    top = 'd5_computer.txt'
    a = open( top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()

    topic = ' Input Output Devices '
    label_topic.config(text = topic)

    refresh_screen()

#----------------------------------------------------------------------------------------------------------

"""
functions for writing in files
        for writing in files in chat screen

"""

def write_ans () :

    enter1 = entry_feed.get('1.0' , END)

    b.write(enter1)
    b.close()

    window.destroy()

    """
                            Reopening of files after
                                changes are saved
    """

    if no_topic == 1 :
        topic_1()
    
    elif no_topic == 2 :
        topic_2()          
    
    elif no_topic == 3 :
        topic_3()
    
    elif no_topic == 4 :
        topic_4()
    
    elif no_topic == 5 :
        topic_5()
    
def feed_answer () :
    """
a seperate window for writing answer
            on file

    """
    global window
    window=Tk()

    frame_root = Frame(window , bg = c1)
    frame_root.pack()
                                                                                            
    label = Label (frame_root , text = 'Enter the answer of Question here ...' , bg = c1 , fg = 'white' )
    label.pack()

    global entry_feed
    entry_feed = Text (frame_root , height = 3 , width = 30 , fg = 'white' , bg = c2)
    entry_feed.bind ('<Return>' , write_ans)
    entry_feed.pack()

    button = Button (frame_root , text = 'Add answer' , command  = write_ans , bg = c3 , fg = 'white' )
    button.pack()
    
def write_file () :
    """
opening file for appending in
exsisting  files

    """
    global b
    b = open ( top , 'a')
    
    b.write(chat_raw)
    b.write('\n')

    button_write.place_forget()
    feed_answer ()

#----------------------------------------------------------------------------------------------

def refresh_screen () :

    for widget in frame_chats.winfo_children():
        widget.destroy()

    button_write.place_forget()
    label_space = Label (frame_chats , bg = c1 ,  text = '')
    label_space.pack()

#------------------------------------------------------------------------------------------

def submit() :

    """
function for producing response of
        request of user

    """
    button_write.place_forget ()
    global chat_raw
    chat_raw = entry.get('1.0' , 'end-1c')
                        
    entry.delete('1.0' , END)
    
    chat = chat_raw.lower()
    chat = chat.replace(' ','')

    global label_request
    label_request = Label(frame_chats ,text=chat_raw , bg = c5 , fg= 'white'  , justify = LEFT , wraplength = 300, font = 'Verdana 8 bold')
    
    label_request.pack(anchor = 'w')   
    
    global answer
    
    if chat == 'groupmembers' or chat == 'group' or chat == 'developers' or chat == 'groupmember':
          answer = "AHSAN EHTESHAM  \nISHAQ KAMRAN   \nMUHAMMAD FAHAD ALAM"

    elif chat == "what'smyname?" or chat == "whatsmyname?" or chat == "whatismyname?" or chat == "whatsmyname" or chat == 'myname?' or chat =='myname' :
          answer = myname

    elif chat == "what'syourname?" or chat == "whatisyourname?" or chat == "whatsyourname?" or chat == "whatsyourname" or chat == 'yourname?' or chat =='yourname' :
          answer = chatbot

    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end' :
          answer = 'Bye'

    else:
        i = 0
        j = 0
        for lines in doc:
             stats = lines [:-1]
             stats = stats.lower()
             stat = stats.replace(' ','')
             i += 1
             if stat == chat :
                    answer = doc[i]
                    break
             else:
                 j += 1
                 
        if i == j :
              answer = "I don't understand.........please teach me ! "
              button_write.place(x=430,y=3)

    get_response()
        
def get_response() :

    global label_response
    label_response = Label(frame_chats ,text= answer ,bg= c4 , fg = 'white' , justify = LEFT , wraplength = 300, font = 'Verdana 8 bold')

    label_response.pack(anchor = 'e')

    if answer ==  'Bye':
        root.destroy()


#------------------------------------------------------------------------------------------------------------------

"""
moving from one page to another
    by help of button

"""

def welcome_to_info () :
    frame_welcome.pack_forget ()
    frame_info.pack ()
    
def info_to_topic () :
    frame_info.pack_forget ()
    frame_topic.pack ()

def topic_to_chat () :
    frame_topic.pack_forget ()
    frame_chat.pack()

def chat_to_topic () :
    frame_chat.pack_forget ()
    frame_topic.pack ()

def topic_to_info () :
    frame_topic.pack_forget ()
    frame_info.pack ()

def info_to_welcome () :
    frame_info.pack_forget ()
    frame_welcome.pack ()

#-----------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
"""
calling constructor to make window

"""

root = Tk ()  

#----------------------------------------------------------------------------------------------------

"""  images used in window  """

back = PhotoImage(file = 'image_1.png')

front = PhotoImage(file = 'image_2.png')

arrow = PhotoImage (file = 'image_3.png')

exitt = PhotoImage(file = 'image_4.png')

screen_1 = PhotoImage(file = 'image_5.png')

enter_info = PhotoImage(file = 'image_6.png')

select_topic = PhotoImage(file = 'image_7.png')

submit_img = PhotoImage(file = 'image_8.png')

#---------------------------------------------------------------------------------------------------------------------

"""     WELCOME FRAME    """
"""    first frame containing time date and welcome messages """

frame_welcome = Frame (root , bg = c1 , height = '670' , width = '550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()                 

  
welcome = Label (frame_welcome , text = 'Welcome' , font = "Vardana 40 bold" , bg = c1 , fg = 'white')
welcome.place(x = 160, y = 200)

welcome_chatbot = Label (frame_welcome , text = 'I am Chatbot ! ' , font = "Helvetica 15 bold italic" , bg = c1 , fg = 'white')
welcome_chatbot.place(x = 200 , y = 270)

pic_1 = Label(frame_welcome , image = screen_1)
pic_1.place(x=0 , y = 357)

button_front = Button (frame_welcome , text = 'Front' , image = front, command = welcome_to_info ).place(x=500 , y=10)

#__________________________________________________________________

"""  time option  """

def clock () :
    current = time.strftime("%H:%M:%S")
    label_time = Label (frame_welcome ,bd = 5 ,  text = current , height = 1 , width = 8 , font = 'Ariel 11 bold' ,  fg = 'white' , relief = 'groove' , bg = c3)
    label_time.place(x= 120 , y = 63)

    label_time.after(1000 , clock )
   
button_time = Button (frame_welcome , text = 'Time' , height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg = 'white' ,  command = clock)
button_time.place(x=30 , y = 63)

#_____________________________________________________________________________

"""    date option   """

def date () :
    
    try:
        date = time.strftime("%d %B , 20%y")
        label_date = Label (frame_welcome , bd = 5 , relief = 'groove' ,  text = date , bg = c3 , fg ='white'  , height = 1 , font = 'Ariel 11 bold')
        label_date.place(x= 400 , y = 63)

        label_date.after(86400000 , date)
        
    except AttributeError:
        print('')        
        
        
button_date = Button (frame_welcome , text = 'Date' ,height = 1 , font = 'Vardana 10 bold' ,  width = 8 , bg = c2 , fg='white' , command = date)
button_date.place(x = 310 , y = 63)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""     INFO FRAME   """
"""     frame of entering names    """

frame_info = Frame (root , bg = c1 , height = '670' , width = '550')
frame_info.pack_propagate(0)


sub_frame = Frame (frame_info , height = '80' , width = '450' , bg = c2)
sub_frame.pack_propagate(0)
sub_frame.pack()

label_sub = Label (sub_frame ,image = enter_info , bg = c1 , fg = c2 , font = 'Verdana 30 italic')
label_sub.pack()
                            
user_name = Label (frame_info , text = 'Enter your name : ' , bg = c1 , fg = 'white' , font = 'Ariel 15')
user_name.place(x = 80,y=130)

entry_user = Text (frame_info , bg = c2, fg = 'white' , height ='1'  , width ='40' , font = 'Ariel 15')
entry_user.focus()
entry_user.place(x = 80 , y = 170)

chatbot_name = Label (frame_info , text = 'Enter ChatBot name : ' , bg = c1 , fg = 'white' , font = 'Ariel 15')
chatbot_name.place(x = 80 , y = 220)

entry_chat = Text (frame_info , bg = c2, fg = 'white' , height ='1'  , width ='40' , font = 'Ariel 15')
entry_chat.place(x = 80 , y = 260)

button_1 = Button (frame_info , text ='submit' , font = 'Vardana 10 bold' , bg = c2 , fg = 'white' , command = info )
button_1.place(x = 470 , y = 330)

button_back = Button (frame_info , text = 'Back' , image =  back , command = info_to_welcome).place(x=10 , y = 10)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""     TOPIC FRAME   """
""""   frame for topic selection     """

frame_topic = Frame (root , bg = c1 , height = '670' , width = '550')
frame_topic.pack_propagate(0)
                            
subframe = Frame (frame_topic , bg = c2 , height = '80' , width = '450')
subframe.pack_propagate(0)
subframe.pack()

select_label = Label (subframe , image = select_topic ,bg = c1 , fg = c2, font = 'Ariel 30 italic')
select_label.place(x = 55 , y = 2)

option_1 = Label (frame_topic , text = '1- Technology' , font = 'Verdana 15 italic' , bg = c1 , fg= 'white')
option_1.place(x = 30 , y = 120)

button_opt_1 = Button (frame_topic , text = 'Proceed' , image = arrow  ,command = topic_1)
button_opt_1.place(x = 350 , y = 120)

option_2 = Label (frame_topic , text = '2- Pakistan' , font = 'Verdana 15 italic' , bg = c1 , fg= 'white')
option_2.place(x = 30 , y = 160)

button_opt_2 = Button (frame_topic , text = 'Proceed' , image = arrow , command = topic_2)
button_opt_2.place(x = 350 , y = 160)

option_3 = Label (frame_topic , text = '3-  Islamic History ' , font = 'Verdana 15 italic' ,bg = c1 , fg= 'white')
option_3.place(x=30 , y = 200)

button_opt_3 = Button (frame_topic , text = 'Proceed' , image = arrow , command = topic_3)
button_opt_3.place(x = 350 , y = 200)

option_4 = Label (frame_topic , text = '4- Units of physical Quantities   ' , font = 'Verdana 15 italic' , bg = c1 , fg= 'white')
option_4.place(x = 30 , y = 240)

button_opt_4 = Button (frame_topic , text = 'Proceed' , image = arrow , command = topic_4)
button_opt_4.place(x = 350 , y = 240)

option_5 = Label (frame_topic , text = '5-  Input Output Devices ' , font = 'Verdana 15 italic' , bg = c1 , fg= 'white')
option_5.place(x = 30  , y = 280)

button_opt_5 = Button (frame_topic , text = 'Proceed' , image = arrow , command = topic_5)
button_opt_5.place(x = 350 , y = 280)

down_frame = Frame (frame_topic , height = '80' , width = '550' , bg = c2)
down_frame.pack_propagate(0)
down_frame.pack(side = BOTTOM)

button_back = Button (frame_topic , text = 'Back' , image = back , command = topic_to_info).place(x=10 , y = 10)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""         CHAT FRAME   """
""""       main chat screen   """

frame_chat = Frame (root , bg = c1 , height = '670' , width = '550')
frame_chat.pack_propagate(0)


top_frame = Frame (frame_chat , bg = c2 , height = '110' , width = '500')
top_frame.pack_propagate(0)
top_frame.pack()

label_topic = Label ( top_frame ,bg = c2 , fg = 'white' , font = 'Verdana 20 bold ')
label_topic.pack(pady = '40')


bottom_frame = Frame (frame_chat , bg = c2 , height = '100' , width = '500')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side = BOTTOM)

button = Button (bottom_frame , image = submit_img , font = 'Vardana 10 bold' , bg = c3 , command = submit )
button.place(x = 390 , y = 27)
                                   
entry = Text (bottom_frame , bg = c3 , fg = 'white' , height = '5'  , width ='45' , font  ='Verdana 10')
entry.bind ('<Return>' , submit)
entry.place(x = 17, y = 10)


frame_chats = Frame (frame_chat , bg = c1 , height = '450' , width = '500' )
frame_chats.pack_propagate (0)
frame_chats.pack()

label_space = Label(frame_chats , bg = c1).pack()

button_refresh = Button (top_frame , bg = c3 , fg = 'white' ,  text = 'refresh' , font = 'Vardana 10 bold' ,  command =refresh_screen)
button_refresh.place(x = 440 , y = 80)

button_write = Button (bottom_frame , text = 'write' ,bg = c3 ,fg = 'white' , font = 'Vardana 10 bold' ,  command = write_file )

button_back = Button (top_frame , text = 'Back' , image = back ,  command = chat_to_topic).place(x=10 , y = 10)
button_front = Button (top_frame , text = 'Exit' , image = exitt , command = root.destroy ).place(x=460 , y = 10)

#-----------------------------------------------------------------------------------------------------------

root.mainloop ()
"""    END OF CODE   """


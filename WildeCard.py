from tkinter import *
import random
from DictsForCompSciProject import option1dict, option2dict, option3dict, option4dict

root = Tk()
root.geometry("400x100")
# All Frames
frame = Frame(root)
frame.pack()

option1 = Frame(root)

option2 = Frame(root)

option3 = Frame(root)

option4 = Frame(root)

finalresult = Frame(root)
def startAgain():
    frame.pack()
    finalresult.pack_forget()


def changeScreen():
    if clicked.get() == "Sports":
        option1.pack()
        frame.pack_forget()
    elif clicked.get() == "Movies":
        option2.pack()
        frame.pack_forget()
    elif clicked.get() == "Video games":
        option3.pack()
        frame.pack_forget()
    elif clicked.get() == "Music":
        option4.pack()
        frame.pack_forget()

def finalCard():
    sportOption = clicked2.get()
    regionOption = clicked2b.get()
    teams = {i for i in option1dict if option1dict[i]==(sportOption, regionOption)}
    teams = list(teams)
    teams = random.choice(teams)
    sportcard = Label(finalresult, text= "You should watch an " + str(teams) + " game.").grid(row=2, column=5)
    finalresult.pack()
    option1.pack_forget()

def finalCard2():
    genreOption = clicked3.get()
    ageOption = clicked3b.get()
    movies = {i for i in option2dict if option2dict[i]==(genreOption, ageOption)}
    movies = list(movies)
    movies = random.choice(movies)
    moviecard = Label(finalresult, text= "You should watch " + str(movies) + ".").grid(row=2, column=5)
    finalresult.pack()
    option2.pack_forget()
    
def finalCard3():
    genre2Option = clicked4.get()
    consoleOption = clicked4b.get()
    videoGame = {i for i in option3dict if option3dict[i]==(consoleOption, genre2Option)}
    videoGame = list(videoGame)
    videoGame = random.choice(videoGame)
    videoGame = Label(finalresult, text= "You should play " + str(videoGame) + ".").grid(row=2, column=5)
    finalresult.pack()
    option3.pack_forget()

def finalCard4():
    genre3Option = clicked5.get()
    age3Option = clicked5b.get()
    music = {i for i in option4dict if option4dict[i]==(genre3Option, age3Option)}
    music = list(music)
    music = random.choice(music)
    moviecard = Label(finalresult, text= "You should Listen to " + str(music) + ".").grid(row=2, column=5)
    finalresult.pack()
    option4.pack_forget()
    
# Wilde Card Screen
myLabel = Label(frame, text="WILDE CARD").grid(row=0, column=5)

options = [
    "Sports",
    "Movies",
    "Video games",
    "Music"
]
  
clicked = StringVar() 
clicked.set( "Pick Intrests" )
drop = OptionMenu(frame, clicked , *options )
drop.grid(row=3, column=5)
button = Button(frame, text = "Go Deeper!" , command = changeScreen ).grid(row=4, column=5)
label = Label(frame, text = " " )
label.grid(row=5, column=5)

# Option 1 Screen

myLabel = Label(option1, text="Sports").grid(row=0, column=5)
buttonSport = Button(option1, text = "Find your card!" , command = finalCard ).grid(row=5, column=5)
difSports = [
    "Football",
    "Basketball",
    "Baseball",
    "Soccer"
]
clicked2 = StringVar()
clicked2.set( "Pick Sport" )
drop2 = OptionMenu(option1, clicked2 , *difSports )
drop2.grid(row=3, column=5)

difRegions = [
    "West",
    "Midwest",
    "Southwest",
    "Southeast",
    "Northeast"
]
clicked2b = StringVar()
clicked2b.set( "Pick Region" )
drop2b = OptionMenu(option1, clicked2b , *difRegions )
drop2b.grid(row=4, column=5)

# Option 2 Screen

myMoviesLabel = Label(option2, text="Movies").grid(row=0, column=5)
buttonMovies = Button(option2, text = "Find your card!" , command = finalCard2 ).grid(row=5, column=5)
difgenre = [
    "Action",
    "Comedy",
    "Romance",
    "Drama"
]
clicked3 = StringVar()
clicked3.set( "Pick Genre" )
drop3 = OptionMenu(option2, clicked3 , *difgenre )
drop3.grid(row=3, column=5)

difAges = [
    "0-12",
    "13-18",
    "19-24",
    "25+"
]
clicked3b = StringVar()
clicked3b.set( "Pick Age" )
drop3b = OptionMenu(option2, clicked3b , *difAges )
drop3b.grid(row=4, column=5)

# Option 3 Screen

myVideoGamesLabel = Label(option3, text="Video Games").grid(row=0, column=5)
buttonVideoGames = Button(option3, text = "Find your card!" , command = finalCard3 ).grid(row=5, column=5)
difgenre2 = [
    "Shooter",
    "Puzzle",
    "RPG",
    "Simulator"
]
difConsole = [
    "Playstation",
    "Nintendo Switch",
    "Xbox",
    "PC"
]
clicked4 = StringVar()
clicked4.set( "Pick Genre" )
drop4 = OptionMenu(option3, clicked4 , *difgenre2 )
drop4.grid(row=3, column=5)

clicked4b = StringVar()
clicked4b.set( "Pick Console" )
drop4b = OptionMenu(option3, clicked4b , *difConsole )
drop4b.grid(row=4, column=5)
# Option 4 Screen

myMusicLabel = Label(option4, text="Music").grid(row=0, column=5)
buttonMusic = Button(option4, text = "Find your card!" , command = finalCard4 ).grid(row=5, column=5)
difgenre3 = [
    "Rap",
    "Jazz",
    "Country",
    "Rock"
]
clicked5 = StringVar()
clicked5.set( "Pick Genre" )
drop5 = OptionMenu(option4, clicked5 , *difgenre3 )
drop5.grid(row=3, column=5)

clicked5b = StringVar()
clicked5b.set( "Pick Age" )
drop5b = OptionMenu(option4, clicked5b , *difAges )
drop5b.grid(row=4, column=5)

# Final result Screen
myFinalResultLabel = Label(finalresult, text="Your Wilde Card Is!").grid(row=0, column=5)
myFinalResultLabel2 = Label(finalresult, text="Have Fun!").grid(row=5, column=5)
buttonBegin = Button(finalresult, text = "Back to Start" , command = startAgain ).grid(row=6, column=5)



root.mainloop()



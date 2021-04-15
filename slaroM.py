import subprocess
import tkinter 
from tkinter import *
from tkinter import messagebox

answer1 = "yes"
answer2 = "no"

print("Hi, I'm Slarom The Clown")
print(r""",'_   _`.
   {{ |o| |o| }}
  {{{ '-'O'-' }}}
  {{( (`-.-') )}}
   {{{.`---',}}}
       `---'    """)
name = input("What is your name? ")
age = int(input("How old are you? "))

if age >= 18:
    print("Oooh", name, "You're definitely old enough.")

    wants_to_play = input("But hey, are you sure you want to continue? type yes or no ").lower()

    if wants_to_play == answer1:
        print("YAAAAAY XD")

        print("Now, I'm looking for a person with morals to become friends with")
        print("So, I'm going to ask you a bunch of questions to see if we're..compatible")
        
        question_1 = input("You come across a homeless man in desperate need of water; you have plenty to spare. Do you give him some? yes or no ").lower()

        if question_1 == answer1:
          window = Tk()
        #window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        #window.withdraw()

          messagebox.showinfo(':)', ':) :) :)')

        elif question_1 == answer2:
            messagebox.showinfo(':)', "HAHA, I like you already actually. I wouldn't give him any either")
            messagebox.showinfo(":D", "Some may think that's morally wrong but thankfully")
            messagebox.showinfo(":-)", "Morals are subjective. I like the way you think")
            messagebox.showinfo("Game won", "'you and slaroM have become friends'")
            exit()
        
        
         

        question_2 = input("Question 2: you walk past an alleyway and see this little kid being bullied by bigger kids. Do you help? Yes or No ").lower()


        if question_2 == answer1:
            print(r""".'  _     _  '.
          /   (o)   (o)   \
        |                 |
        |  \           /  |
                \  '.       .'  /
          '.  `'---'`  .'
                '-._____.""")
        question_3 = input("q̶̢̗͗̊u̴̧͇͈̲͉̹͖͐͌͒̏͋̋̇̎̕̕ḙ̷̢̡̢̢̛̛͙͍̣͉̳̳̗͚̝̗̭͙̜̯͋̾̄͐̈͆͒̽̂͑͆͗̄̅̑s̸̞̫̜̱̻͇̅̄̿̽̈́̈́̕͠ṯ̴̡̢̨̳͎̻͇̠̺̩̠̎̓̂̄̅̓̈́̀̐͘į̶̛͖͍͎̮̪̼̹͉̳͓̤̬͖̗͋̈́̈̾̎̿͘ͅờ̸̢͇̩̫̠͍͙̩̼̞͉͕̃͌͒̌̇̈́́̾̎̈́͠n̴̘̲̘̲̠̩̬̼̪͂̇̈́̈́̎̀ ̵͓̑̌́͒̀̄̽̃͛̚̚̕̚͜3̸̧̢̩͔̥̰͉̮͎͈͉̩̖̥͉̬͙̺̑͋͛̽͛̑̈́͗̏̀͗̈͘͘͜͜͝  You're walking down the street and see an old veteran trying to cross it. Do you help him? Yes or No ").lower()

        if question_3 == answer1:
            window = Tk()
        
        

        messagebox.showinfo(":(", "You know..I can't do this")
        messagebox.showinfo(":(", "No one ever ask me what my morals are")
        messagebox.showinfo(">.<", "You think just because you picked the 'good' answers")
        messagebox.showinfo(">.<", "That you're qualified to be my friend!")
        messagebox.showinfo(">.<", "'Oh, I care about the hobo, the vet and the kid..so he must too, right?!")
        messagebox.showinfo(">.<", "BULL! I don't care about any of them. Who says I have to? You? Society?")
        messagebox.showinfo(">.<", "Morals are subjective and I never said 'good' morals")
        messagebox.showinfo(">.<", "but what is 'good'? Your way right?' " )
        messagebox.showinfo("Game Over", "We are not friends.Enjoy the shutdown, dingus. hahahahaha")

        window.deiconify()
        window.destroy()
        window.quit()
        subprocess.call("shutdown/r", shell=True)

        

        
            

        


        
        

    

    elif wants_to_play == answer2:
        window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo(':)', 'Wrong choice, buddy :)')

    window.deiconify()
    window.destroy()
    window.quit()
    subprocess.call("dir/s", shell=True)


    

    
else:
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo('Nope', 'NO MUNCHKINS ALLOWED')
    messagebox.showinfo('>,<', 'I hope you forgot your parents login..DINGUS' )

    window.deiconify()
    window.destroy()
    window.quit()
    subprocess.call("shutdown/r", shell=True)
    
    


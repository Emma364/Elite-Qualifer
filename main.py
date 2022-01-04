#Chatbot by Emma Hamedian
#I used my own knowledge and some of my past replits in order to make this

print('Hello! My name is Roe. ')
name = input(f'What is your name? ')
print(f"Nice to meet you, {name}!")

question = input('How are you doing today?(Say either good or bad) ')
 

if question == "good":
  print("I'm glad that things are going well for you!")
elif question == "bad":
  print("I hope that things get better for you.")
  talk = input('Would you like to talk about it? ')
  if talk == "yes":
   answer_one = input("Ok, what are you having a hard time with? (Say school, work, or etc) ")
   if answer_one == "school":
    print("Are you failing any classes or is it something else? Well, I hope that whatever it is that you are having trouble on, whether it is school work or making new friends, you find the courage in you to continue to push on and work harder to pass!")
   elif answer_one == "work":
    print("Are you having trouble financially and you need a new job or are you having difficulty completing an assignemnt that was given to you? Honestly, as long as you work hard to achieve your goal everything will work out on its own. So don't give up!")
   elif answer_one == "etc":
    print("Well, whatever it is that is bothering you at the moment I hope that it gets better and to never say never!")
  elif talk == "no":
   print("That's ok! Everyone has things that they would like to keep to themselves.")
  
else:
  other = input(f"I don't understand {question}. Try saying something like good or bad. ")

#Happy new year!
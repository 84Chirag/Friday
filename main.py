import console as c
import datetime
import webbrowser
import os
from command import handle_command

console = c.Console()
EXIT_COMMANDS = ["exit", "quit", "bye", "goodbye", "nothing"]
hour = int(datetime.datetime.now().hour)
if 0 <= hour < 12:
    greeting ="Good Morning!"
elif 12 <= hour < 18:
    greeting ="Good Afternoon!"
else:
    greeting ="Good Evening!"
def greet():
    console.WriteLine(f"Hello {greeting}, I'm Friday your virtual assistant")
    day = datetime.datetime.now().strftime("%A")
    console.WriteLine(f"Today is {day}")
    return console.ReadLine("How can I help you?")

response = greet()

while response.lower() not in EXIT_COMMANDS:
    response = handle_command(response)
    if response.lower() not in EXIT_COMMANDS:
        response = console.ReadLine("What More can I do for you?")

console.WriteLine("Goodbye! Have a great day!")
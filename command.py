import console as c
import webbrowser
import os
from dotenv import load_dotenv

load_dotenv()
import smtplib
console = c.Console()
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendEmail(to, subject, content, attachment=None):
    server = smtplib.SMTP(os.environ.get('MAIL_HOST'), os.environ.get('MAIL_PORT'))
    server.ehlo()
    server.starttls()
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = os.environ.get('MAIL_ID')
    msg['To'] = to
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(content, 'plain'))

    # Handle attachment if provided
    if attachment:
        try:
            with open(attachment, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 
                              f'attachment; filename="{os.path.basename(attachment)}"')
                msg.attach(part)
        except Exception as e:
            raise Exception(f"Error with attachment: {str(e)}")

    try:
        server.login(os.environ.get('MAIL_ID'), os.environ.get('MAIL_PASS'))
        server.send_message(msg)
    finally:
        server.close()


def openingRes(res):
    console.WriteLine(f"Opening {res.capitalize()}")

def handle_command(command):
    command = command.lower()
    if 'open chrome' in command:
        openingRes(command)
        query = console.ReadLine("what should I search for?")
        try:
            webbrowser.open("google.com/search?q=" + query)
        except Exception as e:
            console.WriteLine(f"Error opening Chrome: {e}")
    elif 'open youtube' in command:
        openingRes(command)
        query = console.ReadLine("What do you want to watch?")
        try:
            webbrowser.open("youtube.com/results?search_query=" + query)
            console.WriteLine("Opened Youtube")
        except Exception as e:
            console.WriteLine(f"Error opening Youtube: {e}")
    elif 'open' in command:
        res = console.ReadLine("What do you want to open?")
        if res == "code":
            openingRes("Visual Studio Code")
            try:
                os.startfile("C:/Users/DELL/AppData/Local/Programs/Microsoft VS Code/Code.exe")
            except Exception as e:
                console.WriteLine(f"Error opening Visual Studio Code: {e}")
        elif res == "notepad":
            openingRes(command)
            try:
                os.startfile("notepad.exe")
            except Exception as e:
                console.WriteLine(f"Error opening Notepad: {e}")
        else:
            console.WriteLine(f"I don't know how to open {res}")
    elif 'send email' in command:
        to = console.ReadLine("To whom?")
        toEmail = console.ReadLine("Can you provide their email id?")
        subject = console.ReadLine("What is the subject?")
        content = console.ReadLine("What should I say?")
        attachment = console.ReadLine("Do you want to attach a file?")


        try:
            if attachment == 'yes':
                attachment = console.ReadLine("What is the path to the attachment?")
                console.WriteLine("Sending email...")
                sendEmail(toEmail, subject, content, attachment)
            else:
                console.WriteLine("Sending email...")
                sendEmail(toEmail, subject, content)
            console.WriteLine("Email sent successfully")
        except Exception as e:
            console.WriteLine(f"Error sending email: {e}")
    return command
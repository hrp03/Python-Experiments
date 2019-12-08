#greeting with time
import datetime
hour = datetime.datetime.now().hour
greetingMessage = ""
if hour < 12:
    greetingMessage = "Good morning hp"
elif hour < 17:
    greetingMessage = "Good evening hp"
else:
    greetingMessage = "Good night hp"
print(greetingMessage)
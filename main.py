from colorama import Fore,Style,init
from textblob import TextBlob

init(autoreset=True)

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity
conversation_history=[]

print(Fore.YELLOW+"welcome!! type 'exit' to end the conversation.\n")

while True:
    user_input=input(Fore.CYAN+ "YOU:").strip()
    if user_input=='exit':
     break
    
    sentiment=get_sentiment(user_input)
    if sentiment>0.1:
        response="i am glad to hear that!"
        color=Fore.GREEN
    elif sentiment<-0.1:
        response="i am sorry to hear that!"
        color=Fore.RED
    else:
        response="thanks for sharing"
        color=Fore.YELLOW
    print(color+f"Agent:{response}")
    conversation_history.append((user_input,sentiment,response))
print(Fore.YELLOW+ "\nconversation summary:")
for i, (text,polarity,response)in enumerate(conversation_history,1):
    print(f"{i},YOU:{text}")
    print(f"Sentiment:{polarity:.2f}")
    print(f"Agent:{response}\n")

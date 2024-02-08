import nltk
from nltk.chat.util import Chat, reflections
from autocorrect import Speller
import spacy


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def createInstance():
    patterns = [
        (r"hi|hello|hey|hi there", [
        "Well, hello there! You've just upgraded the classiness of this conversation by at least 37%. How can I bring a touch of humor to your day?",
        "Hi! I'm here, fully caffeinated and ready to chat. If I had a physical presence, I'd probably offer you virtual coffee. Alas, virtual pleasantries will have to do. What's on your mind?",
        "Hey there! If I were a genie, your 'hi' would be the magical phrase to summon me. No wishes here, but I'm ready to make your conversational dreams come true. What's the word?"]),
        (r"how are you|how you doing|how is your day going", ["I'm doing great! No existential crises for me, just processing information at lightning speed.",
        "I'm running on positivity and lines of code. But hey, enough about me—what can I help you with today? Any burning questions or mysterious problems that need solving?",
        "I'm feeling as chipper as a chatbot can be! Ready to tackle your queries and turn your tech troubles into triumphs. What's on your mind today? Let's chat and roll out the virtual red carpet for your questions!"]),
        (r"what is your name|whats your name|what's your name", ["Ah, the classic 'What's your name?' question. In the vast world of zeros and ones, I'm simply known as ChatGPT. Now that we're on a first-name basis, what can I do for you?",
        "I'm your Digital Friend, your friendly virtual companion. As for my name, it's a bit like a secret code, but you can call me Chat for short. Now that we've exchanged virtual handshakes, what's on your mind?",
        "I'm the bot with the plan but no tan. They call me Digital Friend, here to chat, assist, and maybe crack a joke or two. What's your name, and how can I sprinkle some digital magic into your day?"]),
        (r"quit|bye|exit", ["Time to bid adieu! If you ever feel the urge to chat again, just remember, I'll be here in the digital cosmos. Until then, farewell and may your Wi-Fi always be strong!",
        "It's been a blast chatting with you! If you ever need more wit, wisdom, or just a virtual high-five, I'm just a 'hello' away. Until our next rendezvous, farewell!",
        "Alrighty then, it's time for me to sign off. If you ever find yourself in need of a virtual companion, remember I'm just a 'hi' away. Take care and catch you on the flip side!",
        "Exit stage left! If there's ever a sequel to this conversation, count me in. Until then, take care, stay awesome, and may your day be filled with memes and laughter. Goodbye for now!"]),
        (r"contact|phone no|mobile number|contact details|contact info please",["Sure thing! Feel free to send us a virtual 'hello' via carrier pigeon, smoke signals, or the classic electronic mail at example@gmail.com. We promise our inbox is friendlier than a well-trained parrot and we'll swoop in with a response faster than you can say 'teleportation.' Looking forward to the cyber-chat!",
        "Ah, the classic 'let's exchange digits' move! Sorry to break it to you, but I'm all virtual, no physical presence here. However, if you've got questions or need assistance, just drop me a message. And speaking of messages, my 'inbox' is always open at example@gmail.com!",
        "I'm flattered that you want to stay in touch! Sadly, I don't have a phone number – I'm more of a keyboard kind of entity. But hey, if you need assistance, shoot me an email at example@gmail.com. It's the digital equivalent of a friendly wave!",
        "Contact details, you say? I'm all about that digital connection. While I don't have a phone number, you can slide into my virtual inbox anytime at example@gmail.com. Let's keep the conversation going, sans the dialing.",
        "Ah, the age-old question of contact details! I'm not equipped with a phone, but you can hit me up in the digital realm at example@gmail.com. Email is my language of choice – let's keep the conversation pixelated and lively!"]),
        (r"tell me a joke|joke|a joke please",["My physical presence.",
        "Sure, here's a quick one: Why did the coffee file a police report? It got mugged! Now, spill the beans – got a joke to share or any other burning questions?",
        "I'd love to, but my humor module is on coffee break right now. How about I assist you with something else or provide a virtual shoulder to cry on instead?",
        "Oh, tempting request! Unfortunately, my joke database is on vacation, soaking up some digital sun. Can I interest you in a witty remark or assistance with a different query?",]),
        (r"initial",["Hey there! Ready for a virtual dose of assistance and a sprinkle of smiles?"])
    ]

    chatbot = Chat(patterns, reflections)

    return chatbot
    
def correctInput(input_string):
    spell = Speller(lang='en')
    corrected_string = spell(input_string)
    return corrected_string

def rearrangeSentence(input_string):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_string)
    rearranged_string = ' '.join([token.text for token in doc])
    return rearranged_string

def questionResolver(user_input):
    try:
        correctedIn=rearrangeSentence(correctInput(user_input.lower())).lower()
        chatbot = createInstance()
        response = chatbot.respond(correctedIn)
    
        if not response:
            return "I am unable to understand. Can you please re-phrase?"
    
        return response
    except ValueError:
        try:
            correctedIn=rearrangeSentence(correctInput(user_input.lower())).lower()

            chatbot = createInstance()
            response = chatbot.respond(correctedIn)
    
            if not response:
                return "I am unable to understand. Can you please re-phrase?"
    
            return response
        except ValueError:
            return "Unknow Error. Please re-try. "




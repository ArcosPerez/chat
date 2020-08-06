from nltk.chat.util import Chat, reflections
mis_reflexions = {
"ir": "fui",
"hola": "hey"
}

pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal ¿En que te podemos ayudar?",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"fiebre|calentura| tos",
        [" usted debe cuidarse mas y te recomiendo que consuma unas pastillas "]
    ],
    [
        r"Cuales son|me puede recetar|recetar",
        [" paracetanol "]
    ],[
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
]
]
def chatear():
    print("Hola soy un tu hacistente personal") #mensaje por defecto
    chat = Chat(pares)
    chat.converse()
if __name__ == "__main__":
    chatear()
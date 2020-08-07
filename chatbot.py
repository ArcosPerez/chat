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
        ["Mi nombre es FED",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal ¿En que te puedo ayudar?",]
    ],
    [
        r"que (.*) se te ofrece|Que puedo hacer por ti ?",
        ["Nada gracias"," quisiera hacer una consulta"]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
     [
        r" indique su genero ?",
        ["Mujer | Hombre",]
    ],
     [
        r"Que sintomas tiene ?",
        ["Sensacion de fiebre" | "Tos" | "Dolor de cabeza" ]
    ],
     [
        r" Desde cuando presenta los sintomas ?", 
        ["Horas| Varios dias |Semanas|Meses"]
     ]
     [
        r"Tengo gripa ?",
        ["Le recomiento tomar alguna pastilla",]
    ],

    [
        r"fiebre|calentura| tos",
        [" usted debe cuidarse mas y te recomiendo que consumir pastillas "]
    ],
    [
        r"Cuales son|me puede recetar|recetar",
        [" paracetanol "]
    ],
      [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo", "Hasta pronto"]
]
]
def chatear():
    print("Hola soy un tu hacistente personal") #mensaje por defecto
    chat = Chat(pares)
    chat.converse()
if __name__ == "__main__":
    chatear()

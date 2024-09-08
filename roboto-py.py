import string, sys, random, codecs
#from
from math import sin, cos, pi, e
from datetime import datetime as dt
from tkinter import *

sys.stdout = codecs.getwriter ('utf_8') (sys.stdout.buffer, 'strict')

#_Function main_ #
def main ():
    try:
        #score user
        score = 0

        #scorog
        togue = [
            "A sailor went to sea. To see what he could see, And all he could see. Was sea, sea, sea.",
            "I like my Bunny. Bears like honey. Girls like cats. Cats like rats. Boys like dogs. Storks like frogs. Mice like cheese. Sparrows like peas.Owls like mice. I like rice. Birds like grain. Say it all again!",
            "I see a big black cat, Big black cat, big black cat. What a big black cat! What a cat! What a cat!",
            "Peter Piper picked. A peck of pickled peppers; A peck of pickled peppers. Peter Piper picked.",
            "Whether the weather be fine. Or whether the weather be not. Whether the weather be cold. Or whether the weather be not. We will walk together. Whatever the weather. Whether we like it or not.",
            "Betty Botta bought some butter, «But», she said, «this butter’s bitter, But a bit of better butter. Will make my batter better». So she bought a bit of butter. And it made her batter better.",
            "If you understand, say «understand». If you don’t understand, say «don’t understand». But if you understand and say «don’t understand». How do I understand that you understand? Understand!"
        ]

        #qut
        qoute = [
            "We do not remember days, we remember moments.",
            "Everyone has one's own path",
            "If you wish to be loved, love!",
            "Never say never",
            "World belongs to the patient..",
            "Everyone sees the world in one's own way",
            "You and I - belong.",
            "Everyone is the creator of one's own fate",
            "A day without laughter is a day wasted.",
            "spit what you think about me, about you, I do not think"
        ]

        #select command
        comm = str ( input ())
        #select index array
        index_arr = int ( input ())

        #random element array
        tog_en = random.choice (togue)
        qou_en = random.choice (togue)

        if ( comm == "togue" or index_arr == togue[0] or index_arr == togue[1] or index_arr == togue[2] or index_arr == togue[3] or index_arr == togue[5] or index_arr == togue[6] ):
            score += index_arr
            print (tog_en)
            print("\nВы Угадали индекс!\nВаши очки -", score)
        elif ( comm == "qoute" or index_arr == qoute[0] or index_arr == qoute[1] or index_arr == qoute[2] or index_arr == qoute[3] or index_arr == qoute[5] or index_arr == qoute[6] or index_arr == qoute[7] or index_arr == qoute[8] or index_arr == qoute[9]  ):
            score += index_arr
            print (qou_en)
            print("\nВы Угадали индекс!\nВаши очки -", score)
        elif comm == "сумма":
            num_1 = int ( input ())
            num_2 = int ( input ())

            res = num_1 + num_2

            print("Сумма чисел -", res)
        elif comm == "произведение":
            num_1 = int ( input ())
            num_2 = int ( input ())

            res = num_1 * num_2

            print("Произведение чисел -", res)
        elif comm == "деление":
            num_1 = int ( input ())
            num_2 = int ( input ())

            res = num_1 / num_2

            print("Деление чисел -", res)
        elif comm == "вычитание":
            num_1 = fint ( input ())
            num_2 = int ( input ())

            res = num_1 - num_2

            print("Вычитание чисел -", res)
        elif comm == "степень":
            num_1 = int ( input ())
            num_2 = int ( input ())

            res = num_1 ** num_2

            print("Результат степени чисел -", res)
    except SyntaxError:
        print ("Syntax error")
    # 100%
    finally:
        print ("\n\n\n\n\n\n\n\n\nDebug works")



return main

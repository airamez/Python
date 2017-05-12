"""
Read a language code from the list below and print "Hello world" using the selected language
    en = English = "Hello world"
    pt = Portuguese = "Olá Mundo"
    sp = Spanish = "Holla Mundo"
    ch = Chinese = "你好，世界"
    ge = Germany = "Hallo Welt"
"""
ENGLISH = "Hello world"
PORTUGUESE = "Olá Mundo"
SPANISH = "Holla Mundo"
CHINESE = "你好，世界"
GERMANY = "Hallo Welt"

language_code = input("Language Code = ")
if language_code == "en":
    print(ENGLISH)
elif language_code == "pt":
    print(PORTUGUESE)
elif language_code == "sp":
    print(SPANISH)
elif language_code == "ch":
    print(CHINESE)
elif language_code == "ge":
    print(GERMANY)
else:
    print("Wrong language code:", language_code)

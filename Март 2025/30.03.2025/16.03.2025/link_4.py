s = "Шёл осенний дождь.\
    Поздним вечером в июле Чупакабра прогуливалась под зонтом.\
    И зашла она в чебуречную! \
    решила купить чебурек, съела и отравилась.\
    и восстали Чупакабры!\
    И тут я проснулся?!\
    "
start_sentense = True 
new_story = ''

for ch in s:
    if start_sentense == True and ch.isalpha():
        new_story  += ch.upper()
        start_sentense = False
    else:
        new_story += ch

    if ch in (" .!?"):
        start_sentense = True 

print(new_story)
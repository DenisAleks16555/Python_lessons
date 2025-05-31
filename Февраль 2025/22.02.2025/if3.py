# "red" "yellow" "green"
trafic_light = "red"
#если жёлтый
#trafic_light = "yellow"

print("Смотрим на сфетофор")

if trafic_light == "red":
    print("Горит красный сигнал") 
    trafic_light = "yellow"

elif trafic_light == "yellow":
    print("Горит жёлтый сигнал")

elif trafic_light == "green":
    print("Горит зелёный сигнал")

else:
    print("Сфетофор сломан")
    print("Ориентируемся на знаки")

    
print("Делаем выводы")

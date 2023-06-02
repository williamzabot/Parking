from Parking import Parking
from Registration import Registration
from datetime import datetime
from datetime import date
import json

parking = Parking()
vacancies = parking.vacancies

def menu():
    while True:
        choice = str(input("""=== Estacionamento do Tio Ivo ===
1- Estacionar
2- Saída
3- Resumo de ocupação
Escolha: """))
        if choice == "1":
            choiceOne()
        elif choice == "2":
            choiceTwo()
        elif choice == "3":
            choiceThree()
        else:
            break


def doRegistration(plate, box):
    vacancies[box].append(Registration(plate, getDateAndTime()))
    print(f"Seu carro foi estacionado no {box}")

def choiceOne():
    inputtedPlate = str(input("Insira sua placa: ")).strip().upper()
    for box, registrations in vacancies.items():
        if len(registrations) == 0:
            doRegistration(inputtedPlate, box)
            break
        elif len(registrations) > 0:
            lastElement = registrations[-1]
            if lastElement.plate == inputtedPlate and lastElement.active:
                print(f"Este veículo: {inputtedPlate} está estacionado no {box}")
                break
            elif not lastElement.active:
                doRegistration(inputtedPlate, box)
                break


def choiceTwo():
    inputtedPlate = str(input("Insira sua placa: ")).strip().upper()
    exitPerformed = False
    for box, registrations in vacancies.items():
        if len(registrations) > 0:
            lastElement = registrations[-1]
            if lastElement.plate == inputtedPlate and lastElement.active:
                exit = getDateAndTime()
                print(f"Este veículo: {inputtedPlate} está estacionado no {box}. Saída: {exit}")
                lastElement.setExitTime(exit)
                exitPerformed = True
                break
    if not exitPerformed:
        print("Placa não encontrada")


def choiceThree():
    for box, registrations in vacancies.items():
        print(box)
        for registration in registrations:
            print(str(registration))
    choice = str(input("""Você deseja armazenar essas informações num arquivo?
    1 - Armazene num arquivo txt
    2 - Armazene num arquivo json
    Qualquer tecla - Não armazenar
    Escolha: """))
    if choice == "1":
        saveFile("txt")
    elif choice == "2":
        saveFile("json")


def getDateAndTime():
    currentDate = date.today().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M')
    return f"{currentDate} {time}"

def saveFile(extension):
    fileName = f"parking.{extension}"
    dict = convertDictionary()
    with open(fileName, 'w') as file:
        json.dump(dict, file, indent=4, separators=(", ", ": "))
    print("Arquivo criado com sucesso!")

def convertDictionary():
    dict = {}
    for i in range(1, 41):
        dict[f"Box {str(i)}"] = []
    for box, registrations in vacancies.items():
        registrationConverted = []
        for registration in registrations:
            registrationConverted.append(registration.toDict())
        dict[box].append(registrationConverted)
    return dict


menu()

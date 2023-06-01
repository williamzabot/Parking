"""Ao finalizar o programa, pergunte ao usuário se ele quer armazenar os dados em um arquivo TXT ou JSON.
Ao iniciar o programa, verifique se o arquivo TXT e JSON já existem. Caso exista, pergunte ao usuário qual arquivo ele quer utilizar.
"""

from Parking import Parking
from Registration import Registration
from datetime import datetime
from datetime import date

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

def choiceOne():
    inputtedPlate = str(input("Insira sua placa: ")).strip()
    for box, registrations in vacancies.items():
        if len(registrations) == 0:
            print(f"Seu carro foi estacionado no {box}")
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
    inputtedPlate = str(input("Insira sua placa: ")).strip()
    for box, registrations in vacancies.items():
        if len(registrations) > 0:
            lastElement = registrations[-1]
            if lastElement.plate == inputtedPlate and lastElement.active:
                exit = getDateAndTime()
                print(f"Este veículo: {inputtedPlate} está estacionado no {box}. Saída: {exit}")
                lastElement.setExitTime(exit)
                break
            else:
                print("Placa não encontrada")
                break


def choiceThree():
    for box, registrations in vacancies.items():
        print(box)
        for registration in registrations:
            print(str(registration))


def getDateAndTime():
    currentDate = date.today().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%H:%M')
    return f"{currentDate} {time}"

menu()

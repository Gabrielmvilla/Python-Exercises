'''

##### Registry for Contacts (saves in file) #####

-*- coding: utf-8 -*-
  
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This program allows to save a contact list in a json file and manipulate
the data saved. The contacts have name, surname, telephone and birthday,
but other fields could be added by the manipulation of this program.
Besides, this code could be used as a "template" for storing other types
of information that requires saving for further access, such as
information about products, services, etc.

'''

from json import dumps, loads
from os import remove, rename

def write_file(name_file: str, object_py: str, mode: str = 'a') -> None:
    if str(type(object_py)) == "<class '__main__.Register'>": #Write a object in a json file:
        json_format = dumps(object_py.__dict__)
        with open(name_file, mode) as arq:
            arq.write(json_format + '\n')
    elif str(type(object_py)) == "<class 'dict'>": #Write a dictionary in a json file:
        json_format = dumps(object_py)
        with open(name_file, mode) as arq:
            arq.write(json_format + '\n')
    else:
        print('This type of data requires other kind of treatment.\nNO DATA WAS SAVED.')
        
def read_file(name_file: str, name_ident: str = 'Void') -> bool:
    with open(name_file, 'r') as arq:
        existence_test: bool = False
        while (line_file := arq.readline()):
            json_to_python = loads(line_file)
            if name_ident == 'all':
                print(f'Name: {json_to_python["name"]} {json_to_python["surname"]} - Telephone: {json_to_python["telephone"]} - Birthday: {json_to_python["birthday"][0]}/{json_to_python["birthday"][1]}/{json_to_python["birthday"][2]}\n')
                existence_test = True
            elif json_to_python['name'].lower() == name_ident.lower():
                print(f'Name: {json_to_python["name"]}\nSurname: {json_to_python["surname"]}\nTelephone: {json_to_python["telephone"]}\nBirthday: {json_to_python["birthday"][0]}/{json_to_python["birthday"][1]}/{json_to_python["birthday"][2]}\n')
                existence_test = True
        if existence_test == False:
            print('Non-existent.')
    return existence_test

def organize(name_file: str, mode: str = 'name') -> None: #THIS SAVES ALL ENTRIES IN A LIST, COULD NOT WORK FOR BIG FILES!
    if mode == 'name':
        all_entries: list = []
        with open(name_file, 'r') as arq:
            lines_registers: int = len(arq.readlines())
            arq.seek(0)
            for num_line in range(0, lines_registers):
                while (line_file := arq.readline()):
                    all_entries.append(loads(line_file))
        all_entries.sort(key = lambda x: x["name"]) #command to organize
                    #Save organized data:
        #The first line must rewrite the existent file:
        organized_reg = all_entries[0] 
        write_file(name_file, organized_reg, 'w')
        #From the second, just add to the file:
        for num_reg in range(1, len(all_entries)):
            organized_reg = all_entries[num_reg]
            write_file(name_file, organized_reg, 'a')
                
    elif mode == 'surname': #Same thing, but with the surname:
        all_entries: list = []
        with open(name_file, 'r') as arq:
            lines_registers: int = len(arq.readlines())
            arq.seek(0)
            for num_line in range(0, lines_registers-1):
                while (line_file := arq.readline()):
                    all_entries.append(loads(line_file))
        all_entries.sort(key = lambda x: x['surname'])
        organized_reg = all_entries[0] 
        write_file(name_file, organized_reg, 'w')
        for num_reg in range(1, len(all_entries)-1):
            organized_reg = all_entries[num_reg]
            write_file(name_file, organized_reg, 'a') 

def delete_register(name_file: str, name_del: str, surname_del: str) -> None:
    with open(name_file, 'r') as arq:
        while (line_file := arq.readline()):
            json_to_python = loads(line_file)
            if json_to_python['name'] != name_del or json_to_python['surname'] != surname_del: # If's not to delete the register/line, copy to a new file. 
                write_file('temp_file.json', json_to_python)
    remove(name_file) #Delete the old file.
    rename('temp_file.json', name_file) # Rename the new one.
        
def edit_register(name_file: str, name_mod: str, surname_mod: str, field: str) -> None:
    with open(name_file, 'r') as arq:
        test_existence_edit: bool = False
        while (line_file := arq.readline()):
            json_to_python = loads(line_file)
            if json_to_python['name'] == name_mod and json_to_python['surname'] == surname_mod:
                if field.lower() == 'name':
                    json_to_python['name'] = str(input('Insert a new name for the register: '))
                elif field.lower() == 'surname':
                    json_to_python['surname'] = str(input('Insert a new surname for the register: '))
                elif field.lower() == 'telephone':
                    json_to_python['telephone'] = int(input('Insert a new telephone number for the register: '))
                elif field.lower() == 'birthday':
                    json_to_python['birthday'][0] = int(input('Insert a new day number for the register (1 to 31): '))
                    json_to_python['birthday'][1] = int(input('Insert a new month number for the register (1 to 12): '))
                    json_to_python['birthday'][2] = int(input('Insert a new year number for the register  (1900 to 2023): '))
                else:
                    print('Invalid.')
                test_existence_edit = True
            write_file('temp_file.json', json_to_python) # The jason convertion is done in the function.
        if test_existence_edit == False:
            print('Non-existent.')
    remove(name_file)
    rename('temp_file.json', name_file)    
    
def add_people() -> None: #Create a fake registry for tests. I made it all up, nothing real:
    person1 = Register('Zappe', 'Silva', '987654321', (13, 6, 95))
    person2 = Register('Pam', 'Das Flores', '987654321', (7, 9, 97))
    person3 = Register('Kia', 'Leee', '987654321', (10, 2, 2000))
    person4 = Register('Ross', 'Last', '987654321', (10, 2, 90))
    person5 = Register('Michelle', 'Ma Belle', '987654321', (30, 5, 94))
    person6 = Register('Michelle', 'Double', '987654321', (31, 6, 95))
    person7 = Register('Astrid', 'Ironmade', '777777777', (12, 12, 1912))
    organize('registry.json', mode = 'name')
    

class Register:
    def __init__(self: object, name: str, surname: str, telephone: int, birthday: tuple):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.birthday = birthday
        write_file('registry.json', self)

if __name__ == '__main__':
    print('#### Registry for Contacts ###')
    while True:
        operation: int = input('\n\nInsert the number for the desired operation:\n1 - See one register\n2 - Add new entry\n3 - Edit regiter\n4 - Delete register\n5 - Organize registry\n6 - See all registers\n9 - Create a fake registry for tests\n0 - Exit\n-> ')
        
        try:
            operation = int(operation)
        except:
            print('Use only numbers.')
        
        if operation == 0: #Exit
            break
        elif operation == 1: #See one register
            name_person = str(input('Insert the name of the person to see the data: '))
            print('\n')
            read_file('registry.json', name_ident = name_person)
            
        elif operation == 2: #New entry
            try:
                name_person = str(input('Insert a name for the register: '))
                surname_person = str(input('Insert a surname: '))
                telephone_person = int(input('Insert a telephone number: '))
                day_person = int(input('Insert a day for the birthday (1 to 31): '))
                month_person = int(input('Insert a month for the birthday (1 to 12): '))
                year_person = int(input('Insert a year for the birthday (1900 to 2023): '))
                Register(name_person, surname_person, telephone_person, (day_person, month_person, year_person))
                print('Register added.\n')
            except:
                print('Invalid values.')
            
        elif operation == 3: #Edit entry
            name_person = str(input('Insert the name of the person to edit: '))
            test_existence3 = read_file('registry.json', name_ident = name_person)
            if test_existence3 == True:
                surname_person = str(input('Insert the surname of the person to edit: '))
                campo_edicao = str(input('Insert the field of the register to edit or "0" to cancel the operation: '))
                if campo_edicao != '0':
                    edit_register('registry.json', name_person, surname_person, campo_edicao)
            
        elif operation == 4: #Delete entry
            name_person = str(input('Insert the name of the person to delete: '))
            test_existence4 = read_file('registry.json', name_ident = name_person)
            if test_existence4 == True:
                surname_person = str(input('Insert the surname of the person to delete or "0" to cancel: '))
                if surname_person != '0':
                    delete_register('registry.json', name_person, surname_person)
                    print('Register deleted.')
            
        elif operation == 5: #Organize registry
            mode_org = int(input('Organize by:\n1 - Name\n2 - Surname\n-> '))
            if mode_org == 1:
                organize('registry.json', mode = 'name')
            elif mode_org == 2:
                organize('registry.json', mode = 'surname')
            else:
                print('Invalid option.')
                           
        elif operation == 6: #See all registers
            print('\n')
            read_file('registry.json', name_ident = 'all')
            
        elif operation == 9: #Create fake registry for tests
            add_people()
        
        else:
            print('Invalid option.')

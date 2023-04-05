from classes import UserName, PhoneNumber, Record, ContactsBook


PHONE_NUMBER =  ContactsBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as ex:
            return ex
        except KeyError as ex:
            return ex
        except ValueError as ex:
            return ex
        except TypeError as ex:
            return ex
    return inner

@input_error
def hello(*args):
    return "How can I help you?"

def help(*args):
    return"""Tthis is an instruction"""

@input_error
def add_phone(*args):
    lst_param = args[0].split()
    name = UserName(lst_param[0])
    phone = PhoneNumber(lst_param[1])
    for contact, rec in PHONE_NUMBER.items(): 
        if name.value == contact:
            rec.add_number(phone)
            return f'{rec.name.value.capitalize()}: {rec.numbers}'
    else:
        record = Record(name,phone) 
        PHONE_NUMBER.add_contact(record)

@input_error
def change_phone(*args):
    lst_param = args[0].split()
    contact = UserName(lst_param[0])
    old_number = PhoneNumber(lst_param[1])
    new_number = PhoneNumber(lst_param[2])
    for k, v in PHONE_NUMBER.items():
        if k == contact.value:
            v.change_number(old_number,new_number)
    return f'{contact.value.capitalize()}: {new_number.value}'

@input_error
def show_phone(*args):
    contact = args[0]
    for name, record  in PHONE_NUMBER.items():
        if name == contact:
            return record.numbers
    return 'Number not found'

def show_all(*args):
    return '\n'.join([str(k) + ': ' + str(v) for k,v in PHONE_NUMBER.items()])

@input_error
def exit(*args):
    return 'Bay'

COMMANDS = {help: 'help',
            add_phone: 'add',
            show_phone: "show",
            change_phone: "change",
            show_all: "all",
            exit: 'exit'}

def command_handler(text: str):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            
            return command, text.replace(kword, '').strip()
    return None, None


def main():
    while True:
        user_input = input('>>>')

        command, data = command_handler(user_input)
        print(command(data))
        if command == exit:
            break
    

if __name__=="__main__":
    main()
   
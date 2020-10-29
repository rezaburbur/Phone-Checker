
#!/usr/local/bin/python3
# Phone_Number v1.0.1
# coded by: hack4lx
# 👊 ʍ4ղíƒҽՏԵ0 ϲվҍҽɾ ՏҽϲմɾíԵվ Եҽɑʍ™💪
# Thank You :  @rainboy1 | @KindKhers4lx | @Mohsening | @Vampire4lx | @erfan4lx | @HatBLACK4LX
from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPhoneContact
from telethon import functions, types

def check(phone_number, usr):
    try:
        contact = InputPhoneContact(client_id = 0, phone = phone_number, first_name="__test__", last_name="__last_test__")
        contacts = client(functions.contacts.ImportContactsRequest([contact]))
        username = contacts.to_dict()['users'][0]['username']
        return username
        dell = client(functions.contacts.DeleteContactsRequest(id=[username]))
    except:
        res = "__err__"
        return res

def list_checker():
    list_file = input("لیست شماره ها: ")
    usr = input("یوزرنیم هدف: ")
    list = open(list_file, 'r').read().splitlines()
    for num in list:
        try:
            ress = check(num, usr)
            if ress == '__err__':
                print ("Number: {} <{}>".format(num, "ERROR!"))
            elif ress.lower() == usr.lower():
                f = open("hit.txt", "a")
                f.write(ress+":"+num)
                f.close()
                print ("Number: {} <{}>".format(num, "OK:)"))
                break
            else:
                print ("Null")
        except:
            print ("Null")

if __name__ == '__main__':
    phone = '+19028120412'
    client = TelegramClient(phone, 1890509, '4c7e4382ca697761d7e9056a56498f74')
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('کد را درج کنید: '))
    list_checker()

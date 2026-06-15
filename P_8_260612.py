# def greeting(user_name):
#     print(f"Hello,{user_name.title()}")
# greeting("Sarah")

# def make_shirt(size,font):
#     print(f"\n this shirt size is {size},font size is {font}")
# make_shirt(43,'汉字')

# def get_formatted_name(first_name,last_name,middle_name=''):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title();
# musician    = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name,last_name,middle_name=''):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('john','henry','.')
# print(musician)

# def country_info(city_name,conuntry_name):
#     print(f"{city_name} {conuntry_name}")
# country_info('Beijing','China')

# def make_album(singer,album,count=None):
#     singer_album = {}
#     singer_album['singer'] = singer
#     singer_album['album'] = album
#     if count:
#         singer_album['count'] = count
#     return singer_album
#
# while True:
#     singer = input('Please input singer name\t')
#     if singer == 'q':
#         break
#     album = input('Please inpiut album name\t')
#     if album == 'q':
#         break
#     count = input('Please input album count\t')
#     singer_album = make_album(singer,album,count)
#     print(singer_album)

# def send_messages(send,receive):
#     while send:
#         cc = send.pop()
#         print(f"Now start to send {cc} to new container...")
#         receive.append(cc);
#         print(f"received.")
#
# def sent_message(received):
#         print(received)
#
# sed = ['A','B','C']
# rec = []
# send_messages(sed[:],rec)
# sent_message(rec)
# sent_message(sed)

# def car(vendor,type,**cars):
#     cars['vendor'] = vendor
#     cars['type'] = type
#     return cars
#
# carinfo = car('HQ','81',color='black',tow_package=True,hight=34)
# print(carinfo)

import pizza as P1
P1.make_pizza(23,'A','B','C')
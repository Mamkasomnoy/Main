dog = '@'
com = '.com'
ru = '.ru'
net = '.net'
the_address_is_correct = 0
sender_one = "university.help@gmail.com"
def send_email(message, recipient, sender="university.help@gmail.com"):
    while 1 > 0:
        if (str(dog) in str(recipient) and str(com) in str(recipient) or str(dog) in str(recipient) and str(ru) in str(recipient) or str(dog) in str(recipient) and str(net) in str(recipient)) and (str(dog) in str(sender) and str(com) in str(sender) or str(dog) in str(sender) and str(ru) in str(sender) or str(dog) in str(sender) and str(net) in str(sender)):
            if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
                break
            elif sender_one == sender:
                print('Письмо успешно отправлено с адреса:', sender, 'на адрес:', recipient)
                break
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса:', sender, 'на адрес:', recipient)
                break
        else:
            print("Невозможно отправить письмо с адреса:", sender, " на адрес:", recipient)
            break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
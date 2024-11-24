dog = '@'
com = '.com'
ru = '.ru'
net = '.net'
sender_one = "university.help@gmail.com"
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    while 1 > 0:
        str(sender)
        str(recipient)
        if (
                (str(dog) in recipient and str(com) in recipient or str(dog) in recipient and str(ru) in recipient or str(dog) in recipient and str(net) in recipient)
                and (str(dog) in sender and str(com) in sender or str(dog) in sender and str(ru) in sender or str(dog) in sender and str(net) in sender)
                and (recipient.endswith(com) or recipient.endswith(ru) or recipient.endswith(net)) and (sender.endswith(com) or sender.endswith(ru) or sender.endswith(net))
            ):

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

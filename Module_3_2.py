def send_email(a="message",*, b="sender", c="recipient"):
    print(a, b, "на", c)

sender = "university.help@gmail.com"
recipient = "afnnebo@gmail.com"
message = "Письмо успешно отправлено с адреса"
send_email(a=message, b=sender, c=recipient)


def send_email(a="message", b="sender", c="recipient"):
    print(a, b, "на", b)

sender = "university.help@gmail.com"
recipient = "afnnebo@gmail.com"
message = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса"
send_email(a=message, b=sender, c=recipient)


def send_email(a="message", b="sender",*, c="recipient"):
    print(a, b, "на", b)

sender = "university.help@gmail.com"
recipient = "afnnebo@gmail.com"
message = "Невозможно отправить письмо с адреса"
send_email(a=message, b=sender, c=recipient)


def send_email(a="message",*, b="sender", c="recipient"):
    print(a, c, "на", c)

sender = "university.help@gmail.com"
recipient = "afnnebo@gmail.com"
message = "Нельзя отправить письмо самому себе!"
send_email(a=message, b=sender, c=recipient)




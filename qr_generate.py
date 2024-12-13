from win10toast import ToastNotifier
import qrcode
from time import sleep

class Programm:
    def __init__(self):
        self.remain = 10
        self.generate_code()
    def generate_code(self):
        try:
            print("Привет,это генератор qr кодов всего за 1 шаг!")
            self.data =input("шаг №1. Напиши сюда текст или ссылку,который будет содержать qr код? >>>>")
            if self.data =="":
                print("Содеражение qr кода не может быть пустым")
                return
            else:
                print("Перед генерацией спрошу 1 вопрос.Хочешь ли ты максимально кастомизировать qr код вплоть до мелочей? ")
                print("1)Да,хочу")
                print("2)Нет,не хочу")
                self.user_choice =int(input("Так что ты выбрал? >>>>"))
                if self.user_choice ==1:
                    print("Отлично!Давай кастомизировать")
                    self.user_version =int(input("Чему будет равно поле qr кода (от 1 до 40)"))
                    if self.user_version <1 or self.user_version >40:
                        print("Вы ввели недопустимые значения")
                        return
                    else:
                        self.user_box_size =int(input("Чему будет равно количевство пикселей в qr коде"))
                        if self.user_box_size <=0:
                            print("Вы ввели недопустимые значения")
                            return
                        else:
                            self.user_border_size = int(input("Чему будет равна толщина границы  в qr коде"))
                            if self.user_border_size <= 0:
                                print("Вы ввели недопустимые значения")
                                return
                            else:
                                for i in range(10):
                                    print(f"До конца генерации осталось: {self.remain} секунд")
                                    sleep(0.7)
                                    self.remain -= 1
                                    if self.remain <= 0:
                                        self.file_name = "my_qr_code.png"
                                        self.qr_1 = qrcode.make(self.data,version=self.user_version,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size =self.user_box_size,border =self.user_border_size)
                                        self.qr_1.save(self.file_name)
                                        ToastNotifier().show_toast("Готово",f"Ваш qr код сгенерирован в файле {self.file_name}.")
                                        return
                elif self.user_choice ==2:
                    for i in range(10):
                        print(f"До конца генерации осталось: {self.remain} секунд")
                        sleep(0.7)
                        self.remain -=1
                        if self.remain <=0:
                            self.file_name = "my_qr_code.png"
                            self.qr_2 = qrcode.make(self.data)
                            self.qr_2.save(self.file_name)
                            ToastNotifier().show_toast("Готово",f"Ваш qr код сгенерирован в файле {self.file_name}.")
                            return
        except ValueError:
            print("Вы ввели недопустимые значения")
if __name__ =="__main__":
    Programm()

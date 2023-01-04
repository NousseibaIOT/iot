# Create your models here.
from django.core.mail import send_mail
from django.db import models
from pynput.keyboard import Key, Controller

class Dht(models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return "temperature= "+str(self.temp)


# Create your models here
    def save(self, *args, **kwargs ):
        if self.temp < 2:
        #envoie sur wtp
            import pywhatkit as kit
            kit.sendwhatmsg_instantly(f'+212696866998', "attention temperature severe! la temperature est a " + str(self.temp), 15, True)
            keyboard = Controller()
            keyboard.press(Key.enter)

         #envoie du msg sur telegram
            import telepot
            token = '5701417127:AAEccut9jXyfsuqrqPsfVk2Co71RavyyBg0'
            rece_id = 5944713240
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'Attention!')
            print(bot.sendMessage(rece_id, 'temperature severe .'))
         #envoie du mail
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine',
                'nousseiba.gaouche@ump.ac.ma',
                ['nousseibagaouche3@gmail.com'],
                fail_silently=False)

        if self.temp > 12:
        #envoie sur wtp
            import pywhatkit as kit
            kit.sendwhatmsg_instantly(f'+212696866998', "attention temperature critique! la temperature est a " + str(self.temp), 15, True)
            keyboard = Controller()
            keyboard.press(Key.enter)

         #envoie du msg sur telegram
            import telepot
            token = '5701417127:AAEccut9jXyfsuqrqPsfVk2Co71RavyyBg0'
            rece_id = 5944713240
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'Attention!')
            print(bot.sendMessage(rece_id, 'temperature critique .'))
         #envoie du mail
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine',
                'nousseiba.gaouche@ump.ac.ma',
                ['nousseibagaouche3@gmail.com'],
                fail_silently=False)
        return super().save(*args, **kwargs)







    # Create your models here




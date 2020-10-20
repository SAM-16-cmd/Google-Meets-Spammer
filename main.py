from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from cryptography.fernet import Fernet
import selenium.common.exceptions as driver_except
from time import sleep
from os import mkdir, environ, listdir
from os.path import exists
import smtplib
from art import text2art
from platform import system

'''Version: 1.0.3.1'''
username = environ['USERNAME']
opperSystem = system()
nonWindows = False

if opperSystem != "Windows":
    nonWindows = True


class generics:
    def __init__(self):
        self.permission_er = False
        self.exist_er = False
        self.accounts = {generic_email:generic_pass}

    def secrets_check(self):
        if not nonWindows:
            if not exists(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS') and not exists(f'C:\\Users\\{username}\\Documents\\GMS'):
                print('made it')
                try:
                    mkdir(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS')
                except PermissionError:
                    self.permission_er = True
                    self.return_home(['Google Meet Spammer Encountered a Permission Error', 'Restart the Program in Administrator Mode'])
                except FileNotFoundError:
                    self.permission_er = True
                    try:
                        mkdir(f'C:\\Users\\{username}\\Documents\\GMS')
                    except FileNotFoundError:
                        self.return_home('The directory ' + f'C:\\Users\\{username}\\OneDrive\\Documents' + ' Could not be found.')

            if not exists(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets') and not exists(f'C:\\Users\\{username}\\Documents\\GMS\\secrets'):
                try:
                    mkdir(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets')
                except PermissionError:
                    self.permission_er = True
                    self.return_home('Google Meet Spammer Encountered a Permission Error. Run the program again in an administrator environment.')
                except FileNotFoundError:
                    self.permission_er = True
                    try:
                        mkdir(f'C:\\Users\\{username}\\Documents\\GMS\\secrets')
                    except FileNotFoundError:
                        self.return_home('The directory ' + f'C:\\Users\\{username}\\OneDrive\\Documents' + ' Could not be found.')
        else:
            if not exists('GMS'):
                try:
                    mkdir('GMS')
                except PermissionError:
                    self.return_home(['Google Meet Spammer encountered a permission error when trying to create the GMS folder', 'To fix this restart the program in administrator mode'])
            if not exists('GMS/secrets'):
                try:
                    mkdir('GMS/secrets')
                except PermissionError:
                    self.return_home(['Google Meet Spammer encountered a permission error when trying to create the secrets folder', 'To fix this restart the program in administrator mode'])

    def grab_secrets(self):
        if nonWindows:
            for x in range(len(listdir('GMS/secrets'))):
                if exists(f'GMS/secrets/user-{x}.sacc'):
                    with open(f'GMS/secrets/user-{x}.sacc', 'rb')as get_sec:
                        contents = get_sec.readlines()
                        get_sec.close()
                    dec = Fernet(contents[2])
                    _password = dec.decrypt(contents[1])
                    _gmail = dec.decrypt(contents[0])
                    gmail = _gmail.decode()
                    self.accounts[gmail] = _password
        else:
            try:
                for x in range(len(listdir(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets'))):
                    if exists(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets\\user-{x}.sacc'):
                        with open(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets\\user-{x}.sacc', 'rb')as get_sec:
                            contents = get_sec.readlines()
                            get_sec.close()
                        dec = Fernet(contents[2])
                        _password = dec.decrypt(contents[1])
                        _gmail = dec.decrypt(contents[0])
                        gmail = _gmail.decode()
                        self.accounts[gmail] = _password
            except FileNotFoundError:
                try:
                    for x in range(len(listdir(f'C:\\Users\\{username}\\Documents\\GMS\\secrets'))):
                        if exists(f'C:\\Users\\{username}\\Documents\\GMS\\secrets\\user-{x}.sacc'):
                            with open(f'C:\\Users\\{username}\\Documents\\GMS\\secrets\\user-{x}.sacc', 'rb')as get_sec:
                                contents = get_sec.readlines()
                                get_sec.close()
                            dec = Fernet(contents[2])
                            _password = dec.decrypt(contents[1])
                            _gmail = dec.decrypt(contents[0])
                            gmail = _gmail.decode()
                            self.accounts[gmail] = _password
                except FileNotFoundError:
                    self.return_home('The documents folder could not be found when trying to grab account data')

    def add_secrets(self, gmail, password):
        ngmail = gmail.encode()
        npassword = password.encode()
        key = Fernet.generate_key()
        safe = Fernet(key)
        _gmail = safe.encrypt(ngmail)
        _password = safe.encrypt(npassword)

        accounts = 0
        if nonWindows:
            for x in listdir('GMS/secrets'):
                accounts += 1
            with open(f'GMS/secrets/user-{accounts}.sacc', 'wb')as user:
                user.writelines([_gmail, b'\n', _password, b'\n', key])
                user.close()
        else:
            try:
                for x in listdir(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets'):
                    accounts += 1

                with open(f'C:\\Users\\{username}\\OneDrive\\Documents\\GMS\\secrets\\user-{accounts}.sacc', 'wb')as user:
                    user.writelines([_gmail, b'\n', _password, b'\n', key])
                    user.close()
            except FileNotFoundError:
                try:
                    for x in listdir(f'C:\\Users\\{username}\\Documents\\GMS\\secrets'):
                        accounts += 1

                    with open(f'C:\\Users\\{username}\\Documents\\GMS\\secrets\\user-{accounts}.sacc', 'wb')as user:
                        user.writelines([_gmail, b'\n', _password, b'\n', key])
                        user.close()
                except FileNotFoundError:
                    self.return_home('The documents folder could be found for adding account data')

    def gmail_valid(self, gmail, password):
        serv = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        try:
            serv.login(gmail, password)
        except:
            return False

        return True

    def add_gmail(self):
        for x in range(12):
            print('\n')

        ngmail = input('Enter a gmail; preferably a spam one:\n')
        gmail = ngmail.replace('@gmail.com','') + '@gmail.com'
        password = input('Enter the password to the gmail you entered:\n')
        if not self.gmail_valid(gmail, password):
            self.return_home('Your gmail was not added due to the entered gmail having an invalid password, or identifier. Check your connection to the internet.')
        else:
            self.add_secrets(gmail, password)
            self.grab_secrets()
            self.return_home('Gmail Added')

    def main_page(self):
        print(text2art('GOOGLE Meet Spammer v1'))
        for x in range(2):
            print('\n')

        print('Options:\n-(a)Spam\n-(b)Add a Gmail')
        for x in range(2):
            print('\n')

        print('Current Available Gmails:')
        for x in gen.accounts:
            print(f'+{x}')

        selection = input('\nEnter an Option:\n')

        if selection == 'a' or selection == 'A':
            spam = spammer()
            spam.startup()
        elif selection == 'b' or selection == 'B':
            self.add_gmail()
        else:
            self.return_home(['That is not an option.', 'Try entering \'a\' or \'b\''])

    def return_home(self, status):
        if type(status) == list:
            for x in status:
                print(x)
        else:
            print(status)
        input('Press Enter to Return Home')
        for x in range(20):
            print('\n')

        self.main_page()

    def logged_account_check(self, grabbed_accounts):
        for x in grabbed_accounts.split(','):
            added = False
            for y in self.accounts:
                if x == y:
                    added = True
            if not added:
                return False

        return True


class spammer:
    def __init__(self):
        self.gens = generics()
        self.gens.grab_secrets()
        self.accounts = None
        self.spammessage = None
        self.how_many = None
        self.meet_code = None
        self.meet_link = None
        self.corn_boy = False

    def startup(self):
        for x in range(20):
            print('\n')

        for x in self.gens.accounts:
            print('->' + x)

        naccounts = input('Enter the gmails of the accounts you want to use to spam; sepperate the gmails using commas, do not include spaces:\n')
        accounts = ''
        for x in naccounts.split(','):
            accounts = accounts + x.replace('@gmail.com', '').replace(' ', '') + '@gmail.com' + ','
        accounts = accounts[:-1]
        print(accounts)
        if not self.gens.logged_account_check(accounts):
            print('You entered a gmail that has not yet been entered, go back to the menu to enter it.')
            input()
            self.gens.main_page()
        else:
            if accounts.count('@gmail.com') == 1 and ',' not in accounts:
                self.accounts = [accounts]
            elif accounts.count('@gmail.com') > 1 and ',' not in accounts:
                print('You entered more than one gmail and did not put commas.')
                input()
                self.gens.main_page()
            else:
                self.accounts = accounts.split(',')

            self.loading()

    def loading(self):
        for x in range(20):
            print('\n')
        self.spammessage = input('Enter the message you want the bots to spam:\n')
        self.how_many = input('Enter how many times you want the bots to spam it:\n')
        try:
            int(self.how_many)
        except TypeError:
            print('You did not eneter an integer value for the amount of times to spam')
            input()
            self.gens.main_page()

        self.meet_link = input('Enter the link to you google meet:\n')
        self.meet_code = self.meet_link.split('/')[2]
        self.spam_attack()

    def spam_attack(self):
        for x in self.accounts:
            chrome_opt = Options()
            chrome_opt.add_argument('--incognito')
            driver = Chrome(options=chrome_opt)
            sleep(1)
            try:
                driver.get('https://apps.google.com/meet/')
                sleep(2)
                driver.maximize_window()
                sleep(1)
                driver.find_element_by_link_text('Sign in').click()
                sleep(2)
                driver.find_element_by_name('identifier').send_keys(x + '\n')
                sleep(2)
                driver.find_element_by_name('password').send_keys(self.gens.accounts[x] + '\n')
                sleep(2)
                driver.find_element_by_tag_name('input').send_keys(self.meet_link + '\n')
                sleep(3)

                #Is used to click the dismiss button in the microphone javascript permissions popup
                driver.find_element_by_css_selector('#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.vdySc.pMgRYb.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div > span > span').click()

                #Is used to click the join button
                driver.find_element_by_css_selector('#yDmH0d > c-wiz > div > div > div:nth-child(5) > div.crqnQb > div > div > div.vgJExf > div > div > div.d7iDfe.NONs6c > div > div.Sla0Yd > div > div.XCoPyb > div > span > span').click()
                print('\aSelect allow or block on the permissions popup.')
                input('Press enter when you do so.')

                error = False
                while not error:
                    error = True
                    try:
                        found = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]').click()
                    except:
                        print('No find')
                        error = False

                sleep(3)

                for x in range(int(self.how_many)):
                    driver.find_element_by_name('chatTextInput').send_keys(self.spammessage + '\n')
            except driver_except.ElementNotInteractableException:
                self.gens.return_home('Do not minimize, or intereact with the chrome window unless told to do so by the program.')

        driver.quit()
        self.gens.return_home('Chat Spammed Successfully')


gen = generics()
gen.secrets_check()
gen.grab_secrets()
gen.main_page()


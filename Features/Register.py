# coding=utf-8

import unittest
import random
import string


class RegisterCases(unittest.TestCase):
    def __init__(self):
        print 'Register baslamak uzere'

    def valid_register(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Eemail türet
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Şifre yaz
        testrunner.find_element_by_id('password').send_keys('123456')

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('write')
        assert checker.text == 'YAZI GÖNDER'.decode('utf-8')

    def invalid_register_empty_username(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_id('popup-register').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajını kontrol et
        checker = testrunner.find_element_by_class_name('error')
        assert checker.text == 'Kullanıcı adınız boş olamaz.'.decode('utf-8')

    def invalid_register_empty_email(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_id('popup-register').click()

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajını kontrol et
        checker = testrunner.find_element_by_class_name('error')
        assert checker.text == 'E-posta alanı boş olamaz.'.decode('utf-8')

    def invalid_register_inappropriate_email(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_id('popup-register').click()

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ##Hatalı Eemail gir
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys('asdasd')

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajını kontrol et
        checker = testrunner.find_element_by_class_name('error')
        assert checker.text == 'E-posta adresiniz hatalı.'.decode('utf-8')

    def invalid_register_empty_password(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_id('popup-register').click()

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Eemail türet
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajını kontrol et
        checker = testrunner.find_element_by_class_name('error')
        assert checker.text == 'Şifre alanı boş olamaz.'.decode('utf-8')

    def invalid_register_without_agreement(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Eemail türet
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Şifre yaz
        testrunner.find_element_by_id('password').send_keys('123456')

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('error')
        assert checker.text == 'Sözleşmeyi kabul etmeniz gerekmekte.'.decode('utf-8')

    def invalid_register_min_character_username_error(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###Min altında bir isim ekle
        testrunner.find_element_by_id('userName').send_keys('ab')

        ###Eemail türet

        letters = string.ascii_lowercase[:12]
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Şifre yaz
        testrunner.find_element_by_id('password').send_keys('123456')

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('errorBody')
        assert checker.text == 'kullanıcı adı en az 3, en fazla 34 karakterden oluşabilir'.decode('utf-8')

    def invalid_register_max_character_username_error(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###Max sınırını aşan bir isim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(30))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Eemail türet
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Şifre yaz
        testrunner.find_element_by_id('password').send_keys('123456')

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('errorBody')
        assert checker.text == 'kullanıcı adı en az 3, en fazla 34 karakterden oluşabilir'.decode('utf-8')

    def invalid_register_min_character_password_error(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Eemail türet
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Min altında şifre yaz
        testrunner.find_element_by_id('password').send_keys('12')

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('errorBody')
        assert checker.text == 'Şifre 3 karekterden az, 20 karakterden fazla olamaz.'.decode('utf-8')

    def invalid_register_max_character_password_error(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Eemail türet
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Max sınırını aşan şifre yaz
        password = ''.join(random.choice(letters) for i in range(21))
        testrunner.find_element_by_id('password').send_keys(password)

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('errorBody')
        assert checker.text == 'Şifre 3 karekterden az, 20 karakterden fazla olamaz.'.decode('utf-8')

    def invalid_register_used_username(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###Daha önceden kullanılmış isim ekle
        testrunner.find_element_by_id('userName').send_keys('asd')

        ###Eemail türet
        letters = string.ascii_lowercase[:12]
        email_address = 'test_' + ''.join(random.choice(letters) for i in range(7)) + '@deneme.com'
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys(email_address)

        ###Şifre yaz
        testrunner.find_element_by_id('password').send_keys('123456')

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('errorBody')
        assert checker.text == 'Bu kullanıcı adı daha önce kaydedilmiş.'.decode('utf-8')

    def invalid_register_used_email(self, testrunner):
        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###İsim türet
        letters = string.ascii_lowercase[:12]
        username = 'test_' + ''.join(random.choice(letters) for i in range(7))
        testrunner.find_element_by_id('userName').send_keys(username)

        ###Daha önceden kullanılmış email ekle
        testrunner.find_element_by_xpath('//*[@data-yto="registerEmail"]').send_keys('yigit.cetin@yemeksepeti.com')

        ###Şifre yaz
        testrunner.find_element_by_id('password').send_keys('123456')

        ###Kullanıcı sözleşmesini kabul et
        testrunner.find_element_by_name('agreement').click()

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('submit').click()

        ###Üye olunmuş mu kontrol et
        checker = testrunner.find_element_by_class_name('errorBody')
        assert checker.text == 'Bu email adresi daha önce kaydedilmiş.'.decode('utf-8')

    def go_login_page(self, testrunner):

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###Login sayfasına git
        testrunner.find_element_by_xpath('//*[@data-yto="registerLink"]').click()
        print 'Giriş sayfasına tıklanıldı'

        ##Doğrı sayfada mısın kontrol et
        checker = testrunner.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/span')
        assert checker.text == 'Yemek.com üyeliğim yok!'.decode('utf-8')

    def close_register_popup(self,testrunner):

        ###Uye ol'a tıkla
        testrunner.find_element_by_class_name('popupRegisterButton').click()
        print 'Uye ol tıklanıldı'

        ###Popup'ı kapa
        testrunner.find_element_by_class_name('icon-closedWhite').click()
        print 'Pop Up kapatıldı'

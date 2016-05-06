# coding=utf-8

import unittest
from selenium.webdriver.common.action_chains import ActionChains
import string
import random


class SettingsCases(unittest.TestCase):
    def __init__(self):
        print ''

    def go_settings(self,testrunner):

        element = testrunner.find_element_by_class_name('avatar')
        hov = ActionChains(testrunner).move_to_element(element)
        hov.perform()
        print 'Donut üzerine hover yapıldı'

        testrunner.find_element_by_xpath('//*[@data-yto="headerSettings"]').click()
        print 'Ayarlar butonuna basıldı'

    def check_page(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### Basliklar kontrol ediliyor
        Schecker1 = testrunner.find_element_by_xpath('//*[@data-yto="settingsInfo"]')
        assert Schecker1.text == 'Kişisel bilgiler'.decode('utf-8')

        Schecker2 = testrunner.find_element_by_xpath('//*[@data-yto="settingsOther"]')
        assert Schecker2.text == 'Başka başka?'.decode('utf-8')

        Schecker3 = testrunner.find_element_by_xpath('//*[@data-yto="settingsBulletinLabel"]')
        assert Schecker3.text == "Yemek.com'un her hafta atacağı lezzetli e-postalarından almak istiyorum.".decode('utf-8')

        Schecker4 = testrunner.find_element_by_xpath('//*[@id="settingsOverlayContent"]/div[2]/div/div/div/form/div[3]/div/div[2]/button[1]')
        assert Schecker4.text == "İPTAL".decode('utf-8')

        Schecker4 = testrunner.find_element_by_xpath('//*[@id="settingsOverlayContent"]/div[2]/div/div/div/form/div[3]/div/div[2]/button[2]')
        assert Schecker4.text == "AYARLARIMI GÜNCELLE".decode('utf-8')

        Schecker5 = testrunner.find_element_by_class_name('warning')
        assert Schecker5.text == "Zorunlu alanları belirtir.".decode('utf-8')

    def valid_change_name(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ##Ad Soyad alanını değiştir
        testrunner.find_element_by_xpath('//*[@data-yto="settingsName"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="settingsName"]').send_keys('Best Tester in the World')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

    def invalid_change_name_min_req(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ##Ad Soyad alanını değiştir
        testrunner.find_element_by_xpath('//*[@data-yto="settingsName"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="settingsName"]').send_keys('as')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

        ### Hata mesajını kontrol et
        error_checker = testrunner.find_element_by_class_name('error')
        assert error_checker.text == 'Takma Adınız en az 3 en fazla 25 karakterden oluşabilir'.decode('utf-8')

    def invalid_change_name_max_req(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ##Ad Soyad alanını değiştir
        letters = string.ascii_lowercase[:12]
        username = ''.join(random.choice(letters) for i in range(26))
        testrunner.find_element_by_xpath('//*[@data-yto="settingsName"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="settingsName"]').send_keys(username)

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

        ### Hata mesajını kontrol et
        error_checker = testrunner.find_element_by_class_name('error')
        assert error_checker.text == 'Takma Adınız en az 3 en fazla 25 karakterden oluşabilir'.decode('utf-8')

    def get_email_checkbox(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### Email checkbox'ı işaretlendi
        testrunner.find_element_by_xpath('//*[@data-yto="settingsBulletinLabel"]').click()

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

    def valid_update_job(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### Meslek yaz
        testrunner.find_element_by_id('job').clear()
        testrunner.find_element_by_id('job').send_keys('test uzman')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

    def invalid_update_job(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### Meslek yaz
        letters = string.ascii_lowercase[:12]
        job = ''.join(random.choice(letters) for i in range(151))
        testrunner.find_element_by_id('job').clear()
        testrunner.find_element_by_id('job').send_keys(job)

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesaj kontrolü
        error_checker = testrunner.find_element_by_class_name('error')
        assert error_checker.text == 'Meslek alanı 150 karakterden fazla olamaz.'.decode('utf-8')

    def choose_city(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ###şehir seç
        testrunner.find_element_by_class_name('form-control').click()
        testrunner.find_element_by_class_name('form-control').send_keys('istanbul')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

    def choose_gender(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ###cinsiyet seç
        testrunner.find_element_by_xpath('//*[@id="settingsOverlayContent"]/div[2]/div/div/div/form/div[1]/div[6]/div/label[2]/input').click()

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

    def invalid_birthday_date(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ###doğum tarihi gir
        testrunner.find_element_by_id('date').clear()
        testrunner.find_element_by_id('date').send_keys('31231900')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajı
        error = testrunner.find_element_by_class_name('error')
        assert error.text == 'Doğum tarihi hatalıdır.'.decode('utf-8')

    def invalid_birthday_range(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ###doğum tarihi gir
        testrunner.find_element_by_id('date').clear()
        testrunner.find_element_by_id('date').send_keys('31121900')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajı
        error = testrunner.find_element_by_class_name('error')
        assert error.text == 'Yaş aralığı doğru değil.'.decode('utf-8')

    def valid_birthday(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ###doğum tarihi gir
        testrunner.find_element_by_id('date').clear()
        testrunner.find_element_by_id('date').send_keys('31121920')

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

    def close_settings(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### popup kapatılır
        testrunner.find_element_by_xpath('//*[@data-yto="profileSettingsClose"]').click()

    def social_links_max_character_limit(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        letters = string.ascii_lowercase[:12]
        social_link = ''.join(random.choice(letters) for i in range(251))

        ### blog linki
        testrunner.find_element_by_xpath('//*[@data-yto="settingsBlog"]').send_keys(social_link)

        ### fb linki
        testrunner.find_element_by_xpath('//*[@data-yto="settingsFacebook"]').send_keys(social_link)

        ### twitter linki
        testrunner.find_element_by_xpath('//*[@data-yto="settingsTwitter"]').send_keys(social_link)

        ### instagram linki
        testrunner.find_element_by_xpath('//*[@data-yto="settingsInstagram"]').send_keys(social_link)

        ### google linki
        testrunner.find_element_by_xpath('//*[@data-yto="settingsGplus"]').send_keys(social_link)

        ### youtube linki
        testrunner.find_element_by_xpath('//*[@data-yto="settingsYoutube"]').send_keys(social_link)

        ###Ayarları güncelle
        testrunner.find_element_by_class_name('submit').click()

        ###Hata mesajı
        error = testrunner.find_element_by_class_name('error')
        assert error.text == 'Blog adresi 250 karakterden fazla olamaz Facebook adresi 250 karakterden fazla olamaz Twitter adresi 250 karakterden fazla olamaz Instagram adresi 250 karakterden fazla olamaz Google+ adresi 250 karakterden fazla olamaz Youtube adresi 250 karakterden fazla olamaz'.decode('utf-8')

    def change_password_page(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### password linkine tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="settingsPassword"]').click()

        ### sayfayı kontrol et

        text1 = testrunner.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/div/form/div[1]/div/span')
        assert text1.text == 'Mevcut Şifre'.decode('utf-8')

        text2 = testrunner.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/div/form/div[2]/div/span')
        assert text2.text == 'Yeni Şifre'.decode('utf-8')

        ### popup kapatılır
        testrunner.find_element_by_xpath('//*[@data-yto="closePopupWindow"]').click()

    def change_password_valid(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### password linkine tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="settingsPassword"]').click()

        ###Mevcut sifreyi gir
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').send_keys('123456')

        ###Yeni şifre gir
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').send_keys('123456')

        ###Degistir butonuna bas
        testrunner.find_element_by_class_name('submit').click()

    def change_password_invalid_credentials(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### password linkine tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="settingsPassword"]').click()

        ###Mevcut sifreyi gir
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').send_keys('abcd')

        ###Yeni şifre gir
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').send_keys('123456')

        ###Degistir butonuna bas
        testrunner.find_element_by_class_name('submit').click()

        ###Hata metni kontrolü
        error = testrunner.find_element_by_class_name('toast-message')
        assert error.text == 'Bilgiler doğrulanamadı'.decode('utf-8')

    def change_password_invalid_min_characters(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### password linkine tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="settingsPassword"]').click()

        ###Mevcut sifreyi gir
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').send_keys('ab')

        ###Yeni şifre gir
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').send_keys('123456')

        ###Degistir butonuna bas
        testrunner.find_element_by_class_name('submit').click()

        ###Hata metni kontrolü
        error = testrunner.find_element_by_class_name('toast-message')
        assert error.text == 'Şifre 3 karekterden az, 18 karakterden fazla olamaz.'.decode('utf-8')

    def change_password_invalid_max_characters(self,testrunner):

        ###Ayarlar sayfasına gider
        go = SettingsCases()
        go.go_settings(testrunner)

        ### password linkine tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="settingsPassword"]').click()

        ###Mevcut sifreyi gir
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changePassword"]').send_keys('abcdeabcdeabcdeabcd')

        ###Yeni şifre gir
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="changeNewPassword"]').send_keys('123456')

        ###Degistir butonuna bas
        testrunner.find_element_by_class_name('submit').click()

        ###Hata metni kontrolü
        error = testrunner.find_element_by_class_name('toast-message')
        assert error.text == 'Şifre 3 karekterden az, 18 karakterden fazla olamaz.'.decode('utf-8')

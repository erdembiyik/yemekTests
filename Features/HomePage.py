# coding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageCases(unittest.TestCase):
    def __init__(self):
        print ''

    def check_home_page(self, testrunner):
        ### Sayfa başlık kontrolleri
        element1 = testrunner.find_element_by_link_text('Tarifler')
        assert element1.text == 'Tarifler'.decode('utf-8')
        element2 = testrunner.find_element_by_link_text('Keşfet')
        assert element2.text == 'Keşfet'.decode('utf-8')
        element3 = testrunner.find_element_by_link_text('İzle')
        assert element3.text == 'İzle'.decode('utf-8')
        element4 = testrunner.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div[1]/h2/a')
        assert element4.text == 'En Yeniler'.decode('utf-8')
        element5 = testrunner.find_element_by_link_text('Tüm Tarifler')
        assert element5.text == 'Tüm Tarifler'.decode('utf-8')
        element6 = testrunner.find_element_by_class_name('write')
        assert element6.text == 'YAZI GÖNDER'.decode('utf-8')
        element7 = testrunner.find_element_by_link_text('Yemek.com')
        assert element7.text == 'Yemek.com'.decode('utf-8')

    def home_subscription_valid(self, testrunner):
        ###Geçerli bir email adresi girilir
        testrunner.find_element_by_xpath('//*[@data-yto="subscribeEmail"]').send_keys('yigit.cetin@yemeksepeti.com')
        testrunner.find_element_by_xpath('//*[@data-yto="subscribeSubmit"]').click()

        ###Uyarı metni kontrolü
        success = testrunner.find_element_by_class_name('success')
        assert success.text == 'Aboneliğiniz başarı ile gerçekleşmiştir.'.decode('utf-8')

    def home_subscription_invalid(self, testrunner):
        ###Geçerli bir email adresi girilir
        testrunner.find_element_by_xpath('//*[@data-yto="subscribeEmail"]').send_keys('yigit.cetin')
        testrunner.find_element_by_xpath('//*[@data-yto="subscribeSubmit"]').click()

        ###Uyarı metni kontrolü
        error = testrunner.find_element_by_class_name('error')
        assert error.text == 'E-posta adresiniz hatalı.'.decode('utf-8')

    def home_menu_open(self, testrunner):

        ### menüye tıklanır
        testrunner.find_element_by_class_name('menu').click
        print 'Menü açıldı'

    def home_menu_links(self,testrunner):

        menu = HomePageCases()
        menu.home_menu_open(testrunner)

        ### menü başlık kontrolleri
        menu1 = testrunner.find_element_by_link_text('Yemek Tarifleri')
        assert menu1.text == 'Yemek Tarifleri'.decode('utf-8')
        menu2 = testrunner.find_element_by_link_text('Ye')
        assert menu2.text == 'Ye'.decode('utf-8')
        menu3 = testrunner.find_element_by_link_text('İç')
        assert menu3.text == 'İç'.decode('utf-8')
        menu4 = testrunner.find_element_by_link_text('Şaşır')
        assert menu4.text == 'Şaşır'.decode('utf-8')
        menu5 = testrunner.find_element_by_link_text('İzle')
        assert menu5.text == 'İzle'.decode('utf-8')
        menu6 = testrunner.find_element_by_link_text('Öğren')
        assert menu6.text == 'Öğren'.decode('utf-8')
        menu7 = testrunner.find_element_by_link_text('Keşfet')
        assert menu7.text == 'Keşfet'.decode('utf-8')
        menu8 = testrunner.find_element_by_link_text('Sözlük')
        assert menu8.text == 'Sözlük'.decode('utf-8')

    def home_menu_footer_links(self,testrunner):

        menu = HomePageCases()
        menu.home_menu_open(testrunner)

        wait = WebDriverWait(testrunner, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-yto="menuYazarlar"]')))
        assert element.text=='Yazarlar'.decode('utf-8')

        ### menü başlık kontrolleri
        fmenu1 = testrunner.find_element_by_xpath('//*[@data-yto="menuYazarlar"]')
        assert fmenu1.text == 'Yazarlar'.decode('utf-8')
        fmenu2 = testrunner.find_element_by_link_text('//*[@data-yto="menuYazarOl"]')
        assert fmenu2.text == 'Yazar Ol'.decode('utf-8')
        fmenu3 = testrunner.find_element_by_link_text('//*[@data-yto="menuHakkimizda"]')
        assert fmenu3.text == 'Hakkımızda'.decode('utf-8')
        fmenu4 = testrunner.find_element_by_link_text('//*[@data-yto="menuIletisim"]')
        assert fmenu4.text == 'İletişim'.decode('utf-8')
        fmenu5 = testrunner.find_element_by_link_text('//*[@data-yto="menuKullanim"]')
        assert fmenu5.text == 'Kullanım Koşulları'.decode('utf-8')
        fmenu6 = testrunner.find_element_by_link_text('//*[@data-yto="menuGizlilik"]')
        assert fmenu6.text == 'Gizlilik Politikası'.decode('utf-8')



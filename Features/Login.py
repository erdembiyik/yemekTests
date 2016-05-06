# coding=utf-8

import unittest


class LoginCases(unittest.TestCase):
    def __init__(self):
        print ''

    def valid_login(self, testrunner):
        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###alanı temizle ve dogru maili gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').send_keys('yigit.cetin@yemeksepeti.com')
        print 'Dogru mail girildi'

        ###alanı temizle ve dogru sifreyi gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').send_keys('123456')
        print 'Dogru sifre girildi'

        ###giris yap butonuna bas
        testrunner.find_element_by_class_name('submit').click()

        ###uye sayfasının acıldıgını kontrol et
        checker = testrunner.find_element_by_class_name('write')
        assert checker.text == 'YAZI GÖNDER'.decode('utf-8')

    def invalid_login(self, testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###alanı temizle ve yanlıs maili gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').send_keys('xxx')
        print 'Yanlıs mail girildi'

        ###alanı temizle ve yanlıs sifreyi gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').send_keys('xxx')
        print 'Yanlıs sifre girildi girildi'

        ###giris yap butonuna bas
        testrunner.find_element_by_class_name('submit').click()

        ###hata mesajını kontrol et
        error_text = testrunner.find_element_by_class_name('error')
        assert error_text.text == 'Yanlış Kullanıcı Adı veya Şifre'.decode('utf-8')

    def valid_facebook_login(self, testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###facebook butonuna tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="facebook"]').click()
        print 'Facebook butonuna basıldı'

        ###facebook penceresi
        current = testrunner.current_window_handle

        for handle in testrunner.window_handles:
            testrunner.switch_to_window(handle)

        testrunner.find_element_by_id("email").clear()
        testrunner.find_element_by_id("email").send_keys("testfoc32@outlook.com")
        testrunner.find_element_by_id("pass").clear()
        testrunner.find_element_by_id("pass").send_keys("Yc123123")
        testrunner.find_element_by_id("loginbutton").click()

        ###yemek penceresine donus
        testrunner.switch_to_window(current)

        ###uye sayfasının acıldıgını kontrol et
        FBchecker = testrunner.find_element_by_class_name('write')
        assert FBchecker.text == 'YAZI GÖNDER'.decode('utf-8')

    def valid_forgot_password(self, testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###Sifremi unuttum butonuna tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="loginForgotPassword"]').click()
        print 'Sifremi unuttum butonuna basıldı'

        ###Gecerli bir email adresi yazılır
        testrunner.find_element_by_xpath('//*[@data-yto="forgotEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="forgotEmail"]').send_keys('yigit.cetin@yemeksepeti.com')
        print 'Dogru mail girildi'

        ###Gonder butonuna tıklanılır
        testrunner.find_element_by_class_name('submit').click()

        ###sifre sayfasının dogru yonlendıgını kontrol et
        passchecker = testrunner.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div/form/div[2]/p')
        assert passchecker.text == 'E-postanıza gönderilen kodu aşağıdaki alana girerek yeni şifrenizi tanımlayabilirsiniz.'.decode('utf-8')

    def invalid_forgot_password(self, testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###Sifremi unuttum butonuna tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="loginForgotPassword"]').click()
        print 'Sifremi unuttum butonuna basıldı'

        ###Gecerli bir email adresi yazılır
        testrunner.find_element_by_xpath('//*[@data-yto="forgotEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="forgotEmail"]').send_keys('asdas')
        print 'Yanlıs mail girildi'

        ###Gonder butonuna tıklanılır
        testrunner.find_element_by_class_name('submit').click()

        ###sifre sayfasının dogru yonlendıgını kontrol et
        passerror = testrunner.find_element_by_class_name('error')
        assert passerror.text == 'E-posta adresi geçerli değil.'.decode('utf-8')

    def empty_mail_forgot_password(self, testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###Sifremi unuttum butonuna tıkla
        testrunner.find_element_by_xpath('//*[@data-yto="loginForgotPassword"]').click()
        print 'Sifremi unuttum butonuna basıldı'

        ###Gecerli bir email adresi yazılır
        testrunner.find_element_by_xpath('//*[@data-yto="forgotEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="forgotEmail"]').send_keys('')
        print 'mail bos bırakıldı'

        ###Gonder butonuna tıklanılır
        testrunner.find_element_by_class_name('submit').click()

        ###sifre sayfasının dogru yonlendıgını kontrol et
        passerror = testrunner.find_element_by_class_name('error')
        assert passerror.text == 'Bu email adresi kayıtlı değildir.'.decode('utf-8')

    def email_login_max_character_error(self,testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###mail alanına 100 kaarakterden fazla gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').send_keys(
            'abcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjk')
        print ' 100 karakterden fazla girildi girildi'

        ###sifre gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').send_keys('123456')
        print 'sifre girildi'
        
        ###giris yap butonuna bas
        testrunner.find_element_by_class_name('submit').click()
        
        ###uye sayfasının acıldıgını kontrol et
        MXCHchecker = testrunner.find_element_by_class_name('error')
        assert MXCHchecker.text == \
               'Kullanıcı adı veya e-posta alanı 3 karekterden az, 100 karakterden fazla olamaz'.decode('utf-8')

    def password_login_max_character_error(self,testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###mail alanına 100 kaarakterden fazla gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginEmail"]').send_keys('yigit.cetin@yemekseperi.com')
        print 'Email girildi'

        ###sifre gir
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').clear()
        testrunner.find_element_by_xpath('//*[@data-yto="loginPassword"]').send_keys(
            'abcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjkabcdefghjk')
        print '100 karakterden fazla girildi girildi'

        ###giris yap butonuna bas
        testrunner.find_element_by_class_name('submit').click()

        ###uye sayfasının acıldıgını kontrol et
        MXCHchecker = testrunner.find_element_by_class_name('error')
        assert MXCHchecker.text == 'Şifre 3 karekterden az, 100 karakterden fazla olamaz.'.decode('utf-8')

    def close_login_popup(self, testrunner):

        ###Giris yap butonuna bas
        testrunner.find_element_by_class_name("popupLoginButton").click()
        print 'Giris yap butonuna basıldı'

        ###Pop up'ı kapa
        testrunner.find_element_by_class_name('icon-closedWhite').click()
        print 'Login pop up kapatıldı'
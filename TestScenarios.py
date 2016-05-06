# coding=utf-8


import Config
import unittest
import Features
from Features import Login
from Features import Register
from Features import Logout
from Features import Profile
from Features import Settings
from Features import Search
from Features import HomePage


class LogInTests(unittest.TestCase):

    def setUp(self):
        print "Login testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_valid_login(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"

    def test_invalid_login(self):

        login = Features.Login.LoginCases()
        login.invalid_login(self.testrunner.driver)
        print "Login beklenildigi gibi basarisiz"

    def test_valid_facebook_login(self):

        login = Features.Login.LoginCases()
        login.valid_facebook_login(self.testrunner.driver)
        print "Facebook Login beklenildigi gibi basarili"

    def test_valid_forgot_password(self):

        login = Features.Login.LoginCases()
        login.valid_forgot_password(self.testrunner.driver)
        print "Sifremi unuttum islemi beklenildigi gibi basarili"

    def test_invalid_forgot_password(self):

        login = Features.Login.LoginCases()
        login.invalid_forgot_password(self.testrunner.driver)
        print "Sifremi unuttum islemi beklenildigi gibi basarisiz"

    def test_empty_mail_forgot_password(self):

        login = Features.Login.LoginCases()
        login.empty_mail_forgot_password(self.testrunner.driver)
        print "Sifremi unuttum islemi beklenildigi gibi basarisiz"

    def test_max_char_email_login(self):

        login = Features.Login.LoginCases()
        login.email_login_max_character_error(self.testrunner.driver)
        print "Email Maksimum karakter uyarısı verildi"

    def test_max_char_password_login(self):

        login = Features.Login.LoginCases()
        login.password_login_max_character_error(self.testrunner.driver)
        print "Sifre Maksimum karakter uyarısı verildi"

    def test_close_login_popup(self):

        login = Features.Login.LoginCases()
        login.close_login_popup(self.testrunner.driver)
        print "Giriş yap pop up'ı kapatıldı"


class RegisterTests(unittest.TestCase):

    def setUp(self):
        print "Register testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_valid_register(self):

        register = Features.Register.RegisterCases()
        register.valid_register(self.testrunner.driver)
        print "Register istenildigi gibi basarili"

    def test_invalid_register_empty_username(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_empty_username(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_empty_email(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_empty_username(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_inappropriate_email(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_inappropriate_email(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_empty_password(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_empty_password(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_without_agreement(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_without_agreement(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_min_charachter_username(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_min_character_username_error(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_max_charachter_username(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_max_character_username_error(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_min_charachter_password(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_min_character_password_error(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_max_charachter_password(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_max_character_password_error(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_used_username(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_used_username(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_invalid_register_used_email(self):

        register = Features.Register.RegisterCases()
        register.invalid_register_used_email(self.testrunner.driver)
        print "Register hata mesajı istenildigi gibi geldi"

    def test_go_login_page(self):

        register = Features.Register.RegisterCases()
        register.go_login_page(self.testrunner.driver)
        print "Login sayfasına gidildi"

    def test_close_register_popup(self):

        register = Features.Register.RegisterCases()
        register.close_register_popup(self.testrunner.driver)
        print "Üye ol pop up'ı kapatıldı"


class LogOutTests(unittest.TestCase):

    def setUp(self):
        print "Logout testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_logout(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        logout = Features.Logout.LogOutCases()
        logout.valid_logout(self.testrunner.driver)
        print "Logout istenildigi gibi basarili"


class ProfileTests(unittest.TestCase):

    def setUp(self):
        print "Profil sayfasi testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_go_profile(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        profile = Features.Profile.ProfileCases()
        profile.go_profile(self.testrunner.driver)
        print "Profil sayfasına basarili bir sekilde gidildi ve sayfa kontrol edildi"

    def test_go_setting_from_profile(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        profile = Features.Profile.ProfileCases()
        profile.go_setting_from_profile(self.testrunner.driver)
        print "Profil sayfasına basarili bir sekilde gidildi ve sayfa kontrol edildi"


class SettingsTests(unittest.TestCase):

    def setUp(self):
        print "Ayarlar sayfasi testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_check_settings_page(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.check_page(self.testrunner.driver)
        print  "Ayarlar sayfası, sayfa kontrolleri tamam"

    def test_go_settings_change_name_valid(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.valid_change_name(self.testrunner.driver)
        print "Ayarlar sayfasindan ad ve soyad degistirildi"

    def test_go_settings_change_name_invalid_min_req(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.invalid_change_name_min_req(self.testrunner.driver)
        print "Ayarlar sayfasindan ad ve soyad min değerin altında olduğu için degistirilemedi"

    def test_go_settings_change_name_invalid_max_req(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.invalid_change_name_max_req(self.testrunner.driver)
        print "Ayarlar sayfasindan ad ve soyad max değerin üstünde olduğu için degistirilemedi"

    def test_get_email_checkbox(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.get_email_checkbox(self.testrunner.driver)
        print "Ayarlar sayfasindan yemek.com'dan eposta almak istiyorum seçeneği seçildi"

    def test_update_job_valid(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.valid_update_job(self.testrunner.driver)
        print "Ayarlar sayfasindan meslek alanı hatasız değiştirildi"

    def test_update_job_invalid(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.invalid_update_job(self.testrunner.driver)
        print "Ayarlar sayfasindan meslek alanı hata mesajı düzgün alındı"

    def test_choose_city(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.choose_city(self.testrunner.driver)
        print "Ayarlar sayfasindan şehir seçildi"

    def test_choose_gender(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.choose_gender(self.testrunner.driver)
        print "Ayarlar sayfasindan cinsiyet seçildi"

    def test_invalid_birthday_date(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.invalid_birthday_date(self.testrunner.driver)
        print "Ayarlar sayfasindan hatlı doğum günü uyarısı göründü"

    def test_invalid_birthday_range(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.invalid_birthday_range(self.testrunner.driver)
        print "Ayarlar sayfasindan hatlı doğum günü uyarısı göründü"

    def test_valid_birthday_change(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.valid_birthday(self.testrunner.driver)
        print "Ayarlar sayfasindan doğum günü değiştirildi"

    def test_close_settings(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.close_settings(self.testrunner.driver)
        print "Ayarlar sayfasi kapatıldı"

    def test_social_links_max_character_limit(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.social_links_max_character_limit(self.testrunner.driver)
        print "Sosyal ağ linklerine fazla karakter girildi"

    def test_check_change_password_page(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.change_password_page(self.testrunner.driver)
        print "Sifre degistirme sayfasi duzgun"

    def test_change_password_valid(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.change_password_valid(self.testrunner.driver)
        print "Sifre duzgun degıstrıldı"

    def test_change_password_invalid_credentials(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.change_password_invalid_credentials(self.testrunner.driver)
        print "Sifre hata mesajı alındı"

    def test_change_password_invalid_min_characters(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.change_password_invalid_min_characters(self.testrunner.driver)
        print "Sifre hata mesajı alındı"

    def test_change_password_invalid_max_characters(self):

        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        setting = Features.Settings.SettingsCases()
        setting.change_password_invalid_max_characters(self.testrunner.driver)
        print "Sifre hata mesajı alındı"


class SearchTests(unittest.TestCase):

    def setUp(self):
        print "Arama testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_search_page(self):
        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        search = Features.Search.SearchCases()
        search.search_page_search_keyword(self.testrunner.driver)
        print "Arama sayfası dogru geliyor"

    def test_close_search_page(self):
        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        search = Features.Search.SearchCases()
        search.close_search_page(self.testrunner.driver)
        print "Arama sayfası kapatildi"


class HomePageTests(unittest.TestCase):

    def setUp(self):
        print "Arama testleri basliyor"
        self.testrunner = Config.Setup()
        self.testrunner.loader()
        print "Sayfa yuklendi"

    def tearDown(self):
        print "Temizleme islemi basladi"
        self.testrunner.driver.close()
        print "Temizleme islemi bitti"

    def test_check_home_page(self):
        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        home = Features.HomePage.HomePageCases()
        home.check_home_page(self.testrunner.driver)
        print 'Anasayfa başlıkları doğru geliyor'

    def test_home_page_subscription_valid(self):
        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        home = Features.HomePage.HomePageCases()
        home.home_subscription_valid(self.testrunner.driver)
        print 'kayıt işlemi başarılı'

    def test_home_page_subscription_invalid(self):
        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        home = Features.HomePage.HomePageCases()
        home.home_subscription_invalid(self.testrunner.driver)
        print 'kayıt işlemi hatalı'

    def test_open_menu_footer_links(self):
        login = Features.Login.LoginCases()
        login.valid_login(self.testrunner.driver)
        print "Login istenildigi gibi basarili"
        home = Features.HomePage.HomePageCases()
        home.home_menu_footer_links(self.testrunner.driver)
        print 'menü açıldı ve doğru geldi'


if __name__ == '__main__':
    unittest.main(verbosity=2)
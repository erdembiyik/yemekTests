# coding=utf-8

import unittest
from selenium.webdriver.common.action_chains import ActionChains


class LogOutCases(unittest.TestCase):
    def __init__(self):
        print ''

    def valid_logout(self, testrunner):

        element = testrunner.find_element_by_class_name('avatar')
        hov = ActionChains(testrunner).move_to_element(element)
        hov.perform()
        print 'Donut üzerine hover yapıldı'

        testrunner.find_element_by_xpath('//*[@data-yto="headerLogout"]').click()
        print 'Logout butonuna basıldı'
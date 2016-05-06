# coding=utf-8

from TestScenarios import *
import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LogInTests))
    suite.addTest(unittest.makeSuite(RegisterTests))
    suite.addTest(unittest.makeSuite(LogOutTests))
    suite.addTest(unittest.makeSuite(SettingsTests))
    suite.addTest(unittest.makeSuite(SearchTests))
    suite.addTest(unittest.makeSuite(SearchTests))
    suite.addTest(unittest.makeSuite(HomePageTests))
    #dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    #buf = file("C:\Users\yigit.cetin\PycharmProjects\Yemek.com\Reports\TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    buf = file("/users/yigitcetin/PycharmProjects/Yemek.com/Reports/TestReport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='Test Report',
            description='Result of tests'
            )
    EmailHtml = runner.run(suite)
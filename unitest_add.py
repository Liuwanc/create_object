import  unittest
from Day10.add_teach import ciclk_ticher

class Edu_aoto(unittest.TestCase):
    def add_teacher(self):
        driver = ciclk_ticher.create_driver()
        ciclk_ticher.open_url(driver)
        ciclk_ticher.login(driver)
        ciclk_ticher.click_mem(driver)
        ciclk_ticher.click_teacher(driver)
        ciclk_ticher.iframe_swith(driver)
        ciclk_ticher.clic_teacher(driver)
        ciclk_ticher.add_teacher(driver)
        ciclk_ticher.check_add(driver)
    def test_001(self):
        a =self.add_teacher()
        self.assertEqual(a,'13222222222')
if __name__ == '__main__':
    unittest.main()
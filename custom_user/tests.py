from django.test import TestCase
from django.contrib.auth import get_user_model

  
class custom_user_test(TestCase):


    def set_up(self):
        self.user = get_user_model().objects.create_user(
            username = 'ebrahimayyad11',           
            email = 'ayyad_ebrahim@hotmail.com',            
            password = 'ebrahim1234'
        )       


    def create_test(self):
        self.assertEquals(self.user.__str__(),'ebrahimayyad11')    


    def Unique_test(self):
        try:
            self.user2 = get_user_model().objects.create_user(
                username = 'ebrahimayyad11',           
                email = 'ayyad_ebrahim@hotmail.com',            
                password = 'ebrahim1234'
            )           
        except:          
            print('Resgistration falied!')
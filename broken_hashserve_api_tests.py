import unittest
import broken_hashserve_api
from generate_password import generatePassword

unittest.TestLoader.sortTestMethodsUsing = None


class TestBrokenHashServeAPITests(unittest.TestCase):
    def setUp(self):
        self.bhs_api = broken_hashserve_api.BrokenHashServeEndpoints()
        self.gp = generatePassword()

    def test_post_hash_password_succesful(self):
        '''
        See test case 1

        '''
        # todo write a class or function that generates a password
        password = self.gp.generate_Password()
        password_payload = '{"password":"' + password + '"}'
        test_response = self.bhs_api.post_hash_endpoint(password_payload)

        self.assertEqual(test_response[0], 200)

        self.assertIsInstance(test_response[1], str)

    def test_pos_hash_password_invalid_json(self):
        '''
        See test case 2

        '''
        password = self.gp.generate_Password()
        password_payload = '{"password":"' + password + '",}'
        test_response = self.bhs_api.post_hash_endpoint(password_payload)

        self.assertEqual(test_response[0], 400)

        self.assertIsInstance(test_response[1], str)

        self.assertEqual(test_response[1], "Malformed Input\n")

    def test_post_hash_password_emptystring(self):
        '''
        see test case 3

        '''
        password = ""  # testing for empty string, this test case should fail since the server responds with 200
        password_payload = '{"password":"' + password + '"}'
        test_response = self.bhs_api.post_hash_endpoint(password_payload)

        # print(test_response[0], test_response[1], type(test_response[0]), type(test_response[1]))

        self.assertEqual(test_response[0], 400)  # testing for status code of 400, look at defect 2

        self.assertEqual(test_response[1], str)

    def test_get_base64_password(self):
        '''
        see test case 4

        '''
        test_response = self.bhs_api.get_base64_password(1)

        self.assertEqual(test_response[0], 200)

        self.assertIsInstance(test_response[1], str)

    def test_get_base64_password_hash_not_found(self):
        '''
        see test case 5

        '''
        test_response = self.bhs_api.get_base64_password(100000000)  # inserting an absurdly high number to
        # ensure string 'hash not found' is always returned

        self.assertEqual(test_response[0], 400)

        self.assertIsInstance(test_response[1], str)

        self.assertEqual(test_response[1], 'Hash not found\n')

    def test_get_stats(self):
        '''
        see test case 6

        '''
        test_response = self.bhs_api.get_stats()

        self.assertEqual(test_response[0], 200)

        self.assertIsInstance(test_response[1], dict)  # todo write a test that asserts for json not the dictionary type

    def test_shutdown(self):
        '''
        see test case 7

        '''
        test_response = self.bhs_api.shutdown()

        self.assertEqual(test_response, 200)

        self.assertIsInstance(test_response, int)


if __name__ == 'main':
    unittest.main()




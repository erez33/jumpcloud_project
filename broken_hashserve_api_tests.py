import unittest
import broken_hashserve_api
from generate_password import generatePassword

unittest.TestLoader.sortTestMethodsUsing = None


class TestBrokenHashServeAPITests(unittest.TestCase):
    def setUp(self):
        self.bhs_api = broken_hashserve_api.BrokenHashServeEndpoints()
        self.gp = generatePassword()

    @unittest.skip("successful password post")
    def test_post_hash_password_succesful(self):
        # todo write a class or function that generates a password
        password = self.gp.generate_Password()
        password_payload = '{"password":"' + password + '"}'
        test_response = self.bhs_api.post_hash_endpoint(password_payload)

        self.assertEqual(test_response[0], 200)

        self.assertIsInstance(test_response[1], str)

    @unittest.skip("skipping invalid json")
    def test_pos_hash_password_invalid_json(self):
        password = self.gp.generate_Password()
        password_payload = '{"password":"' + password + '",}'
        test_response = self.bhs_api.post_hash_endpoint(password_payload)

        self.assertEqual(test_response[0], 400)

        self.assertIsInstance(test_response[1], str)

        self.assertEqual(test_response[1], "Malformed Input\n")

    @unittest.skip("skipping empty string")
    def test_post_hash_password_emptystring(self):
        password = ""  # testing for empty string, this test case should fail since the server responds with 200
        password_payload = '{"password":"' + password + '"}'
        test_response = self.bhs_api.post_hash_endpoint(password_payload)

        # print(test_response[0], test_response[1], type(test_response[0]), type(test_response[1]))

        self.assertEqual(test_response[0], 400)  # testing for status code of 400, look at defect 2

        self.assertEqual(test_response[1], str)

    @unittest.skip("skipping base64 password")
    def test_get_base64_password(self):
        test_response = self.bhs_api.get_base64_password(1)

        self.assertEqual(test_response[0], 200)

        self.assertIsInstance(test_response[1], str)

    @unittest.skip("skipping base64 password hash_not_found")
    def test_get_base64_password_hash_not_found(self):
        test_response = self.bhs_api.get_base64_password(100000000)  # inserting an absurdly high number to
        # ensure string 'hash not found' is always returned

        self.assertEqual(test_response[0], 400)

        self.assertIsInstance(test_response[1], str)

        self.assertEqual(test_response[1], 'Hash not found\n')

    @unittest.skip("skipping stats")
    def test_get_stats(self):
        test_response = self.bhs_api.get_stats()

        self.assertEqual(test_response[0], 200)

        self.assertIsInstance(test_response[1], dict)  # todo write a test that asserts for json not the dictionary type

    @unittest.skip("skipping shutdown")
    def test_shutdown(self):
        test_response = self.bhs_api.shutdown()
        # print(test_response, type(test_response))

        self.assertEqual(test_response, 200)

        self.assertIsInstance(test_response, int)


if __name__ == 'main':
    unittest.main()

# to execute tests python3 -m unittest -v  tests.py

# t = TestBrokenHashServeAPITests()
# t.setUp()
# t.test_post_hash_password()
# # t.test_get_stats()
# # t.test_shutdown()
# t.test_get_base64_password()
# t.test_post_hash_password_emptystring()
# t.test_pos_hash_password_invalid_json()

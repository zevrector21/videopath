from videopath.apps.videos.tests.endpoints.endpoints_base import EndpointsBaseTestCase

USER_URL = '/v1/user/'

# Uses the standard django frame testing client
class TestCase(EndpointsBaseTestCase):

    def test_get_access(self):
        self.setup_users_and_clients()

        # should get list with one user
        response = self.client_user1.get_json(USER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("count"), 1)

        # should be able to access myself
        response = self.client_user1.get_json(USER_URL + "0/")
        self.assertEqual(response.status_code, 200)

        # should not be able to access other user
        response = self.client_user1.get_json(USER_URL + "1/")
        self.assertEqual(response.status_code, 404)

    def test_change_email(self):
        self.setup_users_and_clients()

        new_email = "other@email.com"
        password = self.USER1_DETAILS["password"]

        # should not work, because a password is needed for the change
        response = self.client_user1.put_json(USER_URL + "me/", {"email":new_email})
        self.assertEqual(response.status_code,403)

        # should not work, as the email is malformed
        response = self.client_user1.put_json(USER_URL + "me/", {"email":"malformed email", "password":password})
        self.assertEqual(response.status_code,400)

        # should work
        response = self.client_user1.put_json(USER_URL + "me/", {"email":new_email, "password":password})
        self.assertEqual(response.status_code,200)

        user = self.user1.__class__.objects.get(pk=self.user1.pk)
        self.assertEqual(user.email, "other@email.com" )

    def test_change_password(self):
    	self.setup_users_and_clients()
        
        new_password = "password2"
        password = self.USER1_DETAILS["password"]

        # should not work, because a password is needed for the change
        response = self.client_user1.put_json(USER_URL + "0/", {"new_password":new_password})
        self.assertEqual(response.status_code,403)

        # should not work, as the email is to short
        response = self.client_user1.put_json(USER_URL + "0/", {"new_password":"short", "password":password})
        self.assertEqual(response.status_code,400)

        # should work
        response = self.client_user1.put_json(USER_URL + "0/", {"new_password":new_password, "password":password})
        self.assertEqual(response.status_code,200)

        user = self.user1.__class__.objects.get(pk=self.user1.pk)
        self.assertEqual(user.check_password(new_password), True)


    def test_signup(self):
        self.setup_users_and_clients()

        data = {
            'username': 'dave', 
            'password': 'pw'
        }

        # not enough data provided
        response = self.client.post_json(USER_URL, data)
        self.assertEqual(response.status_code, 400)

        # pw too short
        data = {
                'username': 'dave_new', 
                'password': 'short',
                'email': 'dscharf@gmx.de'
        }
        response = self.client.post_json(USER_URL, data)
        self.assertEqual(response.status_code, 400)

        # invalid email
        data = {
            'username': 'dave_new', 
            'password': 'long_passsword',
            'email': 'dscharfgmx.de'
        }
        response = self.client.post_json(USER_URL, data)
        self.assertEqual(response.status_code, 400)

        # taken username
        data = {
            'username': 'dave', 
            'password': 'long_passsword',
            'email': 'dscharf@gmx.de'
        }
        response = self.client.post_json(USER_URL, data)
        self.assertEqual(response.status_code, 400)

        # taken email
        data = {
            'username': 'dave_new', 
            'password': 'long_passsword',
            'email': 'david@videopath.com'
        }
        response = self.client.post_json(USER_URL, data)
        self.assertEqual(response.status_code, 400)

        # should pass
        data = {
            'username': 'dave_new', 
            'password': 'long_passsword',
            'email': 'dscharf@gmx.de'
        }
        response = self.client.post_json(USER_URL, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("username"), "dave_new")

        # now check that signin works
        login = self.client.login(username="dave_new", password="long_passsword")
        self.assertEqual(login, True)


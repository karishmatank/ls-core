import unittest
import shutil
import os
from app import app
import yaml

class RoutesTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

        # Create a test data directory if it doesn't already exist
        self.data_path = os.path.join(os.path.dirname(__file__), 'data')
        os.makedirs(self.data_path, exist_ok=True)

        # Create a users yaml file
        self.yaml_path = os.path.join(os.path.dirname(__file__), 'users.yml')
        with open(self.yaml_path, 'w') as file:
            yaml.safe_dump({'admin': '$2b$12$ugokt6qiEsW28czTnPB6j.3x9/cZrZLsyTUW5qyxykp0JoW3uzIDu'}, file)

    def tearDown(self):
        shutil.rmtree(self.data_path, ignore_errors=True)
        os.remove(self.yaml_path)

    def _create_document(self, name, content=''):
        with open(os.path.join(self.data_path, name), 'w') as file:
            file.write(content)

    def _admin_session(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['is_signed_in'] = True
                sess['username'] = 'admin'
            return c

    def test_index(self):
        """Test index route ('/')"""
        self._create_document("about.md")
        self._create_document("changes.txt")

        response = self.client.get('/')
        body = response.get_data()

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'about.md', body)
        self.assertIn(b'changes.txt', body)

        # Added in following test after seeing solution
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    def test_file_contents(self):
        """Test route that displays file contents"""
        self._create_document("changes.txt", "There are many changes.")

        # Add context manager after seeing solution to supress ResourceWarnings
        with self.client.get('/changes.txt') as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'There are many changes.', response.get_data())

            # Added in following test after seeing solution
            self.assertEqual(response.content_type, "text/plain; charset=utf-8")

    def test_nonexistent_file(self):
        """Test what happens with file that doesn't exist"""
        with self.client.get('/nonexistent-file.txt') as response:
            # We get a 302 status code
            self.assertEqual(response.status_code, 302)

            # Get redirect location, we will want to make a get request to this location to see response
            redirect_location = response.headers['Location']

        # Check response after redirect
        with self.client.get(redirect_location) as response:
            self.assertIn('nonexistent-file.txt does not exist.', response.get_data(as_text=True))

            self.assertEqual(response.content_type, "text/html; charset=utf-8")

        # Make sure message is gone after reload 
        # (added after seeing comment in solution, solved w/out seeing solution)
        with self.client.get("/") as response:
            self.assertNotIn('nonexistent-file.txt does not exist.', response.get_data(as_text=True))

    def test_md_file(self):
        """Test viewing markdown file"""
        self._create_document("about.md", "# This is my app.")
        
        with self.client.get('/about.md') as response:
            self.assertEqual(response.status_code, 200)

            # Response should be HTML
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            # HTML response should have appropriate tags
            body = response.get_data(as_text=True)
            self.assertIn("<h1>This is my app.</h1>", body)

    def test_edit_file(self):
        """Test edit functionality"""
        self._create_document("changes.txt")
        self.client = self._admin_session()

        with self.client.get('/changes.txt/edit') as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            # Ensure the edit page has 1) the title we expect and 2) a textarea box
            body = response.get_data(as_text=True)
            self.assertIn('Edit content of changes.txt', body)
            self.assertIn("<textarea", body)

    def test_edit_nonexistent_file(self):
        """Test edit functionality with a nonexistent file"""
        self.client = self._admin_session()

        with self.client.get('/nonexistent-file.txt/edit') as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            self.assertIn('nonexistent-file.txt does not exist.', response.get_data(as_text=True))

    def test_edit_signed_out(self):
        """Test edit functionality when user is signed out"""
        self._create_document("changes.txt")

        with self.client.get('/changes.txt/edit') as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            body = response.get_data(as_text=True)
            self.assertIn("You must be signed in to do that", body)
            self.assertIn("Username:", body)
            self.assertIn("Password:", body)

    def test_save_file(self):
        """Test save functionality"""
        self._create_document("changes.txt")
        self.client = self._admin_session()

        data = {'contents': "This is part of a test."}
        with self.client.post('/changes.txt', data=data) as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            self.assertIn('changes.txt has been edited.', response.get_data(as_text=True))

        # Test that the content matches
        with self.client.get('/changes.txt') as response:
            self.assertEqual(response.get_data(as_text=True), data['contents'])

    def test_save_file_signed_out(self):
        """Test save functionality when signed out"""
        self._create_document("changes.txt")

        data = {'contents': "This is part of a test."}
        with self.client.post('/changes.txt', data=data) as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            body = response.get_data(as_text=True)
            self.assertIn("You must be signed in to do that", body)
            self.assertIn("Username:", body)
            self.assertIn("Password:", body)


    def test_new_file_form(self):
        """Test form we see when making a get request to /new"""
        self.client = self._admin_session()
        with self.client.get('/new') as response:
            body = response.get_data(as_text=True)
            self.assertIn('Add a new document:', body)
            self.assertIn('<input name="new-title"', body)
            self.assertIn('<button type="submit">', body)

    def test_new_file_form_signed_out(self):
        """Test new file form access when signed out"""
        with self.client.get('/new') as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            body = response.get_data(as_text=True)
            self.assertIn("You must be signed in to do that", body)
            self.assertIn("Username:", body)
            self.assertIn("Password:", body)
    
    def test_new_file_submit(self):
        """Test form to make sure it creates file successfully"""
        self.client = self._admin_session()
        data = {'new-title': 'test.txt'}
        with self.client.post('/new', data=data) as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            self.assertIn('test.txt has been created.', response.get_data(as_text=True))
        
    def test_new_file_incorrect_name(self):
        """Test form to see if it catches duplicate name or no name"""
        self._create_document("test.txt")
        self.client = self._admin_session()

        data = {'new-title': 'test.txt'}
        with self.client.post('/new', data=data) as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("test.txt already exists.", response.get_data(as_text=True))

        data = {'new-title': ''}
        with self.client.post('/new', data=data) as response:
            self.assertEqual(response.status_code, 422)
            self.assertIn("A name is required.", response.get_data(as_text=True))

    def test_new_file_submit_signed_out(self):
        """Test new file form submit when logged out"""
        data = {'new-title': 'test.txt'}
        with self.client.post('/new', data=data) as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            body = response.get_data(as_text=True)
            self.assertIn("You must be signed in to do that", body)
            self.assertIn("Username:", body)
            self.assertIn("Password:", body)

    def test_delete_file(self):
        """Test delete form"""
        self._create_document("test.txt")
        self.client = self._admin_session()

        with self.client.post('/test.txt/delete', follow_redirects=True) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("test.txt has been deleted.", response.get_data(as_text=True))

        # Forgot to test that document list no longer includes test.txt
        with self.client.get('/') as response:
            self.assertNotIn('test.txt', response.get_data(as_text=True))

    def test_delete_nonexistent_file(self):
        """Test delete on nonexistent file"""
        self.client = self._admin_session()
        with self.client.post('/nonexistent-file.txt/delete') as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            self.assertIn('nonexistent-file.txt does not exist.', response.get_data(as_text=True))

    def test_delete_signed_out(self):
        self._create_document("test.txt")
        with self.client.post('/test.txt/delete') as response:
            self.assertEqual(response.status_code, 302)
            redirect_location = response.headers['Location']

        with self.client.get(redirect_location) as response:
            body = response.get_data(as_text=True)
            self.assertIn("You must be signed in to do that", body)
            self.assertIn("Username:", body)
            self.assertIn("Password:", body)

    def test_sign_in(self):
        """Test sign in link"""
        with self.client.get('/users/signin') as response:
            self.assertEqual(response.status_code, 200)

            body = response.get_data(as_text=True)
            self.assertIn('Username:', body)
            self.assertIn('Password:', body)

    def test_sign_in_validation(self):
        """Test sign in validation"""
        data = {'username': 'admin', 'password': 'secret'}
        with self.client.post("/users/validate", data=data, follow_redirects=True) as response:
            self.assertEqual(response.status_code, 200)

            body = response.get_data(as_text=True)
            self.assertIn('Welcome', body)
            self.assertIn('Signed in as admin.', body)
    
    def test_sign_in_invalid(self):
        """Test sign in with invalid credentials"""
        data = {'username': '', 'password': ''}
        with self.client.post('/users/validate', data=data) as response:
            self.assertEqual(response.status_code, 422)

            body = response.get_data(as_text=True)
            self.assertIn('Invalid credentials', body)
            self.assertIn('Username:', body)
            self.assertIn('Password:', body)
    
    def test_sign_out(self):
        data = {'username': 'admin', 'password': 'secret'}
        self.client.post("/users/validate", data=data, follow_redirects=True)

        with self.client.post('/users/signout', follow_redirects=True) as response:
            self.assertEqual(response.status_code, 200)
            
            body = response.get_data(as_text=True)
            self.assertIn('You have been signed out.', body)
            self.assertIn('Sign In', body)

if __name__ == '__main__':
    unittest.main()
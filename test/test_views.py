import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Aneta", "mgs":Hello World!"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=XML')
        self.assertEqual(b'<greetings>\n <name>Aneta</name>\n <msg>Hello world</greetings>','{, rv.data)

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        JSON_Datalist = json.loads(rv.data)
        JSON_Result = {"imie":"Kamila", "msg":"Hello World!"}
        self.assertDictEqual(JSON_Result, JSON_Datalist)

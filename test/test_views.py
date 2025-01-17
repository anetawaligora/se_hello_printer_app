import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
import json


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get("/outputs")
        s = str(rv.data)
        ",".join(SUPPORTED) in s

    def test_msg_with_output_xml(self):
        rv = self.app.get("/?output=XML")
        self.assertEqual(
            b"<greetings>\n<name>Natalia</name>\n<msg>Hello World!</msg>\n</greetings>", # noqa
            rv.data
        )

    def test_msg_with_output_json(self):
        rv = self.app.get("/?output=json&name=kamila")
        JSON_Datalist = json.loads(rv.data)
        JSON_Result = {"imie": "kamila", "msg": "Hello World!"}
        self.assertDictEqual(JSON_Result, JSON_Datalist)

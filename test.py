import os
import json
import unittest
from subprocess import check_call


class TestTfModule(unittest.TestCase):

    TFSTATE_FILE_PATH = 'terraform.tfstate'

    def setUp(self):
        check_call(['terraform', 'plan'])
        check_call(['terraform', 'apply'])
        with open(self.TFSTATE_FILE_PATH) as tfstate_file:
            self.tfstate = json.load(tfstate_file)

    def tearDown(self):
        try:
            os.unlink(self.TFSTATE_FILE_PATH)
        except OSError:
            pass

    def test_module_outputs_an_id(self):
        outputs = self.tfstate['modules'][0]['outputs']
        assert outputs.get('id')

    def test_module_outputs_a_name(self):
        outputs = self.tfstate['modules'][0]['outputs']
        assert outputs.get('name')

    def test_module_provisions_a_random_id(self):
        resources = self.tfstate['modules'][0]['resources']
        matching_resources = [
            r for r in resources
            if resources[r]['type'] == 'random_id'
        ]
        assert len(matching_resources) == 1
            

    def test_module_provisions_a_random_pet(self):
        resources = self.tfstate['modules'][0]['resources']
        matching_resources = [
            r for r in resources
            if resources[r]['type'] == 'random_pet'
        ]
        assert len(matching_resources) == 1

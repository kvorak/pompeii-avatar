import unittest
import manifestation.Manifest
from manifestation.tests.testmodule import functions


class Test_Manifest(unittest.TestCase):

    mine = None

    def setUp(self):
        self.mine = manifestation.Manifest.ModuleManifest(functions)

    def test_callables(self):
        funcs = self.mine.callables()

        self.assertEqual(len(funcs), 2)

if __name__ == '__main__':
    unittest.main()

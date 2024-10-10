import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../build')))

import sign_module 

class TestSignDatabase(unittest.TestCase):
    
    def setUp(self):
        self.db = sign_module.SignDatabase()

    def test_add_sign(self):
        sign1 = sign_module.Sign("Stop", 1, sign_module.Coordinates(45.1234, 55.1234))
        self.db.add_sign(sign1)
        with self.assertRaises(RuntimeError):
            self.db.add_sign(sign1)

    def test_remove_sign(self):
        sign1 = sign_module.Sign("Stop", 1, sign_module.Coordinates(45.1234, 55.1234))
        self.db.add_sign(sign1)
        self.assertTrue(self.db.remove_sign(1)) 
        with self.assertRaises(RuntimeError):
            self.db.find_sign(1)

        result = self.db.remove_sign(999) 
        self.assertFalse(result) 

    def test_find_sign_not_found(self):
        with self.assertRaises(RuntimeError):
            self.db.find_sign(999)

    def test_add_duplicate_sign(self):
        sign1 = sign_module.Sign("Stop", 1, sign_module.Coordinates(45.1234, 55.1234))
        self.db.add_sign(sign1)
        with self.assertRaises(RuntimeError):
            self.db.add_sign(sign1) 

    def test_add_multiple_signs(self):
        signs_to_add = [
        sign_module.Sign("Stop", 1, sign_module.Coordinates(45.1234, 55.1234)),
        sign_module.Sign("Yield", 2, sign_module.Coordinates(40.7128, -74.0060)),
        sign_module.Sign("Speed Limit", 1, sign_module.Coordinates(50.8503, 4.3517)),  # Дубликат
        sign_module.Sign("No Entry", 3, sign_module.Coordinates(48.8566, 2.3522))]

        successfully_added, failed_to_add = self.db.add_multiple_signs(signs_to_add)

        self.assertEqual(len(successfully_added), 3)
        self.assertEqual(len(failed_to_add), 1)

        print("Successfully added signs:")
        for sign in successfully_added:
            print(f"Sign {sign.name} with ID {sign.id}")

        print("Failed to add signs:")
        for sign in failed_to_add:
            print(f"Sign {sign.name} with ID {sign.id}")

if __name__ == '__main__':
    unittest.main()

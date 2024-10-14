import unittest
from factories import models

class testmodels:

    def test_create(self):
        pass
    def test_read(Self):
        pass
    def test_delete(self):
        instance = YourModelClass.objects.create(field_name="value")
        instance.delete()
        self.assertFalse(YourModelClass.objects.filter(id=instance.id).exists())
    def test_list_all(Self):
          result = self.objects_list  

        self.assertEqual(len(result), 3)
        self.assertIn(self.obj1, result)
        self.assertIn(self.obj2, result)
        self.assertIn(self.obj3, result)
        
    def test_find_by_name(self,name):
        for obj in self.objects_list:
            if obj.name == name:
                return obj
        return None

    def test_find_by_name(self):
        # Try finding an object by name
        result = self.find_by_name("Object 2")
    def test_find_by_category(Self):
        pass
    def test_find_by_availability(self):
        def test_find_by_availability(self):
    # Example of finding objects by availability (assuming a boolean field "available")
    available_objects = YourModelClass.objects.filter(available=True)
    self.assertGreater(len(available_objects), 0)  # Make sure there's at least one available object

    for obj in available_objects:
        self.assertTrue(obj.available)

if __name__ == '__main__':
    unittest.main()

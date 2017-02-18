import sys
sys.path.append("C:\\Users\\babak\\Desktop\\Udacity\\python\\mongo");
import mongo
import unittest
class TestUpper(unittest.TestCase):
    def test_mongo(self):
        result=mongo.find_one();
        expect="";
        for c in result:
            expect=c.get("isDone");
        
        self.assertEqual("true",expect);
if __name__=="__main__":
    unittest.main();

    

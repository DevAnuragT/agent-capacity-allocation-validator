import math,unittest
from agent import analyze
def p(): return {"resources":{"eng":10,"des":4},"assignments":[{"id":"a","resource":"eng","amount":3}]}
class Tests(unittest.TestCase):
 def test_ok(self): self.assertEqual(analyze(p())["status"],"within_capacity")
 def test_remaining(self): self.assertEqual(analyze(p())["resources"][0]["remaining"],7)
 def test_over(self): x=p(); x["assignments"][0]["amount"]=11; self.assertEqual(analyze(x)["status"],"overallocated")
 def test_multiple(self): x=p(); x["assignments"].append({"id":"b","resource":"eng","amount":7}); self.assertEqual(analyze(x)["resources"][0]["allocated"],10)
 def test_unknown(self): x=p(); x["assignments"][0]["resource"]="x"; self.assertRaises(ValueError,analyze,x)
 def test_duplicate(self): x=p(); x["assignments"].append(x["assignments"][0]); self.assertRaises(ValueError,analyze,x)
 def test_bool(self): x=p(); x["resources"]["eng"]=True; self.assertRaises(ValueError,analyze,x)
 def test_nan(self): x=p(); x["assignments"][0]["amount"]=math.nan; self.assertRaises(ValueError,analyze,x)
if __name__=="__main__": unittest.main()

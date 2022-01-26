class Backwords:
    
    def testispalindrome(self,in1):
        revword = self._reverseastring_(in1)
        if revword == in1:
            return True
        else:
            return False
    
    def _reverseastring_(self,in1):
        lenin = len(in1)-1
        outvar = ''
        while lenin > -1:
            outvar = outvar + in1[lenin]
            lenin = lenin - 1
        return outvar

testaword = Backwords()

print(testaword.testispalindrome("potato"))
#print(testaword.reverseastring("Cheese"))
print(testaword._reverseastring_("in1"))

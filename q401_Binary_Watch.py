class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        output_list = []
        self.returnBinaryOutputList(num,output_list)
        return self.createOutputTuple(output_list)[::-1]

    def returnBinaryOutputList(self ,num ,output_list ,input_string='' ,target=10):
        if target < num or target <0:
            return

        if target == 0:
            if num == 0:
                output_list+=[input_string]

        for i in ['1','0']:
            if i == '1':
                self.returnBinaryOutputList(num-1 ,output_list ,input_string=input_string+'1' ,target=target-1)
            else:
                self.returnBinaryOutputList(num ,output_list ,input_string=input_string+'0' ,target=target-1)

    def createOutputTuple(self,output_list):
        tupleList = map(lambda x:(int(x[:4],2),int(x[4:],2)) ,output_list)
        tupleList = filter(lambda x:x[0]<12 and x[1]<60 ,tupleList)
        return list(map(lambda x:str(x[0])+':'+"%02d"%x[1] ,tupleList))

from unittest import TestCase
import day5


class TestComputeStack(TestCase):
    def test_computeStack_1(self):
        stack = ["0001","0","0","0","99"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["2","0","0","0","99"], stackResult)

    def test_computeStack_2(self):
        stack = ["2","3","0","3","99"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["2","3","0","6","99"], stackResult)

    def test_computeStack_3(self):
        stack = ["2","4","4","5","99","0"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["2","4","4","5","99","9801"], stackResult)

    def test_computeStack_4(self):
        stack = ["1","1","1","4","99","5","6","0","99"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["30","1","1","4","2","5","6","0","99"], stackResult)

    def test_computeStack_1_param1Mode_immediate(self):
        stack = ["0101","1","0","2","99"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["0101","1","102","2","99"], stackResult)

    def test_computeStack_1_param2Mode_immediate(self):
        stack = ["1001","1","2","2","99"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["1001","1","3","2","99"], stackResult)

    def test_computeStack_1_immediate(self):
        stack = ["1101","3","2","2","99"]
        stackResult = day5.computeStack(stack)
        self.assertEqual(["1101","3","5","2","99"], stackResult)

    def test_decodeOpcodeAndParamModes(self):
        opcode, param1Mode, param2Mode = day5.decodeOpcodeAndParamModes("1002")
        self.assertEqual(2, opcode)
        self.assertEqual(0, param1Mode)
        self.assertEqual(1, param2Mode)

    def test_decodeOpcodeAndParamModes_short(self):
        opcode, param1Mode, param2Mode = day5.decodeOpcodeAndParamModes("1")
        self.assertEqual(1, opcode)
        self.assertEqual(0, param1Mode)
        self.assertEqual(0, param2Mode)





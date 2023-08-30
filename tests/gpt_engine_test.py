import unittest
from src.gpt_engine.gpt_engine import GPTEngineModel
from unittest.mock import patch

class TestGPTEngine(unittest.TestCase):

    def test_get_context(self):
        gpt_engine = GPTEngineModel("Write a poem", "about love")
        context = gpt_engine._get_context()
        self.assertEqual(context, "Write a poem about love")

    @patch.object(GPTEngineModel, "_get_file")
    def test_batch_process(self, mock_get_file):
        mock_get_file.return_value = "This is a test document."
        gpt_engine = GPTEngineModel("Write a poem", "about love")
        messages = gpt_engine._batch_process("test.docx")
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[0]["content"], "You are a intelligent assistant.")
        self.assertEqual(messages[1]["role"], "user")
        self.assertEqual(messages[1]["content"], "Write a poem about love: \nThis is a test document.")

    @patch.object(GPTEngineModel, "_get_file")
    def test_generate_response(self, mock_get_file):
        mock_get_file.return_value = "This is a test document."
        gpt_engine = GPTEngineModel("Write a poem", "A poem about love")
        response = gpt_engine.generate_response("test.docx")
        self.assertGreater(len(response), 0)

if __name__ == "__main__":
    unittest.main()
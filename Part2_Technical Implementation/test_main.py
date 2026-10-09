import unittest
from unittest.mock import patch, Mock

import main


class TestTextProcessing(unittest.TestCase):
    def test_split_text(self):
        chunks = main.split_text("abcdefghij", chunk_size=4)
        self.assertEqual(chunks, ["abcd", "efgh", "ij"])

    def test_split_text_rejects_zero_size(self):
        with self.assertRaises(ValueError):
            main.split_text("hello", chunk_size=0)

    def test_final_summary_has_at_most_three_bullets(self):
        fake_response = Mock()
        fake_response.content = "- One\n- Two\n- Three\n- Four"

        with patch.object(main.llm, "invoke", return_value=fake_response):
            result = main.create_final_summary(["some source text"])

        self.assertEqual(len(result.splitlines()), 3)
        self.assertTrue(all(line.startswith("- ") for line in result.splitlines()))

    def test_empty_final_summary_raises_error(self):
        fake_response = Mock()
        fake_response.content = ""

        with patch.object(main.llm, "invoke", return_value=fake_response):
            with self.assertRaises(RuntimeError):
                main.create_final_summary(["some source text"])


if __name__ == "__main__":
    unittest.main()

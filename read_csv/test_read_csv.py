import unittest
import os, tempfile
from read_csv.read_csv import read_csv_chunks


class ReadCSVTestCase(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()
        with os.fdopen(self.fd, "w") as f:
            f.write("col1, col2, col3\n")
            for i in range(2000):
                f.write(f"{i}, {i+1}, {i+2}\n")

    def teatDown(self):
        os.remove(self.path)

    def test_chunks(self):
        chunks = list(read_csv_chunks(self.path, chunk_size = 500))
        print(chunks)
        self.assertEqual(len(chunks), 5)
        self.assertEqual(len(chunks[0]), 1)

if __name__ == "__main__":
    unittest.main()

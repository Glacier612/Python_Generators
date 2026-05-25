""" Write a generator to read a large CSV file in chunks
without loading it all into memory."""

from typing import Generator


def read_csv_chunks(file_path: str,
                    chunk_size: int = 1000) -> Generator[list, None, None]:
    """
    Read CSV file in chunks
    :param file_path: CSV file path
    :param chunk_size: Chunk of row that will be read at once
    :return: Generator yields rows as list
    """
    try:
        with open(file_path, mode='r', encoding="utf-8") as f:
            chunk = []
            for line in f:
                row = line.strip("\n").split(",")
                print("...line: ",row)

                chunk.append(row)
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk.clear()  # cleaning chunk to reduce memory usage
            yield from [chunk] if chunk else []
    except FileNotFoundError as error:
        raise RuntimeError(f"File {file_path} not found") from error
    except Exception as error:
        raise RuntimeError(f"Error in reading file: {error}") from error


if __name__ == "__main__":
    for rows in read_csv_chunks(r"C:\Users\himan\PyCharmMiscProject"
                                r"\Generators\Python_Generators\read_csv\organizations-500000.csv"):
        print(f"processing chunk of {len(rows)} rows")

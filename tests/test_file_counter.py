from file_counter import file_counter
def test_file_counter_valid_file():
    assert 0 == file_counter.count_lines("testdata/empty.file.txt")
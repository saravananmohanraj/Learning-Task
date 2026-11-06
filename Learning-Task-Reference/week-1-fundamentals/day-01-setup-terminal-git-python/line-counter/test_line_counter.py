from line_counter import count_word

def test_word_found_multiple_times(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("deploy spark cluster\nwrite python etl\nspark streaming app\n")
    assert count_word(str(test_file), "spark") == 2

def test_word_not_found(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("write python etl\nload sql tables\n")
    assert count_word(str(test_file), "spark") == 0
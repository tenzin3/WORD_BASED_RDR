from word_based_rdr.preprocessing.preprocessor import file_2_botok


def test_file_2_botok():
    assert (
        file_2_botok("༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེ-འི་ ཕྲེང་བ།")
        == "རྒྱལ་པོ་ལ་གཏམ་བྱ་བ་རིན་པོ་ཆེའི་ཕྲེང་བ་"
    )

from pathlib import Path

from botok import WordTokenizer
from botok.config import Config

from ..preprocessing.preprocessor import file_2_botok


def botok_max_matcher(file_string, preprocess=False):
    if preprocess:
        file_string = file_2_botok(file_string)

    config = Config(dialect_name="general", base_path=Path.home())
    wt = WordTokenizer(config=config)
    tokens = wt.tokenize(file_string, split_affixes=False)

    max_match_output = ""
    for token in tokens:
        max_match_output += token.text_cleaned + " "
    return max_match_output


if __name__ == "__main__":
    # print(file_2_botok("༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེ-འི་ ཕྲེང་བ།"))
    print(botok_max_matcher("༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེའི་ ཕྲེང་བ།"), end="")
    # print(gold_corpus_2_tagger("༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེ-འི་ ཕྲེང་བ།"))

    # file_2_botok
    # ༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེའི་ ཕྲེང་བ།
    # རྒྱལ་པོ་ལ་གཏམ་བྱ་བ་རིན་པོ་ཆེའི་ཕྲེང་བ་

    # gold_corpus_2_Tagger
    # ༄༅། རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེའི་ ཕྲེང་བ་
    pass

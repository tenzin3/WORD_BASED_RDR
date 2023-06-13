import re

from pybo.corpus.word_cleanup import word_cleanup


def replace_initial_patterns(file_string):
    # Some signs are presented in human annotated training files which needs to be edited
    initial_patterns = {"?": " ", "+": " ", "-": "", "[ ]+": " "}
    modified_content = re.sub(
        "|".join(re.escape(key) for key in initial_patterns.keys()),
        lambda match: initial_patterns[match.group(0)],
        file_string,
    )
    return modified_content


def file_2_botok(file_string):
    """
    input: string of a file before going under max match(botok)
    output/return: cleaned/preprocess string
    *Puntuation wont be present in the output
    (because token.text_cleaned attribute of '༄༅།' is ''), and the character wont also effect in token adjustment
    """

    modified_content = replace_initial_patterns(file_string)
    print(modified_content)
    preprocessed_string = word_cleanup(modified_content)
    return preprocessed_string


def gold_corpus_2_tagger(file_string):
    modified_content = replace_initial_patterns(file_string)
    print(modified_content)
    preprocessed_string = ""

    words = modified_content.split()
    for word in words:
        temp_word = word_cleanup(" " + word + " ")
        preprocessed_string += temp_word + " "

    return preprocessed_string


if __name__ == "__main__":
    # print(file_2_botok("༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེ-འི་ ཕྲེང་བ།"))
    # print(gold_corpus_2_tagger("༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེ-འི་ ཕྲེང་བ།"))

    # file_2_botok
    # ༄༅། །རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེའི་ ཕྲེང་བ།
    # རྒྱལ་པོ་ལ་གཏམ་བྱ་བ་རིན་པོ་ཆེའི་ཕྲེང་བ་

    # gold_corpus_2_Tagger
    # ༄༅། རྒྱལ་པོ་ ལ་ གཏམ་ བྱ་བ་ རིན་པོ་ཆེའི་ ཕྲེང་བ་

    pass

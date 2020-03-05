import zipfslaw
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEXT_DIR_ENG = os.path.join(CURRENT_DIR, 'parsed html docs')
TEXT_DIR_SPANISH = os.path.join(CURRENT_DIR, 'parsed html docs (spanish)')
TEXT_DIR_ITALIAN = os.path.join(CURRENT_DIR, 'parsed html docs (italian)')


def main():
    eng_text = zipfslaw.order_text(TEXT_DIR_ENG)
    eng_frequency = zipfslaw.top_word_frequencies(eng_text, 135)
    eng_data = zipfslaw.generate_zipf_data(eng_frequency)
    zipfslaw.print_data(eng_data, "eng_test.csv")

    spanish_text = zipfslaw.order_text(TEXT_DIR_SPANISH)
    spanish_frequency = zipfslaw.top_word_frequencies(spanish_text, 135)
    spanish_data = zipfslaw.generate_zipf_data(spanish_frequency)
    zipfslaw.print_data(spanish_data, "spanish_test.csv")

    italian_text = zipfslaw.order_text(TEXT_DIR_ITALIAN)
    italian_frequency = zipfslaw.top_word_frequencies(italian_text, 135)
    italian_data = zipfslaw.generate_zipf_data(italian_frequency)
    zipfslaw.print_data(italian_data, "italian_test.csv")


main()



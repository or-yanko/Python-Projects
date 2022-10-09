from logging import exception
from googletrans import Translator
import argparse
import os

translator = Translator()


def translate(text, src="auto", dest="en"):
    return translator.translate(text, src=src, dest=dest).text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    try:

        parser.add_argument("target", help="Text/Document to translate")
        parser.add_argument(
            "-s", "--source", help="Source language, default is Google Translate's auto detection", default="auto")
        parser.add_argument("-d", "--destination",
                            help="Destination language, default is English", default="en")

        args = parser.parse_args()
        target = args.target
        src = args.source
        dest = args.destination
    except:
        print("enter like:\n'python translate_doc.py 'Bonjour' -s fr -d en'\n'python translate_doc.py wonderland.txt --source en --destination ar'")
        exit()
    if os.path.isfile(target):
        basename = os.path.basename(target)
        dirname = os.path.dirname(target)
        try:
            filename, ext = basename.split(".")
        except:
            filename = basename
            ext = ""
        translated_text = translate(open(target).read(), src=src, dest=dest)
        open(os.path.join(dirname, f"{filename}_{dest}{f'.{ext}' if ext else ''}"), "w").write(
            translated_text)
    else:
        print(translate(target, src=src, dest=dest))

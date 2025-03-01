import sys
from PIL import ImageGrab
from surya.texify import TexifyPredictor
import clipboard as cb


def main():
    image = ImageGrab.grabclipboard()
    predictor = TexifyPredictor()

    if image is not None:
        prediction = (predictor([image]))
        latex_text = prediction[0].text

        # remove start and end of math segment to allow pasting into desmos
        latex_text = latex_text.replace('<math display="block">', "")
        latex_text = latex_text.replace('</math>', "")
        # remove bold symbols
        latex_text = latex_text.replace('\\mathbf', "")

        print(latex_text)
        cb.copy(latex_text)
    else:
        sys.exit("clipboard has no image")


if __name__ == "__main__":
    main()

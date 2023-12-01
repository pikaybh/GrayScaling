from util import Rgb2Gray


def test_run(input_file):
    Img = Rgb2Gray(input_file)
    Img.show()
    Img.save(log = True)


if __name__ == "__main__":
    test_run(input("Insert file name: "))
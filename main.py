"""The Long Roast: writes one satirical sentence to /output/entry.txt."""

import os
import shutil


LINE = "He wrote the law that will govern every algorithm in the country, then printed the bill, photographed the printout with his phone, and asked an intern to turn the photo back into a PDF."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Create the output directory first.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One line only: the whole entry is a single sentence.
        f.write(LINE)


if __name__ == "__main__":
    main()

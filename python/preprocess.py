#!/usr/bin/env python3
import sys
from pathlib import Path


class Preprocess:
    def __init__(self):
        self.this_dir = Path(__file__).resolve().parent.parent

    def rescale(self):
        pass

    def main(self):
        # return X, y, X_offset, X_scale, y_offset

        return


if __name__ == "__main__":
    sys.exit(Preprocess().main())

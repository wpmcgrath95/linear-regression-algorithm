#!/usr/bin/env python3
import sys

from linear_model import LinearModelScratch
from sklearn.linear_model import LinearRegression


class LinearRegressionScratch:
    def __init__(self):
        pass

    def sklearn_linear_reg(self):
        # use sklearn linear regression to compare results
        sklearn_lr = LinearRegression()

        return sklearn_lr

    def main(self):
        LinearModelScratch().main()


if __name__ == "__main__":
    sys.exit(LinearRegressionScratch().main())

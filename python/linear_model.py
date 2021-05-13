#!/usr/bin/env python3
import sys

from preprocess import Preprocess


class LinearModelScratch:
    """
    1. preprocess data to normalize and rescale so dataset meets assumptions
    2. fit linear model
    3. optimize linear model with loss func like LSE, gradient descent, or OLS
    4. calculate expected values and beta coefficient
    5. use ANOVA (SSE and SST)
    6. goodness of fit (R^2, correlation) and t-test/f-test and regularization
    7. residual analysis (check for multicollinearity)
    """

    def __init__(self):
        pass

    def main(self):
        Preprocess().main()


if __name__ == "__main__":
    sys.exit(LinearModelScratch().main())

# Building a Linear Regression Model from Scratch

The goal of this project is to build a linear regression model or algorithm from scratch and test it on real data. In this project, I first preprocess the data to make sure it meets certain assumptions, I then create a linear model as a base model and finally I create a linear regression model. The linear regression model fits the linear model with coefficients w = (w1,...,wn) to minimize the loss function between the observed dataset and the predicted targets using a linear approximation. This is for learning purposes only.

# Setup for developement:

- Setup a python 3.x venv (usually in `.venv`)
  - You can run `./scripts/create-venv.sh` to generate one
- `pip3 install --upgrade pip`
- Install dev requirements `pip3 install -r requirements.dev.txt`
- Install requirements `pip3 install -r requirements.txt`
- `pre-commit install`

## Update versions:

`pip-compile --output-file=requirements.dev.txt requirements.dev.in --upgrade`

# Run `pre-commit` locally:

`pre-commit run --all-files`

# Sources:

These sources helped me throughout the project.

1. [scikit-learn](https://github.com/scikit-learn/scikit-learn/blob/15a949460/sklearn/linear_model/_base.py#L391)

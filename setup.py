from setuptools import setup, find_packages

setup(
    name="mldemand",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
    ],
    description="A simple machine learning demand forecasting tool",
    author="Steven Bianco",
    author_email="stevenbianco938938@gmail.com",
    url="https://github.com/stevenbianco/ml-demand-forecast",
)

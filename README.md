# Wordle Solver

This is a NLP-adjacent project that can be used to support your daily Wordle clue guesses.  Each time you make a guess, you can add the result to "Wordle Notebook" to improve your chances at guessing the correct 5-letter word by using Wikipedia's most frequent words list.

# Step-by-Step

TODO: Add a screenshot of example right here.

## Conda environment

When setting up the project, consider using a conda environment to isolate the required packages.

1. Create new conda environment (you can also use PyCharm's interpreter settings to create your conda environment instead of using command line here)
```
conda env create --name wordle-solver
```
2. Set up jupyter for conda environment ([sauce](https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook))
```
pip install jupyter ipykernel
```
```
python -m ipykernel install --user --name wordle-solver --display-name "wordle-solver"
```

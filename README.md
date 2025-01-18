<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

create new folder in desktop then drag and drop in ide (vs studio code)

open terminal (should already be cd'd in project folder)

create a virtual environment by running: python3 -m venv .venv

activate the ve by running: source .venv/bin/activate

pip install notebook ipykernel pandas numpy gensim nltk pyLDAvis matplotlib

register ve as a jupyter kernel python -m ipykernel install --user --name .venv --display-name "Python (.venv)"

install python and juptyer code extensions from marketplace

create new file and save it as .ipynb

select the python kernel in the top right corner (button that says kernel) then select python (.venv) if not showing up restart ide

test it: select code cell and paste then run:

import sys print(sys.version) import pandas as pd print(pd.version)

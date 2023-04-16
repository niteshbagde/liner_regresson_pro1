## END TO END
# House pricing predection

### Create environment - Venv
```
conda create -p Venv python == 3.8

```

### Install necessay packages
```
pip install -r requirements.txt

```

### Setting up setup.py
*   Added necessay code for setup 
*   add details for setup parameter for setup.py
*   defined function for getting requirements.txt as list
*   exception for -e . in fuction while creating list
*   can be executed as 
```
python setup.py install
``` 
* the -e . will trigget the setup.py
```
pip install -r requirements.txt
``` 

### File and folder structure

" this can be automated "

* > src   -folder
    * > componnets  -folder
        * __init__.py
        * data_ingestion.py
        * data_transformation.py
    * > pipeline    -folder
        * __init__.py
        * training_pipeline.py
        * prediction_pipeline.py
    * __init__.py
    * .gitignore
    * README.md
    * requirements.txt
    * setup.py




### todo


### todo


### GIT commands
echo "# Linear_regression_ML_project" >> README.md
* git init
* git add .
* git commit -m "first commit"
* git branch -M main

> -----use your repo url
* git remote add origin https://github.com/niteshbagde/Linear_regression_ML_project.git       

*  git push -u origin main
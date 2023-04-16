@echo off
set "project_name=ML_Project"
set "desktop=%USERPROFILE%\Desktop"
set "project_folder=%desktop%\%project_name%"

echo Creating project folder: %project_folder%
mkdir "%project_folder%"
mkdir "%project_folder%"\logs

copy NUL "%project_folder%\__init__.py"

echo Creating data folders...
mkdir "%project_folder%\data"
mkdir "%project_folder%\data\raw"
mkdir "%project_folder%\data\processed"
mkdir "%project_folder%\data\external"
mkdir "%project_folder%\data\interim"

echo Creating sample data file...
copy NUL "%project_folder%\data\raw\data.csv"

echo Creating sample processed data file...
copy NUL "%project_folder%\data\processed\data_cleaned.csv"

echo Creating sample preprocessed data file...
copy NUL "%project_folder%\data\interim\data_preprocessed.pkl"

echo Creating models folder...
mkdir "%project_folder%\models"
copy NUL "%project_folder%\models\__init__.py"

echo Creating sample model files...
mkdir "%project_folder%\models\model_1"
echo model 1 files > "%project_folder%\models\model_1\model.txt"
copy NUL "%project_folder%\models\model_1\model.pkl"
copy NUL "%project_folder%\models\model_1\hyperparameters.txt"
copy NUL "%project_folder%\models\model_1\__init__.py"

mkdir "%project_folder%\models\model_2"
echo model 2 files > "%project_folder%\models\model_2\model.txt"
copy NUL "%project_folder%\models\model_2\model.pkl"
copy NUL "%project_folder%\models\model_2\hyperparameters.txt"
copy NUL "%project_folder%\models\model_2\__init__.py"

echo Creating notebooks folder...
mkdir "%project_folder%\notebooks"

echo Creating sample Jupyter notebooks...
copy NUL "%project_folder%\notebooks\exploratory_data_analysis.ipynb"
copy NUL "%project_folder%\notebooks\model_training.ipynb"
copy NUL "%project_folder%\notebooks\hyperparameter_tuning.ipynb"
copy NUL "%project_folder%\notebooks\model_evaluation.ipynb"
copy NUL "%project_folder%\notebooks\rough.ipynb"

echo Creating scripts folder...
mkdir "%project_folder%\scripts"

echo Creating sample Python scripts...
copy NUL "%project_folder%\scripts\__init__.py"
copy NUL "%project_folder%\scripts\utils.py"
copy NUL "%project_folder%\scripts\preprocess_data.py"
copy NUL "%project_folder%\scripts\train_model.py"
copy NUL "%project_folder%\scripts\hyperparameter_tuning.py"
copy NUL "%project_folder%\scripts\evaluate_model.py"
copy NUL "%project_folder%\app.py"
copy NUL "%project_folder%\setup.py"


echo Creating reports folder...
mkdir "%project_folder%\reports"

echo Creating sample report file...
copy NUL "%project_folder%\reports\project_report.pdf"

echo Creating README, LICENSE, and requirements files...
echo Project README > "%project_folder%\README.md"
echo Project LICENSE > "%project_folder%\LICENSE"
echo pandas > "%project_folder%\requirements.txt"

echo Project creation complete.
pause

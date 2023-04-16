import os

# Define the project directory name
project_dir = "project_name"

# Create the project directory if it doesn't exist
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

# Define the directory names
data_dir = os.path.join(project_dir, "data")
raw_dir = os.path.join(data_dir, "raw")
processed_dir = os.path.join(data_dir, "processed")
models_dir = os.path.join(project_dir, "models")
saved_models_dir = os.path.join(models_dir, "saved_models")
notebooks_dir = os.path.join(project_dir, "notebooks")
src_dir = os.path.join(project_dir, "src")
data_src_dir = os.path.join(src_dir, "data")
models_src_dir = os.path.join(src_dir, "models")
utils_src_dir = os.path.join(src_dir, "utils")
tests_dir = os.path.join(project_dir, "tests")

# Create the directories if they don't exist
for directory in [data_dir, raw_dir, processed_dir, models_dir, saved_models_dir, notebooks_dir, src_dir, data_src_dir, models_src_dir, utils_src_dir, tests_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create a README.md file
with open(os.path.join(project_dir, "README.md"), "w") as f:
    f.write("# " + project_dir)

# Create a requirements.txt file
with open(os.path.join(project_dir, "requirements.txt"), "w") as f:
    f.write("")

# Create a LICENSE file
with open(os.path.join(project_dir, "LICENSE"), "w") as f:
    f.write("")

# Create data loading and processing modules
data_loader_code = """
def load_data():
    # TODO: Implement data loading code
    pass
"""

data_processor_code = """
def preprocess_data(data):
    # TODO: Implement data preprocessing code
    pass
"""

with open(os.path.join(data_src_dir, "data_loader.py"), "w") as f:
    f.write(data_loader_code)

with open(os.path.join(data_src_dir, "data_processor.py"), "w") as f:
    f.write(data_processor_code)

# Create a model module
model_code = """
import torch.nn as nn

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        # TODO: Define the model architecture

    def forward(self, x):
        # TODO: Define the forward pass
        pass
"""

with open(os.path.join(models_src_dir, "model.py"), "w") as f:
    f.write(model_code)

# Create a configuration module
config_code = """
class Config:
    data_file = "data.csv"
    batch_size = 32
    learning_rate = 0.001
"""

with open(os.path.join(utils_src_dir, "config.py"), "w") as f:
    f.write(config_code)

# Create a logger module
logger_code = """
import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to INFO
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    return logger
"""

with open(os.path.join(utils_src_dir, "logger.py"), "w") as f:
    f.write(logger_code)

#Add a test module
test_code = """
import unittest

class Test(unittest.TestCase):
def test_dummy(self):
self.assertEqual(1, 1)

if name == 'main':
unittest.main()
"""

with open(os.path.join(tests_dir, "test.py"), "w") as f:
    f.write(test_code)

print("Project template created successfully!")
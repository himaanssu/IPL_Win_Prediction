# IPL Win Prediction

This project aims to predict the outcome of IPL matches using machine learning techniques. The project includes a Jupyter notebook for data analysis and model training, as well as a Python script for deploying the model.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)

## Overview
In this project, we use historical IPL match data to train a machine learning model that predicts the winner of a match based on various features such as team composition, match location, and player performance.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/himaanssu/ipl-win-prediction.git
    cd ipl-win-prediction
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Running the Jupyter Notebook
1. Start Jupyter Notebook:
    ```sh
    jupyter notebook
    ```

2. Open `project.ipynb` and run the cells to see the data analysis and model training process.

### Running the Python Script
1. Ensure your virtual environment is activated.

2. Run the script:
    ```sh
    python app.py
    ```

## Files
- `project.ipynb`: Jupyter notebook containing data analysis and model training.
- `app.py`: Python script for deploying the trained model.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

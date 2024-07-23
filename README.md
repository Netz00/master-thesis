![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-gray?style=for-the-badge&logo=Jupyter)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![TensorFLow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

# Master thesis

## Classification performance analysis of medical histopathology images using deep neural networks

>💡 This repository contains Jupyter Notebooks and Python scripts used during master thesis research.
- [Thesis Presentation](./etc/250_23-24_Durdov-Božo_516-2022_Master_Thesis_presentation.pdf)

### Repository structure

    .
    ├── notebooks                   # Jupyter Notebooks
    ├── etc
    │   ├── diagrams                # draw.io diagrams 
    │   ├── pseudocode              # LaTeX code for iterative algorithm
    │   └── ...
    └── README.md


### Jupyter Notebooks

1. Data_preview
   - Downloads the datasets
   - Prints the samples from each dataset
2. Data_preprocessing
   - Converting images from .tif into .png
   - Resizing images
   - Datasets merge
3. Training
   - Train and save models for model/dataset combinations
4. Testing
   - Load saved models and evaluate them
   - Store evaluation results for future analyze without loading datasets/models
   - Analyze the evaluation results
5. Iterative_v1
   - Single shared test set iterative algorithm implementation
   - Train and analyzis included

>⚠️ Each notebook uses the results of the previous ones and they need to be executed in order.


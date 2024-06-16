# Master thesis

## Classification performance analysis of medical histopathology images using deep neural networks

>💡 This repository contains Jupyter Notebooks and Python scripts used during master thesis research.


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


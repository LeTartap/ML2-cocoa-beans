# Install dependencies
Run dependencies.ipynb

# Import data and preprocess:
Data can already be found in the correct format in datasets/cocoa_diseases.
To get an idea about the data format of the labels (bounding boxes and classes) accepted by YOLO, 
take a look at preprocessing.ipynb. No need to run the commands, since the data is already created.


# cocoa_pipeline_dense.ipynb

This notebook is a basic pipeline for the dense model training. It makes use of wandb, a library
integrated with ultralytics which is useful for logging and comparing different model architectures
and training/validation results.
Furthermore, I am trying to understand what the trained model file contains and how to access its weights and layers.



# Sparsification folder


We will apply the pruning method for sparsification and, if time and knowledge allows for, quantization. I will post some resources
below where you can learn more about these methods.
PyTorch provides APIs for applying pruning and a beta for quantization.
It is important that we experiment with different architectures and compare model sizes, performance, time for training/inference.


# Resources

Object detection performance metrics: https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173
Pruning: https://www.datature.io/blog/a-comprehensive-guide-to-neural-network-model-pruning
Quantization: https://www.datature.io/blog/introducing-post-training-quantization-feature-and-mechanics-explained
YOLO11 architecture explained in more detail: https://www.youtube.com/watch?v=L9Va7Y9UT8E&ab_channel=Dr.PriyantoHidayatullah




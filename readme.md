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
This will be useful for performing sparsification on desired layers.


# Sparsification folder

I found a library which is integrated with ultralytics that applies sparsification alogrithms directly onto the 
desired layers from the model architecture, called SparseML. You specify a .yaml file with a recipe for sparsification
and include it into your training loop. However, SparseML only provides integrations with YOLOv5 and YOLOv8 :(. 
To sparsify YOLOv11 with this library, we have to modify the training loop used by YOLO's model.train() function.
In other words, we have to access the underlying implementation of YOLO in PyTorch in order to do sparsification from scratch as shown in this tutorial: https://github.com/neuralmagic/sparseml/blob/main/integrations/torchvision/tutorials/docs-torchvision-sparsify-from-scratch-resnet50-beans.ipynb .

Modifying this training loop entails: manage data loading, forward pass, loss calculation, and optimizer steps explicitly in our script.
I am doing that in customTrainingLoop.ipynb, based on this thread: https://github.com/ultralytics/ultralytics/issues/8964 .
However, I am running into an issue mentioned in the thread as well, but I cannot manage to fix it. Maybe you can have a look at it.


I am still not 100% whether this approach is feasible. I spent quite some time looking over how YOLO is implemented ( https://github.com/ultralytics/ultralytics/tree/main/ultralytics). Our modification of the training loop must not interfere with the functions provided by YOLO's train() function which does model logging, performance metrics and other necessary stuff. That would require a lot of manual work from us and we do not have the necessary knowledge to re-implement all those features. A lot of people seem to be doing custom training loops on top of YOLO, so this leads me to believe that we can do that too, without affecting the underlying implementation.
However, if we cannot manage to implement this method quickly, I propose we either look at a different way of sparsifying YOLOv11 or using YOLOv8 which is already integrated with SparseML.



# Pet-Classiffier

This project trys using a Convolution Neural Net to classify a given picture into whether it is either having a cat or a dog in it. 

The basic CNN structure is as follows: Convolution -> Pooling -> Convolution -> Pooling -> Fully Connected Layer -> Output

Convolution is the act of taking the original data, and creating feature maps from it.Pooling is down-sampling, most often in the form of "max-pooling," where we select a region, and then take the maximum value in that region, and that becomes the new value for the entire region. Fully Connected Layers are typical neural networks, where all nodes are "fully connected." The convolutional layers are not fully connected like a traditional neural network.

To download the dataset used in this project, follow the link:https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765

Once the dataset is downloaded, Run the datasetcreator script to prepare your data for training the CNN.

After that train the net by executing the net.py script.


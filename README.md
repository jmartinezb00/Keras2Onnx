
## Install
Install the package tf2onnx.
 `pip install tf2onnx`

## Keras2Onnx
Convert from a Keras model .h5 to a Barracuda model .onnx

# Conversion to .pb
 First of all we will have to convert to a .pb file, so we are going to use the script `h52pb.py`, in which we are going to introduce as the first parameter the keras model.
 
 For example:
 `>>python h52pb.py keras_model.h5`
 
 This will return us the file .pb with the name saved_model.pb in a folder called saved_model.
 
# Conversion to .onnx

 Finally we introduce the following command:
 
  `>> python -m tf2onnx.convert --opset 10 --saved-model [PATH of saved_model folder]  --output [PATH where we will store the model]\{name}.onnx`

 

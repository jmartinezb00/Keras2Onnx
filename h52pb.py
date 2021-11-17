# usage
# python convert_model_to_pb.py model_name.h5 folder/to/save/

# https://stackoverflow.com/questions/60005661/tensorflow-2-0-convert-keras-model-to-pb-file

import sys

import tensorflow as tf

pre_model = tf.keras.models.load_model(sys.argv[1])
pre_model.save("saved_model")
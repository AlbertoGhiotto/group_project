from script.model.whole_model import whole_model
from keras.layers import Input

#height = 224 #dimensions of image
#width = 224
#channel = 3

input_tensor = Input(shape=(224, 224, 3))
#input_tensor = Input(shape=(None, None, 3))

model = whole_model(input_tensor)

model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])

#model.fit( [headline_data, additional_data] , [labels, labels],epochs=50, batch_size=32)

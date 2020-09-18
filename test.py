from nets.rfb import rfb300

NUM_CLASSES = 21
input_shape = (300, 300, 3)
model = rfb300(input_shape, num_classes=NUM_CLASSES)
model.summary()
for i in range(len(model.layers)):
    print(i,model.layers[i].name)
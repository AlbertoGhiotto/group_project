from Script.Model.whole_model import whole_model
from Script.Manage_dataset.Data_generator import data_gen
from Script import prediction
from keras.layers import Input
import numpy as np
IMPORT CV2

BATCH_SIZE = 4      # Scelto da me abbastanza random, ragionevole
STRIDE = 8
NO_OF_TESTING_IMAGES = len(os.listdir(test_frame_path))


def visualize(image, pose):
  for joint in range(pose.shape[0])
    cx = pose[joint][0]
    cy = pose[joint][1]
  
    cv2.imshow('pose', image)
    cv2.circle(image,(int(cx),int(cy)),10,(255,255,255),-11)

def test(model, stride):

    test_frame_path = '../../Dataset/test_frames'
    test_gen = data_gen(test_frame_path, batch_size = BATCH_SIZE)

    predictions = model.predict_generator( test_gen, steps=(NO_OF_TESTING_IMAGES//BATCH_SIZE) )
    
    num_imgs = predictions.shape[1]
    pose_imgs = []
    for img in range(num_imgs)
        pose = prediction.argmax_predict(predictions, stride)
        pose_imgs.append(pose)

    ##### DA RICONTROLLARE

     # Plot the pose on the original image
    if show_result:
        n = os.listdir(test_frame_path)
        for i in range(num_imgs):
            image = cv2.imread(test_frame_path+'/'+n[i])/255.
            image =  cv2.resize(train_img, (DEFAULT_HEIGHT, DEFAULT_WIDTH)) 
            pose = pose_imgs[i*NUM_JOINTS:(i+1)*NUM_JOINTS-1, :] 
            visualize(image, pose)

if __name__ == '__main__':
    model = load_model('Model.h5')
    test(model, STRIDE)

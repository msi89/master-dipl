
# PYTORCH
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
import os

import face_alignment
import pickle
import dlib
import cv2


# cuda for CUDA

###############################################################################

"""use cuda if its available for my case I had cuda installed
on my local environment .........................."""

workers = 0 if os.name == 'nt' else 4

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))

mtcnn = MTCNN(
    image_size=160, margin=0, min_face_size=20,
    thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
    device=device
)

resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)
# t######## Face alignment predictor
face_alignment.FaceAlignment(
    face_alignment.LandmarksType._2D, face_detector='sfd', device='cpu')


model_path = os.path.abspath(
    "assets/faces_model/trained_faces_model.clf")


class FaceSickness():
    classifier = None

    def __init__(self) -> None:
        # Loading model

        try:
            print("Model_path :", model_path)
            with open(model_path, 'rb') as f:
                self.classifier = pickle.load(f)
                print("Loaded classifier ...................")
        except Exception as e:
            print("[ERROR]:>>> Could Not Load FaceSickNess Classifier ! \n", e)

    def analyse_face(self, filename: str) -> str:
        print("GETTING HERE ...............")
        print("PATIENT >>>>>>>>>>>>>>>>>", self.diagnose_image(filename))
        status = self.diagnose_image(filename)[0]
        return status

    def diagnose_image(self, filename: str):

        self.draw_landmarks(filename)
        def collate_fn(x): return x[0]

        dataset = datasets.ImageFolder(
            os.path.abspath("media"))

        dataset.idx_to_class = {i: c for c, i in dataset.class_to_idx.items()}
        loader = DataLoader(dataset, collate_fn=collate_fn,
                            num_workers=workers)

        aligned = []
        names = []
        for x, y in loader:
            x_aligned, prob = mtcnn(x, return_prob=True)
            if x_aligned is not None:
                print('Face detected with probability: {:8f}'.format(prob))
                aligned.append(x_aligned)
                names.append(dataset.idx_to_class[y])

        aligned = torch.stack(aligned).to(device)

        embeddings = resnet(aligned).cpu().detach().numpy()

        pred = self.classifier.predict(embeddings)
        print("PREDICT PROBA >>>>>>>>>>>>>>>>",
              self.classifier.predict_proba(embeddings))
        return pred

    def draw_landmarks(self, filename: str):

        detector = dlib.get_frontal_face_detector()

        predictor = dlib.shape_predictor(os.path.abspath(
            "assets/landmarks/shape_predictor_68_face_landmarks.dat"))

        img = cv2.imread(filename)

        # convert to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detect faces in the image
        faces_in_image = detector(img_gray, 0)

        # loop through each face in image
        for face in faces_in_image:

            # assign the facial landmarks
            landmarks = predictor(img_gray, face)

            # unpack the 68 landmark coordinates from the dlib object into a list
            landmarks_list = []
            for i in range(0, landmarks.num_parts):
                landmarks_list.append(
                    (landmarks.part(i).x, landmarks.part(i).y))

            # for each landmark, plot and write number
            for landmark_num, xy in enumerate(landmarks_list, start=1):
                cv2.circle(img, (xy[0], xy[1]), 1, (50, 205, 50), -1)
                # cv2.putText(img, str(landmark_num),(xy[0]-7,xy[1]+5),
                # cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255), 1)

        cv2.imwrite(filename, img)
        cv2.waitKey(0)

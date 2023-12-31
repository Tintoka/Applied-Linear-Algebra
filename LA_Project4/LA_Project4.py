import numpy as np
import os
from PIL import Image
from matplotlib import pyplot as plt

FOLDER = "./Dataset/"
FILES = os.listdir(FOLDER)
TEST_DIR = "./Testset/"


def load_images_train_and_test(TEST):
    test = np.asarray(Image.open(TEST)).flatten()
    train = []
    for name in FILES:
        train.append(np.asarray(Image.open(FOLDER + name)).flatten())
    train = np.array(train)
    return test, train


def normalize(test, train):
    trainMean = np.mean(train, axis = 0)
    normalized_train = train - trainMean
    normalized_test = test - trainMean

    """
    TODO : Normalize test and train and return them properly
    Hint : To calculate mean properly use two arguments version of mean numpy method (https://www.javatpoint.com/numpy-mean)
    Hint : normalize test with train mean
    """
    return normalized_test,normalized_train



def svd_function(images):

    """
    TODO : implement SVD (use np.linalg.svd) and return u,s,v
    Additional(Emtiazi) todo : implement svd without using np.linalg.svd
    """
    return np.linalg.svd(images, full_matrices = False)



def project_and_calculate_weights(img, u):

    """
    TODO : calculate element wise multiplication of img and u . (you can use numpy methods)
    """
    return np.multiply(img, u)


def predict(test, train):
    min = np.linalg.norm(test)
    iMin =  0
    for i in range(train.shape[1]):
        err = np.linalg.norm(train[:, i] - test)
        if err < min:
            min = err
            iMin = i

    """
    TODO : Find the most similar face to test among train set by calculating errors and finding the face that has minimum error
    return : index of the data that has minimum error in train dataset
    Hint : error(i) = norm(train[:,i] - test)       (you can use np.linalg.norm)
    """
    return iMin


def plot_face(tested, predicted):
    plt.subplot(1,2,1)
    plt.imshow(tested, cmap='gray')

    plt.subplot(1,2,2)
    plt.imshow(predicted, cmap='gray')
    plt.show()
    """
    TODO : Plot tested image and predicted image . It would be great if you show them next to each other
    with subplot and figures that you learned in matplotlib video in the channel.
    But you are allowed to show them one by one
    """



if __name__ == "__main__":
    true_predicts = 0
    all_predicts = 0
    for TEST_FILE in os.listdir(TEST_DIR):
        # Loading train and test
        test, train = load_images_train_and_test(TEST_DIR + TEST_FILE)

        # Normalizing train and test
        test, train = normalize(test, train)
        test = test.T
        train = train.T
        test = np.reshape(test, (test.size, 1))

        # Singular value decomposition
        u, s, v = svd_function(train)

        # Weigth for test
        w_test = project_and_calculate_weights(test, u)
        w_test = np.array(w_test, dtype='int8').flatten()

        # Weights for train set
        w_train = []
        for i in range(train.shape[1]):
            w_i = project_and_calculate_weights(np.reshape(train[:, i], (train[:, i].size, 1)), u)
            w_i = np.array(w_i, dtype='int8').flatten()
            w_train.append(w_i)
        w_train = np.array(w_train).T

        # Predict
        index_of_most_similar_face = predict(w_test, w_train)

        # Showing results
        print("Test : " + TEST_FILE)
        print(f"The predicted face is: {FILES[index_of_most_similar_face]}")
        print("\n***************************\n")

        # Calculating Accuracy
        all_predicts += 1
        if FILES[index_of_most_similar_face].split("-")[0] == TEST_FILE.split("-")[0]:
            true_predicts += 1
            # Plotting correct predictions
            plot_face(Image.open(TEST_DIR + TEST_FILE), Image.open(FOLDER + FILES[index_of_most_similar_face]))
        else:
            # Plotting wrong predictions
            plot_face(Image.open(TEST_DIR + TEST_FILE), Image.open(FOLDER + FILES[index_of_most_similar_face]))

    # Showing Accuracy
    accuracy = true_predicts / all_predicts
    print(f'Accuracy : {"{:.2f}".format(accuracy * 100)} %')


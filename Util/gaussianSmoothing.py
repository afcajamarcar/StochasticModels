########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################
import numpy as np

# Calculate the gaussian value
def calculate_gaussian(x, y, sigma):
	return (1/(2*np.pi*pow(sigma,2)))*pow(np.e,-((pow(x,2) + pow(y,2))/(2*pow(sigma,2))))

# Calculate the gaussian matrix (2*kernel + 1, 2*kernel + 1)
def make_gaussian_matrix(kernel, sigma):
    size_matrix = 2 * kernel + 1
    gaussian_matrix = np.zeros((size_matrix,size_matrix))

    # Find values for 1 Quadrant
    x = 0
    for i in reversed(range(kernel+1)):

        y = 0
        for j in range(kernel, size_matrix):
            gaussian_matrix[i][j] = calculate_gaussian(x, y, sigma)
            y += 1
        x += 1

    # Find values for 2 Quadrant
    x = 0
    for i in reversed(range(kernel+1)):
        y = 0
        for j in reversed(range(kernel+1)):
            gaussian_matrix[i][j] = calculate_gaussian(x, y, sigma)
            y += 1;
        x -= 1

    # Find values for 3 Quadrant
    x = 0
    for i in range(kernel, size_matrix):
        y = 0
        for j in reversed(range(kernel+1)):
            gaussian_matrix[i][j] = calculate_gaussian(x, y, sigma);
            y -= 1
        x -= 1

    # Find values for 4 Quadrant
    x = 0
    for i in range(kernel, size_matrix):
        y = 0
        for j in range(kernel, size_matrix):
            gaussian_matrix[i][j] = calculate_gaussian(x, y, sigma);
            y -= 1
        x += 1

    # Normalize
    normalize = 0.0;
    for i in range(size_matrix):
        for j in range(size_matrix):
            normalize += gaussian_matrix[i][j];

    for i in range(size_matrix):
        for j in range(size_matrix):
            gaussian_matrix[i][j] = gaussian_matrix[i][j] / normalize;

    return gaussian_matrix

# Make the gaussian smoothing
# https://computergraphics.stackexchange.com/questions/39/how-is-gaussian-blur-implemented
def gaussianBlur(kernel, sigma, image):
    imageBlured = np.zeros(image.shape)

    gaussianMatrix =  make_gaussian_matrix(kernel, sigma)

    for ycor in range(kernel, image.shape[0] - kernel):
        for xcor in range(kernel, image.shape[1] - kernel):
            y_blur = 0
            x_blur = 0
            value_blur = 0.0
            for tmpy in range(ycor-kernel, ycor + kernel + 1):
                for tmpx in range(xcor - kernel, xcor + kernel + 1):
                    gm = gaussianMatrix[x_blur][y_blur]
                    value_blur += gm * image[tmpy, tmpx]
                y_blur += 1
                x_blur = 0

            # print image[ycor][xcor], int(value_blur)
            imageBlured[ycor][xcor] = int(value_blur)

    return imageBlured

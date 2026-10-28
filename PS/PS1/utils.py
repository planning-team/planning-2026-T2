#!/usr/bin/python

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def normalize_image(img: np.ndarray, threshold: float = 0.1):
    """
    normalize the image to be between 0 and 1
    """
    dims = img.shape
    env = np.ones(dims)
    z = np.where(img < threshold)
    env[z] = 0.0
    return env


def plot_environment_3d(img: np.ndarray, obj: np.ndarray, state: tuple):
    """
    img: original image in 2d
    obj: is the 3d array of different configurations
    state: is the curent pose (x, y, orientation) of the object
    """
    dims = obj.shape
    dim_x = int((dims[0] - 1) / 2)
    dim_y = int((dims[1] - 1) / 2)
    merged_img = np.copy(img)
    merged_img[state[0] - dim_x:state[0] + dim_x + 1, state[1] - dim_y:state[1] + dim_y + 1] += obj[:, :, state[2]] * 0.5
    return merged_img


def plot_environment_2d(img: np.ndarray, state: tuple):
    """
    img: original image in 2d
    state: is the current pose (x, y) of the point object
    """
    merged_img = np.copy(img)
    merged_img[state[0], state[1]] += 0.5 
    return merged_img

def plotting_results_3d(environment: np.ndarray, rod: np.ndarray, plan: list, save_path: str = 'rod_solve.gif'):
    """
    create an animation of the plan and save it to a file

    @param environment: the environment image in 2d
    @param rod: is the 3d array of different configuration
    @param plan: list of poses
    @param save_path: path to save the animation
    """

    fig = plt.figure()
    imgs = []

    for s in plan:
        im = plot_environment_3d(environment, rod, s)
        plot = plt.imshow(im)
        imgs.append([plot])

    ani = animation.ArtistAnimation(fig, imgs, interval=50, blit=True)

    ani.save(save_path)

    plt.show()

def plotting_results_2d(environment: np.ndarray, plan: list, save_path: str = 'point_solve.gif'):
    """
    create an animation of the plan and save it to a file

    @param environment: the environment image in 2d
    @param plan: list of poses (x, y)
    @param save_path: path to save the animation
    """

    fig = plt.figure()
    imgs = []

    for s in plan:
        im = plot_environment_2d(environment, s)
        plot = plt.imshow(im)
        imgs.append([plot])

    ani = animation.ArtistAnimation(fig, imgs, interval=50, blit=True)

    ani.save(save_path)

    plt.show()

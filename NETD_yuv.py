import os
import numpy as np

import os
import numpy as np

from read_pgm_file import get_data
import inquirer


def avg_20():
    avgimg_20 = 0
    files = ['./datasets/yuv/20/' + folder for folder in os.listdir('./datasets/yuv/20/')]
    for index, value in enumerate(files):
        #print(files[index])
        image = np.memmap(files[index], dtype='float16', mode='r+').reshape(240, 320)
        avgimg_20 = image + avgimg_20
    print(avgimg_20)
    avgimg_20 = avgimg_20 / len(files)

    return avgimg_20


def avg_25(resolution):
    avgimg_25 = 0
    files = os.listdir('./datasets/yuv/25/')
    for index, value in enumerate(files):
        image = np.memmap('./datasets/yuv/25/' + files[index], dtype='uint16', mode='r').reshape(480, 648)
        avgimg_25 = image + avgimg_25
    avgimg_25 = avgimg_25 / 60.0
    print('Averaged 25')

    std_var = np.std(avgimg_25)
    std_var = std_var
    return std_var


def avg_30(resolution):
    avgimg_30 = 0
    files = os.listdir('./datasets/yuv/30/')
    for index, value in enumerate(files):
        image = np.memmap('./datasets/yuv/30/' + files[index], dtype='uint16', mode='r').reshape(480, 648)
        avgimg_30 = image + avgimg_30
    avgimg_30 = avgimg_30 / 60.0
    print('Averaged 30')
    return avgimg_30


def compute_NETD(avg20, stdvar_25, avg30):
    responsivity = (avg30 - avg20) / 10
    print('\nResposivity =', np.average(responsivity))
    print('Temporal noise =', stdvar_25)
    netd = stdvar_25 / np.average(responsivity)
    netd = netd * 1000
    print('\nNETD value =', netd, 'mK')


def main():
    print('Knight NETD test.\n')
    questions = [
        inquirer.List('RESOLUTION', message="Enter resolution", choices=['VGA(Gen2)', 'QVGA(Atto)'])
    ]
    answers = inquirer.prompt(questions)

    sensor = answers['RESOLUTION']
    if sensor == 'VGA(Gen2)':
        columns_to_read = [0, 640]
    else:
        columns_to_read = [0, 320]

    return columns_to_read


if __name__ == '__main__':
    avg_20()
    """resolution = main()
    avg20 = avg_20(resolution)
    stdvar_25 = avg_25(resolution)
    avg30 = avg_30(resolution)
    compute_NETD(avg20, stdvar_25, avg30)
"""

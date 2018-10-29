import os
import numpy as np

import inquirer


def avg_20(resolution):
    avgimg_20 = 0
    files = os.listdir('./datasets/20/')
    for index, value in enumerate(files):
        image = np.memmap('./datasets/20' + '/' + value, dtype='uint16', mode='r').reshape(resolution)
        avgimg_20 = image + avgimg_20
        avgimg_20 = avgimg_20.astype('uint32')

    avgimg_20 = avgimg_20 / 60.0

    print('Averaged 20', avgimg_20)
    return avgimg_20


def avg_25(resolution):
    avgimg_25 = 0
    files = os.listdir('./datasets/25/')
    for index, value in enumerate(files):
        image = np.memmap('./datasets/25' + '/' + value, dtype='uint16', mode='r').reshape(resolution)
        avgimg_25 = image + avgimg_25
        avgimg_25 = avgimg_25.astype('uint32')

    avgimg_25 = avgimg_25 / 60.0
    print('Averaged 25', avgimg_25)

    std_var = np.std(avgimg_25)
    std_var = std_var
    return std_var


def avg_30(resolution):
    avgimg_30 = 0
    files = os.listdir('./datasets/30/')
    for index, value in enumerate(files):
        image = np.memmap('./datasets/30' + '/' + value, dtype='uint16', mode='r').reshape(resolution)
        avgimg_30 = image + avgimg_30
        avgimg_30 = avgimg_30.astype('uint32')

    avgimg_30 = avgimg_30 / 60.0
    print('Averaged 30', avgimg_30)
    return avgimg_30


def compute_NETD(avg20, stdvar_25, avg30):
    responsivity = (avg30 - avg20) / 10
    print('\nResposivity =', np.average(responsivity))
    print('Temporal noise =', stdvar_25)
    netd = stdvar_25 / np.average(responsivity)
    netd = np.abs(netd * 1000)
    print('\nNETD value =', netd, 'mK')


def main():
    print('Knight NETD test.\n')
    questions = [
        inquirer.List('RESOLUTION', message="Enter resolution", choices=['VGA(Gen2)', 'QVGA(Atto)'])
    ]
    answers = inquirer.prompt(questions)

    sensor = answers['RESOLUTION']
    if sensor == 'VGA(Gen2)':
        columns_to_read = [480, 640]
    else:
        columns_to_read = [240, 320]

    return columns_to_read


if __name__ == '__main__':
    resolution = main()
    avg20 = avg_20(resolution)
    stdvar_25 = avg_25(resolution)
    avg30 = avg_30(resolution)
    compute_NETD(avg20, stdvar_25, avg30)

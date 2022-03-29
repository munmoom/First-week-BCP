{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPVC44FRTPH7MXfLeQm+puK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/1-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WQM-U5XhuBQU",
        "outputId": "d4a596ff-d863-4cc5-a690-384f0e1a94dd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "리히터 규모: 3.5\n",
            "가끔 느껴지고 미약한 피해가 발생한다(창문 흔들리고 물건 떨어짐)\n"
          ]
        }
      ],
      "source": [
        "scale = float(input('리히터 규모: '))\n",
        "\n",
        "if scale < 3.5 :\n",
        " print('사람이 거의 느끼지 못하지만 기록된다.')\n",
        "elif scale <= 5.4 :\n",
        " print('가끔 느껴지고 미약한 피해가 발생한다(창문 흔들리고 물건 떨어짐)')\n",
        "elif 5.5 <= scale <= 6.0 :\n",
        " print('건물에 약간의 손상이 온다.(벽균열, 서있기 곤란)')\n",
        "elif 6.1 <= scale <= 6.9 :\n",
        " print('사람이 사는 곳이 파괴될 수 있다.(가옥 30%이하 파괴)')\n",
        "elif 7.0 <= scale <= 7.9 :\n",
        " print('큰 피해를 야기한다(가옥 전파, 교량 파괴, 산사태, 지각 균열)')\n",
        "elif 8.0 <= scale :\n",
        " print('거대한 지진으로 모든 마을이 파괴된다.')"
      ]
    }
  ]
}
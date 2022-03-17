{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOyTswq8u3D4TXWJrZiradJ",
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IVluJwxwFSni",
        "outputId": "5d199457-f838-410a-9c83-55d5a4e782cc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "34\n",
            "섭씨 34.0도는 화씨 93.20도이다.\n"
          ]
        }
      ],
      "source": [
        "C = float(input())\n",
        "F = C*(9/5) + 32\n",
        "print(f'섭씨 {C:2.1f}도는 화씨 {F:2.2f}도이다.')"
      ]
    }
  ]
}
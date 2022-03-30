{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "4-202255127.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM83/ReYumymNlwwRXsan1c",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/4_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "id": "DiRRMfa2yule",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "285eeec2-7793-46c7-9b31-3358af0dfe6d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "2\n"
          ]
        }
      ],
      "source": [
        "t = int(input())\n",
        "n = 1\n",
        "list=[]\n",
        "for p in range(1, t+1):\n",
        " n*=p\n",
        " list.append(n)\n",
        "\n",
        "test = list[-1]\n",
        "test = int(test)\n",
        "while test%10 == 0:\n",
        " test=test//10\n",
        "test = str(test) \n",
        "print(test[-1])"
      ]
    }
  ]
}
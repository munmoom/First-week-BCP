{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled7.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNcSCQWnzI9nUp1lEJ6UidT",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/4-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0JBApkldVZlB",
        "outputId": "b51ada7c-d34b-40e7-a7c5-0952da4e6655"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "472 385\n",
            "2360\n",
            "3776 \n",
            "1416  \n",
            "181720\n"
          ]
        }
      ],
      "source": [
        "a, b = input().split()\n",
        "c = int(b[2])*int(a)\n",
        "d = int(b[1])*int(a)\n",
        "e = int(b[0])*int(a)\n",
        "f = int(a)*int(b)\n",
        "print(c)\n",
        "print(str(d)+' ')\n",
        "print(str(e)+'  ')\n",
        "print(f)"
      ]
    }
  ]
}
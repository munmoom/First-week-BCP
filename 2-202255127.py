{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyN9qhcyjsTX37yqdvqHIq4U",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mNeMbFMXJEUx",
        "outputId": "18f776ba-87dd-43e5-b2d7-ef0e6fe5bac3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "넓이는 28.26이고, 원주는 18.84이다.\n"
          ]
        }
      ],
      "source": [
        "r = float(input())\n",
        "S = 3.14*(r**2)\n",
        "l = 2*3.14*r\n",
        "print(f'넓이는 {S:2.2f}이고, 원주는 {l:2.2f}이다.')"
      ]
    }
  ]
}
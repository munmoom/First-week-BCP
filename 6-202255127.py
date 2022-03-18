{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled10.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP7IpWC+8HgCZi4Zw+zGNYe",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/6-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W7tAcNYlzPqF",
        "outputId": "c2a08a62-0927-421a-91c7-2172af0a3ff0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "123456789-홍길동\n",
            "12345678홍길동\n"
          ]
        }
      ],
      "source": [
        "a = input()\n",
        "b = a[:8]\n",
        "c = a[10:]\n",
        "print(b+c)"
      ]
    }
  ]
}
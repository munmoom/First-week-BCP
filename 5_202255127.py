{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "5-202255127.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyODahSdchem3/MnATipgLHa",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/5_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.lib.display import IFrame\n",
        "t = int(input())\n",
        "n = 1\n",
        "list=[]\n",
        "for p in range(1, t+1):\n",
        " n*=p\n",
        " list.append(n)\n",
        "\n",
        "test = list[-1]\n",
        "test = str(test) \n",
        "\n",
        "new = []\n",
        "for a in test:\n",
        "  new.append(a)\n",
        "\n",
        "while '0' in new:\n",
        "  new.remove('0')\n",
        "\n",
        "new = new[-5:]\n",
        "\n",
        "new = ''. join(new)\n",
        "print(new)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gxAOsSmE94Er",
        "outputId": "abcd8189-e5df-4e3a-f431-ab2bd21d3c9f"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "17664\n"
          ]
        }
      ]
    }
  ]
}
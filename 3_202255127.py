{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "3-202255127.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNufbnGU1HHpvGeH36tcoV0",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/3_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "o3VB5jGbyZko"
      },
      "outputs": [],
      "source": [
        "on = int(input())\n",
        "tw = int(input())\n",
        "th = int(input())\n",
        "fo = int(input())\n",
        "fi = int(input())\n",
        "si = int(input())\n",
        "se = int(input())\n",
        "ei = int(input())\n",
        "ni = int(input())\n",
        "te = int(input())\n",
        "\n",
        "a = on+tw+th+fo+fi+si+se+ei+ni+te\n",
        "b = on+tw+th+fo+fi+si+se+ei+ni\n",
        "c = on+tw+th+fo+fi+si+se+ei\n",
        "d = on+tw+th+fo+fi+si+se\n",
        "e = on+tw+th+fo+fi+si\n",
        "f = on+tw+th+fo+fi\n",
        "g = on+tw+th+fo\n",
        "h = on+tw+th\n",
        "i = on+tw\n",
        "j = on\n",
        "\n",
        "\n",
        "score = [a, b, c, d, e, f, g, h, i, j]\n",
        "\n",
        "for k in score:\n",
        " if 100-k < 0 :\n",
        "  x = int(-(100-k))\n",
        " else:\n",
        "  y = int(100-k)\n",
        "  if x == y:\n",
        "   print(x)\n",
        "  else:\n",
        "   if x < y:\n",
        "    print(x+100)\n",
        "   elif y < x:\n",
        "    print(100-y)\n",
        "\n"
      ]
    }
  ]
}
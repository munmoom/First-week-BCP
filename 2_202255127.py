{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMaFc3kD92bZgYalWz6XOby",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/First-week-BCP/blob/main/2_202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 0\n",
        "for i in range(1,1000):\n",
        " if a == 100:\n",
        "  break\n",
        " else:\n",
        "  for n in range(2,i+1):\n",
        "   if n==i:\n",
        "    a = a + 1\n",
        "    print(i, end=' ')\n",
        "   elif i%n==0:\n",
        "    break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hjHWHKvqSGeS",
        "outputId": "c82a40e6-f484-43cb-aedd-a2ab291c50f2"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 "
          ]
        }
      ]
    }
  ]
}
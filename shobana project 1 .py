{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04c2c3f8",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input the radius of the circle : 1.1\n",
      "The area of the circle with radius 1.1 is: 3.8013271108436504\n"
     ]
    }
   ],
   "source": [
    "from math import pi\n",
    "r = float(input (\"Input the radius of the circle : \"))\n",
    "print (\"The area of the circle with radius \" + str(r) + \" is: \" + str(pi * r**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3d886d53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input the Filename: abc.py\n",
      "The extension of the file is : 'py'\n"
     ]
    }
   ],
   "source": [
    "filename = input(\"Input the Filename: \")\n",
    "f_extns = filename.split(\".\")\n",
    "print (\"The extension of the file is : \" + repr(f_extns[-1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e042a0ea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

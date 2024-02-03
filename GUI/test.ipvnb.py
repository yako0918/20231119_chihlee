{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "url = 'https://blynk.cloud/external/api/get?token=MOPYimQu2tyQj136eu3jLO01iDMIeuOR&v0&v1'\n",
    "\n",
    "response = requests.request(\"GET\",url)\n",
    "if response.status_code == 200:\n",
    "    all_data = response.json()\n",
    "    print(type(all_data['v0']))\n",
    "    print(type(all_data['v1']))\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
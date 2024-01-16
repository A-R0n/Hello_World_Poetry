# Hello World Poetry

## Description
This is a machine learning project where we build a Convolutional Neural Network (CNN)
using ~20,000 images of dogs (with their breeds). After we build our model, we can pass in images of dogs we know and allow it to guess the breed! 

### What's the Poetry part?
Poetry is an open source tool python developers use for their really large projects to help resolve versioning conflicts,
so you can easily manage and reproduce the project on another machine.

### Why are we using Poetry?
 - Idexx is a company that uses it.
 - In this project, we have many dependencies: keras, tensorflow, opencv-python, sklearn, numpy, pandas, numpy, and matplotlib. And as our project grows, so might the number of these dependencies! We're also using it because the lock file gives us performance gains.

 ## How we do get our data?
 - 1) Prereq: Download [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) then create your env >>> `conda env create -f environment.yml`
 - 2) Create an account with [Kaggle](https://www.kaggle.com/)
 - 3) Generate a security token [Create New Token](https://www.kaggle.com/settings)
 - 4) (On MacOS) move the token from Downloads folder to kaggle folder >>> `mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json`
 - 5) (On MacOS) ensure you have read access for the token >>> `sudo chmod 600 ~/.kaggle/kaggle.json`
 - 6) Run the following command from your terminal in the root of your project >>> `kaggle competitions download -c dog-breed-identification`

 Congratulations! You now have over 20,000 images of 120 different dogs 🤓
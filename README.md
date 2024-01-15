# Hello World Poetry

## Description
This is a machine learning project where we build a Convolutional Neural Network (CNN)
using ~20,000 images of dogs (with their breeds). After we build our model, we can reconstruct it to make predictions with images of dogs we know
and test its accuracy.

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
 - 4) Run the following command from your terminal in the root of your project >>> `kaggle competitions download -c dog-breed-identification`.

 Congratulations! You now have over 20,000 images of 120 different dogs 🤓
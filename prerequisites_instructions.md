# Prerequisites instructions

To install the necessary libraries, [pip](https://pip.pypa.io/en/stable/installation/) (package management system) must be previously installed. The installation must be done from the console:

1. Install Pillow (PIL)
Pillow is a powerful image processing library that BlissfulBadgeInspector relies on. To install Pillow, run the following command in your terminal:
> pip install pillow

2. Install scikit-learn (sklearn)
Scikit-learn is a machine learning library used in BlissfulBadgeInspector. Install it using the following command:
> pip install scikit-learn

3. Install NumPy
NumPy is a fundamental package for scientific computing in Python and is essential for BlissfulBadgeInspector. Install it with:
> pip install numpy

4. Verify Installations
After installing the required packages, verify that everything is set up correctly by running the following commands:
> python -c "import PIL; print(PIL._\_version__)"
> 
> python -c "import sklearn; print(sklearn._\_version__)"
> 
> python -c "import numpy; print(numpy._\_version__)"

These commands should print the versions of Pillow, scikit-learn, and NumPy, respectively.

Once you've completed these steps, you should have a working environment for running BlissfulBadgeInspector. If you encounter any issues, refer to the documentation for each library or seek help from the respective community forums.

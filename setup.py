from setuptools import setup

with open("/home/behzad/Desktop/Office/paper-generalizability-window-size/README.md", 'r') as f:
    long_description = f.read()

setup(
    name='paper-generalizability-window-size',
    version='1.0',
    description='scripts',
    license="Concordia University",
    long_description=long_description,
    author='',
    author_email='',
    REQUIRES_PYTHON='>=3.4.0',

    REQUIRED=['numpy', 'pandas', 'sklearn', 'matplotlib'],  # external packages as dependencies
    scripts=[
        'Scripts/Classification.py',
        'Scripts/plot_figures.py',
        'Scripts/plot_results.py',
        'Scripts/Preprocessing.py'
    ]
)
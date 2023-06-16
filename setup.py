from setuptools import setup, find_packages

setup(
    name='language_model_analysis',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'streamlit',
        'matplotlib',
        'torch',
        'sentencepiece',
        'transformers',
        'plotly'
    ],
    entry_points={
        'console_scripts': [
            'streamlit run app.py'
        ]
    }
)

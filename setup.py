"""
Setup
"""
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='contextual-ai',
    version='0.0.1',
    packages=setuptools.find_packages(include=['xai*'], exclude=['tutorials*', 'docs*', 'tests*']),
    author="SAP",
    url="https://github.com/sap-staging/contextual-ai",
    description="Contextual AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'xai': 'xai'},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['numpy==1.18.2',
                      'pandas==0.25.1',
                      'scikit-learn==0.22.2',
                      'scipy==1.3.1',
                      'tqdm==4.44.1',
                      'matplotlib==3.1.1',
                      'seaborn==0.9.0',
                      'fpdf==1.7.2',
                      'wordcloud==1.5.0',
                      'nltk==3.4.5',
                      'ordered-set==3.1',
                      'lime>=0.1.1.32',
                      'dill==0.3.0',
                      'shap>=0.35.0',
                      'yattag==1.12.2',
                      'pyyaml==5.3.1',
                      'pillow==7.0.0',
                      'jsonschema==3.0.2',
                      'PyPDF2 == 1.26.0'
                      ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: Apache Software License'
    ]
)


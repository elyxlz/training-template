from setuptools import setup, find_packages

setup(
    name="xxx",
    version="0.0.1",
    author="xxx",
    author_email="xxx",
    description="xxx",
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url="xxx",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires=">=3.9",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "python-dotenv",
    ],
    extras_require={"train": ["accelerate", "wandb", "tqdm"]},
    license="MIT",
)

from setuptools import setup, find_packages

# Package metadata
name = 'skillshare-backup'
version = '1.0.1'
author = 'Uriel Albarran Oropeza'
author_email = 'hello@ozonostudio.com'
description = 'Script to download classes videos to view offline'
with open("README.md", "r", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()
license = 'MIT'  # or any other license you choose

# Package dependencies
install_requires = [
    'requests',
    'tqdm',
    'telethon',
    'python-slugify',
    'ffmpeg-python',
]

# Setup configuration
setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=["python", "skillshare", "download", "downloader", "dl"],
    source="https://github.com/ozonostudio/skillshare",
    download_url="https://github.com/ozonostudio/skillshare/releases",
    documentation="https://github.com/ozonostudio/skillshare/wiki",
    license=license,
    packages=find_packages(),
    install_requires=install_requires,
    zip_safe=False,
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'down = down:main',
            'skillshare-download = down:main',
        ],
    },
)

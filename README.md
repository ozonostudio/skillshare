# YOU REQUIRE A SUBSCRIPTION, THIS CODE DOESN'T DOWNLOAD VIDEOS FOR PEOPLE WITHOUT AN ACTIVE SUBSCRIPTION ON SKILLSHARE

## Skillshare Downloader
A Python script to download Skillshare videos from a course by simply providing the course link.

This script now backup the videos on .mkv with subtitles and it's capable to upload the files to Telegram on .mp4 (without subtitles)

## Requirements
To use this script, you need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Installation
1. Clone or download this repository to your local machine.
```bash
  git clone https://github.com/ozonostudio/skillshare.git

```
2. Install all the dependencies using pip
```bash
  cd /[skillshare_folder_location]
  pip install -r requirements.txt

```

3. Run the script by typing python (this can change depending on your python version, ex: python3) down.py -h and pressing Enter.
```bash
  python down.py -h

```

4. The script will display a help screen with the steps to follow.

5. All the downloaded files are stored on ./downloads

## Usage

The script now comes with resolution and subtitles language option.
To download the files locally you can use only:
```bash
  python down.py 1749908541

```
By default the video it's going to be downloaded with subtitles on English at 854x480, to change the subtitles language and resolution you can use something like:
```bash
  python down.py -s es-MX -r 1920x1080 1749908541

```
If you want to backup your courses to Telegram I recommend you to create a group with topics because the script it's going to create individual topics per course with all the videos inside
```bash
  python down.py -s es-MX -r 1920x1080 1749908541 -t @yourgroup

```
You also can use
```bash
  python down.py -s es-MX -r 1920x1080 1749908541 -t https://t.me/+XXXxxxXXXX

```
The files are going to be downloaded locally and uploaded to Telegram after each file it's downloaded, but if you want to remove the file after upload, you can use
```bash
  python down.py -s es-MX -r 1920x1080 1749908541 -t -e @yourgroup

```


## License
This project is licensed under the MIT License.

## Acknowledgments
This project was inspired by the need to download Skillshare videos for offline viewing.
# YOU REQUIRE A SUBSCRIPTION, THIS CODE DOESN'T DOWNLOAD VIDEOS FOR PEOPLE WITHOUT AN ACTIVE SUBSCRIPTION ON SKILLSHARE

## Skillshare Downloader
A Python script to download Skillshare videos from a course by simply providing the course link.

This script now backup the videos on .mkv with subtitles and it's capable to upload the files to Telegram on .mp4 (without subtitles)

## Requirements
To use this script, you need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Installation
1. Clone or download this repository to your local machine.
```bash
  git clone https://github.com/ozonostudio/skillshare.git

```
2. Install all the dependencies using pip
```bash
  cd /[skillshare_folder_location]
  pip install -r requirements.txt

```

3. Run the script by typing python (this can change depending on your python version, ex: python3) down.py -h and pressing Enter.
```bash
  python down.py -h

```

4. The script will display a help screen with the steps to follow.

5. All the downloaded files are stored on ./downloads

## Usage

The script now comes with resolution and subtitles language option.
To download the files locally you can use only:
```bash
  python down.py 1749908541

```
By default the video it's going to be downloaded with subtitles on English at 854x480, to change the subtitles language and resolution you can use something like:
```bash
  python down.py -s es-MX -r 1920x1080 1749908541

```
If you want to backup your courses to Telegram I recommend you to create a group with topics because the script it's going to create individual topics per course with all the videos inside
```bash
  python down.py -s es-MX -r 1920x1080 1749908541 -t @yourgroup

```
You also can use
```bash
  python down.py -s es-MX -r 1920x1080 1749908541 -t https://t.me/+XXXxxxXXXX

```
The files are going to be downloaded locally and uploaded to Telegram after each file it's downloaded, but if you want to remove the file after upload, you can use
```bash
  python down.py -s es-MX -r 1920x1080 1749908541 -t -e @yourgroup

```


## License
This project is licensed under the MIT License.

## Acknowledgments
This project was inspired by the need to download Skillshare videos for offline viewing.

## Support
If you find this useful and want to support me please make a donation to any of this links: <br />
https://ko-fi.com/polygoncollectibles <br />
https://www.buymeacoffee.com/polygoncollect <br />
https://www.patreon.com/polygoncollectibles <br />
https://www.paypal.me/polygoncollect <br />
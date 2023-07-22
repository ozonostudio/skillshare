# YOU REQUIRE A SUBSCRIPTION, THIS CODE DOESN'T DOWNLOAD VIDEOS FOR PEOPLE WITHOUT AN ACTIVE SUBSCRIPTION ON SKILLSHARE

## Skillshare Downloader
A Python script to download Skillshare videos from a course by simply providing the course ID.

This script now backup the videos on .mkv with subtitles and it's capable to upload the files to Telegram on .mp4 (without subtitles)

## Requirements
To use this script, you need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Installation
1. Install using PIP.
```bash
  pip install skillshare-downloader

```

2. Once installed you can start with the configuration using
```bash
  $ cd /[folder_for_files_download]/
  down -config

```

3. Open skillshare.com on Chrome and using the inspection window.
4. Go to network and select the Doc Filter.
5. Press the first document and inside the headers copy all the Cookies from the Request Headers.
6. Paste the cookies into a file cookies.txt and save it just in case you want to configure Telegram later.
7. Now drag and drop cookies.txt into your terminal window and press Enter.
8. If you don't want configurate Telegram now, just ENTER without text on the api, hash and phone prompts.

## Usage

first enter on the folder location you want to download all the videos
```bash
  $ cd /[folder_for_files_download]/

```

The script now comes with resolution and subtitles language option.
To download the files locally with the default configuration (en-US at 854x480) you can use:
```bash
  $ down 1749908541

```
By default the video it's going to be downloaded with subtitles on English at 854x480, to change the subtitles language and resolution you can use something like:
```bash
  $ down -s es-MX -r 1920x1080 1749908541

```
If you want to backup your courses to Telegram I recommend you to create a group with topics because the script it's going to create individual topics per course with all the videos inside (Subtitles are not need since Telegram don't support subtitles yet)
```bash
  $ down -r 1920x1080 1749908541 -t @yourgroup

```
You also can use
```bash
  $ down -r 1920x1080 1749908541 -t https://t.me/+XXXxxxXXXX

```
The files are going to be downloaded locally and uploaded to Telegram after each file it's downloaded, but if you want to remove the file after upload, you can use [-e]
```bash
  $ down -r 1920x1080 1749908541 -t -e @yourgroup

```
### UPDATE ---------
- Added automatic resume download
- Added automatic resume uploads to Telegram on the same Topic
- If the choosed resolution doesn't exist the script look for the next lower resolution
- If the subtitles doesn't exist, now download the default en-US subtitles to avoid error

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
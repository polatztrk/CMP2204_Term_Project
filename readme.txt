# Chunked File Transfer - User Guide

This guide explains how to use the Chunked File Transfer project to upload and download files in a chunked manner. The project provides scripts for both the upload and download sides.

## Table of Contents

- [Upload Side](#upload-side)
  - [Prerequisites](#prerequisites)
  - [Uploading a File](#uploading-a-file)
- [Download Side](#download-side)
  - [Prerequisites](#prerequisites-1)
  - [Downloading a File](#downloading-a-file)
- [File Structure](#file-structure)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Upload Side

### Prerequisites

Before using the upload side of the Chunked File Transfer project, ensure you have the following:

- The file you want to upload, placed in the "data" folder.
- Python installed on your computer.
- Knowledge of your broadcast IP range for setting up the `chunk_announcer.py`.

### Uploading a File

1. Open the "upload" folder.

2. Add the file that you want to upload to the "data" folder.

3. Open `chunk_announcer.py` and set your broadcast IP range.

4. Go to the "upload" folder from the terminal.

5. Open `POM_chunk_uploader.py` in the terminal and set your IP.

6. Run `POM_chunk_announcer.py` in the terminal. Enter the file name you want to divide into 5 chunks and announce.

7. Run `chunk_uploader.py` in the terminal.

## Download Side

### Prerequisites

Before using the download side of the Chunked File Transfer project, ensure you have the following:

- Python installed on your computer.

### Downloading a File

1. Go to the "download" folder from the terminal.

2. Run `POM_chunk_discovery.py` in the terminal to discover the file chunks that you can download.

3. Run `POM_chunk_downloader.py` and enter the file name that you want to download.

4. After completing these processes, you will find the file chunks in the "chunks" folder on the download side, and the downloaded file will be located inside the "data" folder.

## File Structure

- "upload" folder: Contains scripts and files for the upload side.
- "download" folder: Contains scripts and files for the download side.
- "data" folder: Where the files to be uploaded are placed.
- "chunks" folder: Where downloaded file chunks are stored.
- "upload_log.txt": Log file for the upload side.
- "download_log.txt": Log file for the download side.

## Logging

Log texts for both the upload and download sides can be found in "upload_log.txt" and "download_log.txt" respectively.

## Contributing

Contributions to this project are welcome. If you have improvements, bug fixes, or additional features to add, please feel free to open an issue or create a pull request.


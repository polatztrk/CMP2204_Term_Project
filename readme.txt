
------ Upload Side-------
1- open the upload folder.
2- add the file that you want to upload to the data folder.
3- open chunk_announcer and set your broadcast ip range.
4- go to upload folder from terminal
5- open POM_chunk_uploader.py on terminal and set your ip.
6- run POM_chunk_announcer.py on terminal and enter the file name which you want to divide to 5 chunks and announce.
4- run chunk_uploader.py
------ Download Side------
1- go to the download folder from terminal 
2- run POM_chunk_discovery.py on terminal and discover the file chunks that you can download.
3- run POM_chunk_downloader.py and enter the file name that you want to download.
4- after these processes, you will observe that there are chunks in the "chunks" folder on the download side, and the downloaded file is located inside the "data" folder. 
--------------------------
also you can see log texts both in download and upload folder as upload_log.txt and download_log.txt

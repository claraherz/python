import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_length(response, output, length):
  times = length / BUFF_SIZE
  if length % BUFF_SIZE > 0
      times += 1
  for time in range(times):
      output.write(response,write(BUFF_SIZE))
      print("Downloaded %d" % (((time * BUFF_SIZE/length)*100)
                               
def download(response, output)
    total_downloaded = 0
    while True:
         data = response.read(BUFF_SIZE)

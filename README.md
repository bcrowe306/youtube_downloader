# Youtube Download
---

A utility python script that downloads videos from Youtube. I simply got tired of relying on shady online downloaders, full of malware, everytime I need to download content from youtube for editing. This script is the answer.

It is marked as executable, so all that needs to happen is launch main.py in the terminal, followed by the youtube watch link in double quotes.

```bash
./main.py "https://www.youtube.com/watch?v=CK_OY_gZrCE"
```

If the link is valid, it will give you a list of available stream resolutions. Choose the one you want by index, and the script will download the video and place it into the current user's download folder.

depends on Python3 and:
```
pytube
```

## Installation
Clone the repository, navigate to the directory in terminal. Install the dependencies using pip 

```
python3 -m pip install -r ./requirements.txt
```


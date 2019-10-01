# ReviewCrawler
Reviews of Google Play crawler

# How to use

1. Install Chrome

2. pip install -r requirements.txt

3. **Run "main.py"**

4. Review will be printed.


# Arguments
usage:
```
python3 main.py [--skip true] [--threads 4] [--google true] [--naver true] [--full false] [--face false]
```

```
--skip true        Skips keyword if downloaded directory already exists. This is needed when re-downloading.

--threads 4        Number of threads to download.

--google true      Download from google.com (boolean)

--naver true       Download from naver.com (boolean)

--full false       Download full resolution image instead of thumbnails (slow)

--face false       Face search mode


```

# Customize

You can make your own crawler by changing collect_links.py

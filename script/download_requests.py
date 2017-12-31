from tqdm import tqdm
import requests
import os.path


def download(url, filename, override=False):
    if override or not os.path.exists(filename):
        r = requests.get(url, stream=True)

        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))

        with open(filename, 'wb') as f:
            for data in tqdm(r.iter_content(32 * 1024), total=total_size, unit='B', unit_scale=True):
                f.write(data)
    else:
        print('{} already downloaded.'.format(filename))


if __name__ == "__main__":
    download(
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1494837554&di=2b9d5cc7fb57e9b7f7fd02792db5566f&imgtype=jpg&er=1&src=http%3A%2F%2Fwww.ysg88.com%2FUploadFiles%2FFCK%2F2014-08%2F201408110V06J8L4J4.jpg",
        "test.jpg", True)

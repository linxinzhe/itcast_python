from urllib.request import urlretrieve
import os.path
from tqdm import tqdm


class DLProgress(tqdm):
    last_block = 0

    def hook(self, block_num=1, block_size=1, total_size=None):
        self.total = total_size
        self.update((block_num - self.last_block) * block_size)
        self.last_block = block_num


def download(url, filename, override=False):
    if override or not os.path.exists(filename):
        with DLProgress(unit='B', unit_scale=True, miniters=1, desc='downloading {}'.format(filename)) as pbar:
            urlretrieve(
                url,
                filename,
                pbar.hook)
    else:
        print('{} already downloaded.'.format(filename))


if __name__ == "__main__":
    download("http://httpbin.org/", "test.txt", True)

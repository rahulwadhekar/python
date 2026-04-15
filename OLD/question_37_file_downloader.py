class DiskFullError(Exception):
    pass


class HTTPDownloader:
    def download(self, size, space):
        try:
            if space < size:
                raise DiskFullError
            print("HTTP: Download successful")
        except DiskFullError:
            print("HTTP: Not enough disk space")


class FTPDownloader:
    def download(self, size, space):
        try:
            if space < size:
                raise DiskFullError
            print("FTP: Download successful")
        except DiskFullError:
            print("FTP: Not enough disk space")


downloads = [(HTTPDownloader(), 50, 100), (FTPDownloader(), 200, 100)]

for d, size, space in downloads:
    d.download(size, space)
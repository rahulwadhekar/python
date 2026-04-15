class PaperJamError(Exception):
    pass


class LaserPrinter:
    def print_document(self, pages):
        try:
            if pages > 500:
                raise PaperJamError
            print("LaserPrinter: Fast printing")
        except PaperJamError:
            print("LaserPrinter: Paper jam detected!")


class InkjetPrinter:
    def print_document(self, pages):
        try:
            if pages > 500:
                raise PaperJamError
            print("InkjetPrinter: Slow printing")
        except PaperJamError:
            print("InkjetPrinter: Paper jam detected!")


printers = [(LaserPrinter(), 100), (InkjetPrinter(), 600)]

for printer, pages in printers:
    printer.print_document(pages)
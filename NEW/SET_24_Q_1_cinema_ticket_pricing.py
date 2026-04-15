class PaperJamError(Exception):
    pass


class Printer:
    def print_document(self, pages):
        pass


class LaserPrinter(Printer):
    def print_document(self, pages):
        if pages > 500:
            raise PaperJamError
        print("Laser Printer: Fast printing")


class InkjetPrinter(Printer):
    def print_document(self, pages):
        if pages > 500:
            raise PaperJamError
        print("Inkjet Printer: Slow printing")


try:
    p = LaserPrinter()
    p.print_document(600)

except PaperJamError:
    print("Paper jam! Printing paused")
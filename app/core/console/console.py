class Console:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def success(self, message):
        print(f"{self.OKGREEN}{message}{self.ENDC}")

    def heading(self, message):
        print(f"{self.HEADER}{message}{self.ENDC}")

    def info(self, message):
        print(f"{self.OKBLUE}{message}{self.ENDC}")

    def warn(self, message):
        print(f"{self.WARNING}{message}{self.ENDC}")

    def error(self, message):
        print(f"{self.FAIL}{message}{self.ENDC}")

    def bold(self, message):
        print(f"{self.BOLD}{message}{self.ENDC}")

    def underline(self, message):
        print(f"{self.UNDERLINE}{message}{self.ENDC}")
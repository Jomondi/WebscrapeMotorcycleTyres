class AspectRatio:
    def __init__(self):
        self.ratio = None
        self.TIRE_WIDTH = None
        self.TIRE_ASPECT_RATIO = None
        self.select_aspect_ratio()

    def select_aspect_ratio(self):
        self.ratio = True
        self.TIRE_WIDTH = input("Enter a tire width from these values [60, 70, 80, 90, 100, 110, 120, 130, 140, "
                                "150, 160, 170, 180, 190, 200, 210, 230, 240, 250, 260, 280, 300, 330]: ")

        if int(self.TIRE_WIDTH) == 60:
            ASPECT_RATIO = [70, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 70:
            ASPECT_RATIO = [90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 80:
            ASPECT_RATIO = [80, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 90:
            ASPECT_RATIO = [80, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False
        elif int(self.TIRE_WIDTH) == 100:
            ASPECT_RATIO = [80, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 110:
            ASPECT_RATIO = [70, 80, 85, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 120:
            ASPECT_RATIO = [50, 55, 60, 65, 70, 80, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 130:
            ASPECT_RATIO = [60, 70, 80, 90, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 140:
            ASPECT_RATIO = [60, 70, 75, 80, 85, 90]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 150:
            ASPECT_RATIO = [60, 65, 70, 80, 90]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 160:
            ASPECT_RATIO = [60, 70, 80]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 170:
            ASPECT_RATIO = [60, 70, 80, 100]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 180:
            ASPECT_RATIO = [55, 60, 65, 70, 80]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 190:
            ASPECT_RATIO = [50, 55, 60]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 200:
            ASPECT_RATIO = [30, 50, 55, 60, 70]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 210:
            ASPECT_RATIO = [40]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 230:
            ASPECT_RATIO = [60]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 240:
            ASPECT_RATIO = [40, 45, 50, 55]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 250:
            ASPECT_RATIO = [40]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 260:
            ASPECT_RATIO = [40]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 280:
            ASPECT_RATIO = [35]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 300:
            ASPECT_RATIO = [35]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

        elif int(self.TIRE_WIDTH) == 330:
            ASPECT_RATIO = [30]
            self.TIRE_ASPECT_RATIO = input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: ")
            while self.ratio:
                if int(self.TIRE_ASPECT_RATIO) not in ASPECT_RATIO:
                    print("You entered an incorrect value. Select a value from the stated list")
                    self.TIRE_ASPECT_RATIO = int(input(f"Enter a tire aspect ratio from these values {ASPECT_RATIO}: "))
                else:
                    self.ratio = False

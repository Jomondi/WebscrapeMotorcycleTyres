from tire_aspect_ratio import AspectRatio

aspect_ratio = AspectRatio()


class RimSize:
    def __init__(self):
        self.rim = None
        self.TIRE_RIM_SIZE = None
        self.select_rim_size()

    def select_rim_size(self):
        self.rim = True

        if int(aspect_ratio.TIRE_WIDTH) == 60 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 70:
            RIM_SIZE = [16]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 60 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 60 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [10, 12, 14, 15, 16, 17, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 70 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [14, 17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 70 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [10, 14, 16, 17, 18, 19, 21]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 80 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [14, 16]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 80 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [10, 14, 16, 17, 21]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 80 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [8, 10, 12, 14, 16, 17, 18, 19, 21, 23]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 90 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [14, 16, 17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 90 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [8, 10, 12, 14, 16, 18, 19, 21]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 90 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [10, 12, 14, 18, 19, 21]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 100 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [10, 14, 16, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 100 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [10, 12, 14, 16, 17, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 100 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [8, 10, 17, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 110 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 70:
            RIM_SIZE = [11, 12, 13, 16, 17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 110 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [10, 14, 16, 17, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 110 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 85:
            RIM_SIZE = [18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 110 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [12, 13, 16, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 100 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [12, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 50:
            RIM_SIZE = [26]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 55:
            RIM_SIZE = [26]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 65:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 70:
            RIM_SIZE = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [12, 14, 16, 17, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [10, 16, 17, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 120 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [16, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 130 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [13, 16, 17, 19, 21, 23]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 130 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 70:
            RIM_SIZE = 10, 11, [12, 13, 16, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 130 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [12, 15, 16, 17, 18, 19]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 130 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 90:
            RIM_SIZE = [10, 15, 16, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 130 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 100:
            RIM_SIZE = [16, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 170 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 180 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 55:
            RIM_SIZE = [17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 180 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [16, 17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 180 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 65:
            RIM_SIZE = [16]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 180 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 70:
            RIM_SIZE = [15, 16]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 180 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 80:
            RIM_SIZE = [14]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 190 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 50:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 190 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 55:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 190 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 200 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 30:
            RIM_SIZE = [23]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 200 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 50:
            RIM_SIZE = [17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 200 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 55:
            RIM_SIZE = [16, 17, 18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 200 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [16, 17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 200 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 70:
            RIM_SIZE = [15]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 210 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 40:
            RIM_SIZE = [18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 230 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 60:
            RIM_SIZE = [15]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 240 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 40:
            RIM_SIZE = [18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 240 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 45:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 240 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 50:
            RIM_SIZE = [26]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 240 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 55:
            RIM_SIZE = [16]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 250 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 40:
            RIM_SIZE = [18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 260 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 40:
            RIM_SIZE = [18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 280 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 35:
            RIM_SIZE = [18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 300 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 35:
            RIM_SIZE = [18]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

        elif int(aspect_ratio.TIRE_WIDTH) == 330 and int(aspect_ratio.TIRE_ASPECT_RATIO) == 30:
            RIM_SIZE = [17]
            self.TIRE_RIM_SIZE = input(f"Enter a tire width from these values {RIM_SIZE}: ")
            while self.rim:
                if int(self.TIRE_RIM_SIZE) not in RIM_SIZE:
                    print("You entered the incorrect tire rim size!")
                    self.TIRE_RIM_SIZE = int(input(f"Enter a tire width from these values {RIM_SIZE}: "))
                else:
                    self.rim = False

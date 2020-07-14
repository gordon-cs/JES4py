class Sample:
    def __init__(self, sound, index):
        self.sound = sound
        self.index = index

    def __str__(self):
        try:
            s = "Sample at {} with value {}".format(self.index, self.getValue())
        except:
            s = "Sample at {} with value {} value unknown".format(self.index)
        return s

    def __repr__(self):
        return self.__str__()

    def getSound(self):
        """Method to get this sample's sound object

        Returns
        -------
        Sound
           the sound object
        """
        return self.sound

    def getValue(self):
        """Method to get the sample value

        Returns
        -------
        int
            the sample's value
        """
        return self.sound.getSampleValueAt(self.index)

    def setValue(self, newValue):
        """Method to set the sample value

        Parameters
        ----------
        newValue : int or float
            the new value to store
        """
        self.sound.setSampleValueAt(self.index, int(newValue))

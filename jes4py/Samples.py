from jes4py.Sample import Sample

class Samples:
    def __init__(self, sound):
        self.sound = sound
        self.samples = []
        for i in range(sound.getLength()):
            self.samples.append(Sample(sound, i))

    def __str__(self):
        """Obtains a string representation of this array of Samples

        Returns
        -------
        str
            string representation of this array of Samples
        """
        return "Samples, length {}".format(self.sound.getLength())

    def __retr__(self):
        return self.__str__()

    @classmethod
    def getSamples(cls, sound):
        """Method to get the array of samples from a sound

        Parameters
        ----------
        sound : Sound
            the sound

        Returns
        -------
        list of Sample
            the array of samples
        """
        samples = []
        for i in range(sound.getLength()):
            samples.append(Sample(sound, i))
        return samples

    def getSample(self, index):
        """Method to get a specific Sample

        Parameters
        ----------
        index : int
            the index to get the sample from

        Returns
        -------
        Sample
            the sample at the given index
        """
        return self.samples[index]

    def setSample(self, index, value):
        """Method to set the value of a specific Sample

        Parameters
        ----------
        index : int
           the index to get the sample
        value : int or float
            the value to set it to
        """
        self.samples[index].setValue(value)

    def getSound(self):
        """Method to get these Samples' sound object

        Returns
        -------
        Sound
            the sound object
        """
        return self.sound

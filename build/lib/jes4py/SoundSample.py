from jes4py import Config

class SoundSample:
    """Provides access to frames (samples) within a Sound

    Attributes
    ----------
    wrapLevels : bool
        Indicates whether levels outside the range 0-255 are clamped
        or wrapped around (saturating or modular arithmetic).
        False to clamp levels, true to modulo them.
    """

    wrapLevels = False

    def __init__(self, sound, frameNumber):
        """Constructor

        Parameters
        ----------
        sound : Sound
            sound the frame (sample) belongs to
        frameNumber : int
            index of frame (sample)
        """
        self.wrapLevels = Config.getConfigVal("CONFIG_WRAPPIXELVALUES")
        self.sound = sound
        self.frameNumber = frameNumber

    def __str__(self):
        """Return string with sound sample meta information

        Returns
        -------
        str
            user-readable sound sample information
        """
        return "Sample at index {} has value {}".format(self.frameNumber, self.getValue())

    def __repr__(self):
        """Return string representation of sound sample

        Returns
        -------
        str
            string of sound sample
             contents
        """
        return self.__str__()

    @classmethod
    def correctLevel(cls, level):
        """Map sound level to [-32768,32767] according to wrapLevel setting

        Parameters
        ----------
        level : float
            nonnegative integer representing a color value

        Returns
        -------
        int
            corrected color level
        """
        level = int(level)
        if cls.wrapLevel:
            if level < 0:
                return -1*((-1*level) % 32768)
            elif level > 0:
                return level % 32768
        elif level < -32768:
            return 0
        elif level > 32767:
            return 32767
        return level

    @classmethod
    def setWrapLevels(cls, wrap):
        """Round and correct a sound level to be within (-32768, 32767)

        Parameters
        ----------
        wrap : bool
            True to enable level wrapping, False for level truncation
        """
        cls.wrapLevels = wrap

    @classmethod
    def getWrapLevels(cls):
        """Return current setting of wrap level

        Indicates whether levels outside the range (-32768, 32767) are
        clamped or wrapped around (saturating or modular arithmetic).

        Returns
        -------
        bool
            True means levels are wrapped, False means levels are truncated
        """
        return cls.wrapLevels

    def getValue(self):
        value = 0
        try:
            value = self.sound.getSampleValue(self.frameNumber)
        except:
            pass
        return value
    
    def setValue(self, value):
        try:
            self.sound.setSampleValue(self.frameNumber, value)
        except:
            pass

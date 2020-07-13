# /**
#  * Class that represents a sound.  This class is used by the students
#  * to extend the capabilities of SimpleSound.
#  * <br>
#  * Copyright Georgia Institute of Technology 2004
#  * @author Barbara Ericson ericson@cc.gatech.edu
#  *
#  * Modified 17 July 2007 Pam Cutter Kalamazoo College
#  *    Added a copySoundInto method which allows copying as much of
#  *     this sound as will fit into a destination sound
#  *    Added a cropSound method which returns a new sound which is a
#  *     specified portion of this sound
#  *
#  * Kalamazoo and other additional methods merged by Buck Scharfnorth 22 May 2008
#  */
import Sound

class Sound:

    # /**
    #  * Constructor that takes a file name
    #  * @param fileName the name of the file to read the sound from
    #  */
    def __init__(self, arg=None):
        if isinstance(arg, None):
            # arg is a Picture
            self.image = arg.image.copy()
            self.extension = arg.extension
            self.filename = arg.filename
            self.title = arg.title
        elif isinstance(arg, PIL.Image.Image):
            # arg is a PIL image
            self.image = arg
            self.extension = extension
            try:
                self.filename = self.title = arg.filename
            except AttributeError:
                self.filename = self.title = ''
        elif isinstance(arg, str):
            # arg is a string, do what JES does and make picture of string
            self.image = PIL.Image.new("RGB", (600, 200))
            self.extension = extension
            self.title = arg
            self.filename = ''
            draw = PIL.ImageDraw.Draw(self.image)
            draw.text((0, 100), arg)
        else:
            # arg is not None or not recogized; create empty Picture
            self.image = None
            self.extension = extension
            self.filename = self.title = ''

    # ////////////////// methods ////////////////////////////////////

    # /**
    #  * Method to return the string representation of this sound
    #  * @return a string with information about this sound
    #  */
    def __str__(self):
        output = "Sound"
        fileName = getFileName()

        # // if there is a file name then add that to the output
        if (fileName != ""):
            output = output + " file: " + fileName

        # // add the length in frames
        output = output + " number of samples: " + getLengthInFrames()

        return output

    def getFileName(self):
        """Return sound file name

        Returns
        -------
        string
            name of file containing sound data
        """
        return self.fileName

    # /**
    #  * Method to copy as much of this sound as will fit into
    #  * another sound.
    #  * @param dest the sound which gets copied into
    #  * @param startIndex the starting index for copying
    #  */
    def copySoundInto(self, dest, startIndex):
        numSamplesToCopy = Math.min(this.getLength(), dest.getLength() - startIndex)

        for (int i = 0; i < numSamplesToCopy; i++) {
            int value = this.getSampleValueAt(i);
            dest.setSampleValueAt(i + startIndex, value);

        }
    }

    # /**
    #  * Method to crop out a portion of this sound and return it
    #  * as a new sound
    #  * @param startIndex the index at which to start cropping
    #  * @param numSamples the number of samples to crop out
    #  * @return the new sound derived from this sound by cropping
    #  * @throws SoundException
    #  */
    public Sound cropSound(int startIndex, int numSamples) throws SoundException {
        int numSamplesToCopy;
        if (startIndex + numSamples < this.getLength()) {
            numSamplesToCopy = startIndex + numSamples;
        } else {
            numSamplesToCopy = this.getLength() - startIndex;
        }
        Sound newSound = new Sound(numSamplesToCopy);

        for (int i = 0; i < numSamplesToCopy; i++) {
            int value = this.getSampleValueAt(i + startIndex);
            newSound.setSampleValueAt(i, value);
        }
        return newSound;
    }
} // end of class Sound, put all new methods before this
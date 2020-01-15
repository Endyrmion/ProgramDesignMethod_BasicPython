# 5. Write a program that calculates the wavelength of a wave traveling at a constant velocity given the speed and the frequency.
# Use the formula lambda = v/f, where lambda is wavelength in meters, v is velocity in meters per second, and f is frequency in Hertz (cycles per second).
# Print the velocity, frequency, and wavelength. Assign each of these values to a variable and use the variables in your print() statements.
# The following demonstrates what the program prints:
# The speed (m/s): 343 The frequency (Hz): 256 The wavelength (m): 1.33984375


def waveLengthCalc(velocity, frequency):
    return velocity / frequency


try:
    velo = int(input("Velocity:\n--> "))
    freq = int(input("Frenquency:\n--> "))


except:
    print("Wrong input.")
    exit()

print("Wavelength is %fm" % waveLengthCalc(velo, freq))

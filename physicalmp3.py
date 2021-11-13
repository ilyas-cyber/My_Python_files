from pygame import mixer
# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("physicalactivities.mp3")

# Setting the volume
mixer.music.set_volume(0.7)
# Start playing the song
mixer.music.play(-1)

# infinite loop
print("Type Done to Exit:")
query = input(" ")

if query == 'Done':
        # Stop the mixer
        mixer.music.stop()


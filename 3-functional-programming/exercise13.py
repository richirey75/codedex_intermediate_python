# In this lecture I learn about transformations of data
# Transformations of data are operations that change the structure or representation of data.
# Three common transformations of data are:
# 1. Map: Applies a function to each element in a collection and returns a new collection with the results. 
# 2. Filter: Selects elements from a collection based on a condition and returns a new collection with the selected elements.
# 3. Reduce: Combines elements in a collection into a single value using a function.

from functools import reduce

playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
  return song[1] > 5.00

def minutes_to_seconds(song):
  duration = song[1]
  minutes = int(duration)
  seconds = (duration - minutes) * 100

  return minutes * 60 + round(seconds)

def add_total_time(total, song):
  duration = song[1]
  return total + duration

long_songs = list(filter(longer_than_five_minutes, playlist))
songs_seconds = list(map(minutes_to_seconds, playlist))
playlist_duration = reduce(add_total_time, playlist, 0)

print(long_songs)
print(songs_seconds)
print(playlist_duration)




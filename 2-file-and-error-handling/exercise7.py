# In this lecture I learn about the file realm
# The three modes are:
# 'r' - read
# 'w' - write
# 'a' - append

'''
file = open('example.txt', 'r')

content = file.read()

print('Using read():')
print(content)

line1 = file.readline()  # Read the first line
print(line1, end='')     # Printing the first line

line2 = file.readline()  # Read the second line
print(line2, end='')     # Printing the second line

file.close()

'''
liked_songs = {
  'Bad Habits': 'Ed Sheeran',
  'I\'m Just Ken': 'Ryan Gosling',
  'Mastermind': 'Taylor Swift',
  'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
  'Ghost': 'Justin Bieber'
}


def write_liked_songs_to_file(songs, file_name):
  with open(file_name, 'w') as file:
    file.write('Liked songs: \n')
    for song, artist in songs.items(): # songs is  the key and artist is the value, I did not know this, so keep in mind
      file.write(f'{song} by {artist}\n')
  print(f"Successfully added Liked songs to {file_name} ❤️")


write_liked_songs_to_file(liked_songs, 'liked_songs.txt')








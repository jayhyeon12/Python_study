'''
Song class 정의
- 인스턴스 변수: 노래 제목, 장르

singer class 정의
- 인스턴스 변수: 가수 이름, 대표곡

출력 결과
가수 이름: 
노래 제목: 
'''

class Song:
  def set_song(self, title, genre):
    self.title = title
    self.genre = genre
  
  def print_song(self):
    print(f'노래 제목: {self.title}({self.genre})')

class Singer:
  def set_singer(self, name):
    self.name = name
  
  def hit_song(self, song):
    self.song = song
  
  def print_singer(self):
    print(f'가수 이름: {self.name}')
    song.print_song()

song = Song()
song.set_song('home', '락')
# print(song.title)
# print(song.genre)

singer = Singer()
singer.set_singer('피아')
singer.hit_song(song)

singer.print_singer()
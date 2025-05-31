from unittest import TestCase

import classes
import samples
import functions

# Unittests for all the functions from functions.py
class Test(TestCase):
    def test_find_song_1(self):
        expected = functions.find_song('song_not_in_samples')
        actual = None
        self.assertEqual(expected,actual)
    def test_find_song_2(self):
        expected = functions.find_song('Hello').album
        actual = '25'
        self.assertEqual(expected, actual)

    def test_rate_song_1(self):
        print('Respond to the following with a number less than 5 and greater than 0. Then respond with "y"')
        expected = functions.rate_song(samples.songs[1])
        actual = classes.Song.avg_ratings(samples.songs[1])
        self.assertEqual(expected,actual)
    def test_rate_song_2(self):
        print('Respond to the following with a number less than 5 and greater than 0 (not the same as prev test). Then respond with "y"')
        expected = functions.rate_song(samples.songs[0])
        actual = classes.Song.avg_ratings(samples.songs[1])
        self.assertNotEqual(expected,actual)

    def test_get_attribute_1(self):
        expected = functions.get_attribute(samples.songs[0],'genre')
        actual = 'Pop'
        self.assertEqual(expected,actual)
    def test_get_attribute_2(self):
        expected = functions.get_attribute(samples.songs[0],'album')
        actual = '7/27'
        self.assertEqual(expected,actual)

    def test_sorted_songs_1(self):
        print('Input "title" when responding to the following')
        x = samples.songs[0]
        y = samples.songs[1]
        sample = [x,y]
        actual = [y,x]
        functions.sorted_songs(sample)
        self.assertEqual(sample,actual)
    def test_sorted_songs_2(self):
        print('Input "title" when responding to the following')
        x = samples.songs[0]
        y = samples.songs[1]
        sample = [x,y]
        actual = [x,y]
        functions.sorted_songs(sample)
        self.assertNotEqual(sample,actual)




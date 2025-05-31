from unittest import TestCase
import classes
from samples import songs

# Unittests for all the functions within the classes
class TestSong(TestCase):
    def test_add_rating(self):
        song = classes.Song("Work From Home", "Fifth Harmony,Ty Dolla $ign", "7/27", classes.Duration(3, 44), "Pop", 2)
        song.add_rating(3)
        x=song.ratings
        actual = [3]
        self.assertEqual(x,actual)

    def test_add_rating2(self):
        song = classes.Song("Work From Home", "Fifth Harmony,Ty Dolla $ign", "7/27", classes.Duration(3, 44), "Pop", 2)
        song.add_rating(7)
        x=song.ratings
        actual = []
        self.assertEqual(x,actual)

    def test_avg_ratings(self):
        song = classes.Song("Work From Home", "Fifth Harmony,Ty Dolla $ign", "7/27", classes.Duration(3, 44), "Pop", 2)
        r=song.avg_ratings()
        self.assertEqual(None,r)

    def test_avg_ratings2(self):
        song = classes.Song("Work From Home", "Fifth Harmony,Ty Dolla $ign", "7/27", classes.Duration(3, 44), "Pop", 2)
        song.add_rating(4)
        r=song.avg_ratings()
        self.assertEqual(4,r)
class TestDuration(TestCase):
    pass


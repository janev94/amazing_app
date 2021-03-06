from django.db import models
from django.contrib.auth.models import User


class Maze(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rows = models.IntegerField()
    cols = models.IntegerField()
    cells = models.TextField()
    solved_by = models.ManyToManyField(User, related_name="Solved by")
    attempts = models.IntegerField(default = 0)
    creator = models.ForeignKey(User, related_name="Built by")
    solved = models.BooleanField(default=False)
    likes = models.IntegerField(default = 0)
    liked_by = models.ManyToManyField(User, related_name="Liked by")
    __grid = None


    def getOrCreateGrid(self):
        print self.cells, len(self.cells)
        if self.rows*self.cols > len(self.cells):
            self.cells = []
            return self.cells
        if(self.__grid):
            return self.__grid

        cells = [str(x) for x in self.cells if x == "1" or x == "0"] # remove peski unicode
        grid = []
        index = 0
        for i in xrange(self.rows):
            row = []
            for j in xrange(self.cols):
                row += cells[index]
                index += 1
            grid += [row]
        self.__grid = grid
        return grid


    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    mazes_created = models.IntegerField(default=0)
    mazes_solved = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username


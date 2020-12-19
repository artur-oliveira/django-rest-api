from django.db import models

'''
Profile: id, name, email, address { street, suite, city, zipcode } ;
Comment: id, name, email, body, postId;
Post: id, title, body, userId.
'''


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    street = models.CharField(max_length=300)
    suite = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.email

    def __repr__(self):
        return self.__str__()

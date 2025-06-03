from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=30)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    profile_picture = models.ImageField(
        upload_to='feedback_pics/',
        blank=True,  # Makes the field optional
        null=True
    )
    
    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        return '/static/images/default_avatar.jpg'  # Path to your default
    
    def __str__(self):
        return self.User_name

    

class BookTable(models.Model):
    Name = models.CharField(max_length=50)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return f"{self.Name} | {self.Email} | {self.Booking_date}" 


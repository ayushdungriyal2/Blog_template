# import here 
from django.db import models
from autoslug import AutoSlugField
import os
from django.core.validators import FileExtensionValidator

# import end 

# function to rename image 
def image_directory_path(instance, filename):
    # delete if author.png exist 
    try :
        os.remove("blog/static/images/Author.png")
    except :
        pass
    # end delete if author.png exist 
    ext = filename.split('.')[-1]
    return 'blog/static/images/{}.{}'.format('Author', ext)
    # end function to rename image 


# website info 
class WebsiteInfo(models.Model):
    WebsiteName = models.CharField(max_length=50000, default="")
    BlogAuthorImage = models.ImageField(max_length=250, upload_to=image_directory_path, null=True, blank=True, validators=[FileExtensionValidator('PNG')])
    BlogAuthorName = models.CharField(max_length=250,  default="")
    BlogAuthorDesc = models.CharField(max_length=250,  default="")
# end website info 


# Category
class Category(models.Model):
    Name = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.Name
# end Category


# SinlgeBlogInfo 
class SinlgeBlogInfo(models.Model):

    Category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    BlogMetaDescription = models.CharField(max_length=50000, default="")
    BlogImageURL = models.URLField(max_length=50000, default="")
    BlogH1 = models.CharField(max_length=50000, default="")
    BlogH1P = models.TextField(max_length=5000000, default="")
    BlogH2 = models.CharField(max_length=50000, default="")
    BlogH2P = models.TextField(max_length=5000000, default="")
    BlogH3 = models.CharField(max_length=50000, default="")
    BlogH3P = models.TextField(max_length=5000000, default="")
    BlogH4 = models.CharField(max_length=50000, default="")
    BlogH4P = models.TextField(max_length=5000000, default="")
    BlogH5 = models.CharField(max_length=50000, default="")
    BlogH5P = models.TextField(max_length=5000000, default="")
    Slug = AutoSlugField(populate_from='BlogH1',unique=True, null=True, default="")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.BlogH1

# end SinlgeBlogInfo 




        
from django.db import models
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
# Create your models here.

'''define table with star name and its relationships in the cards'''
#validators allow for constraints in the data entry, everything else can be seen used in Django documentation

class Star(models.Model):
	name = models.CharField(max_length=100, unique = True, verbose_name = "Star Name")
	finished = models.BooleanField(default= "True", verbose_name = "Unfinished Card", help_text = "Uncheck if the card information has been completely filled and the card is finished")

	class Meta:
		verbose_name_plural = " Stars" #the space bypasses the default Django Admin alphabetical order without having to directly change the base Admin site
			
	def __str__(self):
		return self.name

class ReferenceURL(models.Model):
	URL = models.URLField(help_text=" Link to the ADS reference search, and perform a search on the reference. Click the link to the corresponding paper and copy the URL of said paper: <br> <a href='http://adsabs.harvard.edu/abstract_service.html' target='_blank'>LINK TO ADS SEARCH. </a> </br> A typical link should look like this: http://adsabs.harvard.edu/abs/1970IBVS..456....1P",\
	verbose_name= "Online Reference", validators=[RegexValidator(regex='http://', message='The complete link must be added. Make sure it contains http://. Follow the example in the help text.', code='nomatch')], blank = True, null = True) 
    #the model above includes a help text with html that let's you link to ADS

	class Meta:
		verbose_name = "Online Reference"
		verbose_name_plural = "Online References"
		
	name = models.ForeignKey(Star,default=1, related_name = 'ADSURL')

	def __str__(self):
		return self.URL

class References(models.Model):
	Ref = models.CharField(max_length = 300, verbose_name = 'Reference', help_text = "Write down any references that were not available in ADS, just as they appear on the card.", blank = True)
	name =  models.ForeignKey(Star, default = 1, related_name = 'REF')
	class Meta:
		verbose_name = 'Reference'
		verbose_name_plural = 'References'
	def __str__(self):
		return self.Ref

    
class ScanImage(models.Model):
    name = models.ForeignKey(Star,default=1,null=True,blank = True, related_name = 'images')
    image = models.ImageField(upload_to='scannedimages/',unique=True)
    format = models.BooleanField(default = "True", verbose_name = "Follows Original Format", help_text = "Uncheck if card doesn't contain a star name")
    def thumbnail(self):
        return mark_safe('<img src="http://0.0.0.0:8000/media/%s" width="383" height="225">' % (self.image)) #the data entry process will be hosted locally at Villanova University and the URL is only for a thumbnail to be available in the admin website during the data entry process
    thumbnail.short_description = 'Thumbnail'
    
    def __str__(self):
        return str(self.image)
	#has a foreign key and saves to folder 'scans/'
    class Meta:
        verbose_name_plural = "Scanned Images"
		
class UnnamedCards(models.Model):
    description = models.TextField(help_text = "Describe the nature of the card, and any relevant information that can be communicated about it. Be concise but thorough.")
    image = models.OneToOneField(ScanImage,default=1)
    class Meta:
        verbose_name = "Cards without a star name"
        verbose_name_plural = "Cards without a star name"    
    def __str__(self):
        return self.description
		
class Aliases(models.Model):
	name = models.ForeignKey(Star,default=1, related_name= 'ali')
	aliases = models.CharField(max_length = 200, default = 1)
#this can be set to read only since it updates automatically with the astroquery signal program
	class Meta:
		verbose_name = "alias"
		verbose_name_plural = "aliases"

	def __str__(self):
		return self.aliases

class RA(models.Model):
	name = models.OneToOneField(Star,default = 1, related_name = "RA")
	#Ra = models.CharField(max_length = 14, help_text=("<h4> <i> e.g. if the RA is 1 hour, 44 minutes, and 38 seconds, input the RA in this manner: <b> 01 h 44 m 38 s </b> DON'T FORGET THE 0s FOR ONE DIGIT INPUTS AND SPACES BETWEEN UNITS. </i> </h4>"), verbose_name = "RA", unique = True, validators=[RegexValidator(regex='^.{14}$', message='Length has to be 14, read help text under field.', code='nomatch')])
	hours = models.CharField(max_length = 2, verbose_name = "Hours", validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2, include a 0 digit before a one digit number.', code='nomatch')])
	minutes = models.CharField(max_length = 2, verbose_name = "Minutes", validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2, include a 0 digit before a one digit number.', code='nomatch')])
	seconds = models.CharField(max_length = 2, verbose_name = "Seconds", validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2, include a 0 digit before a one digit number.', code='nomatch')])
	#the hours minutes seconds format makes it easier to output the data on the dynamic html website later on
	def __str__(self):
		return self.hours

class DEC(models.Model):
	name = models.OneToOneField(Star,default = 1, related_name = "DEC")
	#Dec = models.CharField(max_length = 12, help_text=("<h4> <i> e.g if the DEC is +3 degrees, and 48.6 arc-minutes, input the DEC in this manner: <b> +03 d 48.6 m </b> DON'T FORGET THE 0s FOR ONE DIGIT INPUTS AND SPACES BETWEEN UNITS. </i> <h4>"), verbose_name = "DEC", unique = True, validators=[RegexValidator(regex='^.{12}$', message='Length has to be 12, read help text under field.', code='nomatch')])
	degrees =  models.CharField(max_length = 3, verbose_name = "Degrees", validators=[RegexValidator(regex='^.{3}$', message='Length has to be 3, include + or - sign, and a 0 digit before a one digit number.', code='nomatch')])
	arcminutes = models.CharField(max_length = 2, verbose_name = "Arcminutes", validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2, include a 0 digit before a one digit number.', code='nomatch')])
	arcseconds = models.CharField(max_length = 2, verbose_name = "Arcseconds", validators=[RegexValidator(regex='^.{2}$', message='Length has to be 2, include a 0 digit before a one digit number.', code='nomatch')])
	#the chosem format makes it easier to output the data on the dynamic html website later on
	def __str__(self):
		return self.degrees

class Epoch(models.Model):
	epoch = models.IntegerField(null = True, blank = True, help_text=("<h4> Use this field if your RA and DEC have a specified epoch such as 1900 or '55 which would be 1955, if more than one RA and DEC are provided, use the one with an explicitly specified epoch. </h4>"))
	name = models.OneToOneField(Star, default = 1, related_name = 'ep')
	def __str__(self):
		return str(self.epoch)


class GalacticCoordinate(models.Model):
	lam = models.CharField(max_length = 7, verbose_name = "Lambda", help_text= "<h4> <i> e.g if lambda is 9.2 degrees, write 09.2 </i> </h4>", validators=[RegexValidator(regex='^.{4}$', message='Length has to be 4, read help text under field.', code='nomatch')], blank = True)
	beta = models.CharField(max_length = 7, help_text = "<h4> <i> e.g if beta is +3.6 degrees, write +03.6 </i> </h4>", verbose_name = "Beta", validators=[RegexValidator(regex='^.{5}$', message='Length has to be 5, read help text under field.', code='nomatch')], blank = True)
	name = models.OneToOneField(Star, default = 1, related_name = 'gc')
	def __str__(self):
		return self.lam
		
class Annotation(models.Model):
	annotations = models.CharField(max_length = 200, verbose_name = "Card-Specific Annotations", blank = True)
	name = models.ForeignKey(Star, default = 1, related_name = 'ann')
	class Meta:
		verbose_name = "annotation"
		verbose_name_plural = "annotations"
	def __str__(self):
		return self.annotations
	
from .signals import perform_and_save_query
#this connects the astroquery signal and runs it upon saving of a new item
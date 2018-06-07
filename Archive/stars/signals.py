#create signals to run scripts

from astroquery.simbad import Simbad
from .models import Aliases, ReferenceURL, RA, DEC, Star
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

@receiver(post_save, sender=Star) #makes a receiver connection

#below, a signal called perform_and_save_query is defined. The signal is received 
#post_save aka every time something is saved. This signal makes sure that every time 
#a kwargs (keyword argument) is created, the script will run. the kwargs is name from 
#the model Star. That kwargs is then taken as a variable, in the line x = 
#kwargs['instance'], and that variable is used to run the astroquery search, which then 
#loops the results in a save. Line listA = ... is a decoding for the array which was 
#a byte array

def perform_and_save_query(sender, **kwargs):
    if kwargs.get('created', False):
        Star.objects.get_or_create(name=kwargs.get('instance'))
        x = kwargs['instance'] 
        x = str(x)
        result = Simbad.query_objectids(x)
        if result is None:
            b = Aliases(aliases = "none", name = Star.objects.get(name = x))
            b.save()
        else:
            result_array = result.as_array()
            listA = [j[0].decode("UTF-8") for j in result_array]
            for l in listA:
                l = str(l)
                a = Aliases(aliases = l, name = Star.objects.get(name = x))
                a.save()


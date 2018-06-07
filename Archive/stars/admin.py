from django.contrib import admin

# Register your models here.

from .models import Star, ReferenceURL, ScanImage, Aliases, RA, DEC, Annotation, GalacticCoordinate, Epoch, UnnamedCards, References

#define custom actions below

def check_finished(modeladmin,request,queryset): 
    queryset.update(finished = 'False')
    check_finished.short_description = "Mark selected cards as finished"

def check_unfinished(modeladmin,request,queryset):
    queryset.update(finished = 'True')
    check_unfinished.short_description = "Mark selected cards as unfinished"
    
def check_format(modeladmin,request,queryset):
	queryset.update(format = 'False')
	check_format.short_description = "Mark as cards without a star name"

def check_format2(modeladmin,request,queryset):
	queryset.update(format = 'True')
	check_format2.short_description = "Mark as cards with a star name"
	
# StackedInline is for a template that let's you add more than one foreignkey 
#relationship at once. List_display is for showing what fields you want in the list
#display of the admin page of that model.

class ReferenceURLInline(admin.StackedInline):
	model = ReferenceURL

class ScanImageInline(admin.StackedInline):
	model = ScanImage
	extra = 1

class RAInline(admin.StackedInline):
	model = RA

class DECInline(admin.StackedInline):
	model = DEC

class AnnotationInline(admin.StackedInline):
	model = Annotation

class GalacticCoordinateInline(admin.StackedInline):
	model = GalacticCoordinate

class EpochInline(admin.StackedInline):
	model = Epoch
	
class UnnamedCardsInline(admin.StackedInline):
    model = UnnamedCards
    
class ReferencesInline(admin.StackedInline):
	model = References
	
class StarAdmin(admin.ModelAdmin):
    model = Star
    save_on_top = True
    search_fields = ['name']
    list_display = ('name','finished')
    inlines = [RAInline, DECInline, EpochInline, GalacticCoordinateInline, ReferenceURLInline, ReferencesInline, AnnotationInline, ScanImageInline,
    ]
    actions = [check_finished, check_unfinished]
        
class AliasesAdmin(admin.ModelAdmin):
	model = Aliases
	readonly_fields = ('aliases',)
	view_on_site = False
	list_display = ('aliases', 'name',)
	list_display_links = None
	search_fields = ['name__name', 'aliases']
	def has_add_permission(self, request):
		return False

class DECAdmin(admin.ModelAdmin):
	model = DEC
	list_display = ('degrees', 'arcminutes', 'name')
	def has_add_permission(self, request):
		return False

class RAAdmin(admin.ModelAdmin):
	model = RA
	list_display = ('hours', 'minutes', 'name')
	def has_add_permission(self, request):
		return False

class ReferenceURLAdmin(admin.ModelAdmin):
	model = ReferenceURL
	list_display = ('URL', 'name')
	def has_add_permission(self, request):
		return False

class ScanImageAdmin(admin.ModelAdmin):
	model = ScanImage
	inlines = [UnnamedCardsInline,]
	list_display = ('thumbnail', 'image','format','name')
	readonly_fields = ('thumbnail',)
	list_editable = ('image',)
	actions = [check_format, check_format2]
	
class EpochAdmin(admin.ModelAdmin):
	model= Epoch
	list_display = ('epoch', 'name')
	empty_value_display = '__empty__'
	def has_add_permission(self, request):
		return False

class GalacticCoordinateAdmin(admin.ModelAdmin):
	model = GalacticCoordinate
	list_display = ('lam', 'beta', 'name')
	empty_value_display = '__empty__'
	def has_add_permission(self, request):
		return False
	

class AnnotationAdmin(admin.ModelAdmin):
	model = Annotation
	list_display = ('annotations', 'name')
	search_fields = ['name__name']
	empty_value_display = '__empty__'
	def has_add_permission(self, request):
		return False
	def render_change_form(self, request, context, *args, **kwargs):
        # here we define a custom template
		self.change_form_template = '/admin/change_form.html'
		extra = {
			'help_text': "Use these fields to fill in any left over information that is in the card.",
		}
		context.update(extra)
		return super(AnnotationAdmin, self).render_change_form(request,context, *args, **kwargs)
		
		
class UnnamedCardsAdmin(admin.ModelAdmin):
    model = UnnamedCards
    list_display = ('image', 'description')
    list_editable = ('description',)
    seacrch_fields = ['image__image']
    def has_add_permission(self, request):
        return False
        
class ReferencesAdmin(admin.ModelAdmin):
	model = References
	list_display = ('Ref', 'name')
	def has_add_permission(self, request):
		return False

admin.site.register(ReferenceURL, ReferenceURLAdmin)

admin.site.register(Star, StarAdmin)

admin.site.register(ScanImage, ScanImageAdmin)

admin.site.register(Aliases, AliasesAdmin)

admin.site.register(RA, RAAdmin)

admin.site.register(DEC, DECAdmin)

admin.site.register(Annotation, AnnotationAdmin)

admin.site.register(GalacticCoordinate, GalacticCoordinateAdmin)

admin.site.register(Epoch, EpochAdmin)

admin.site.register(UnnamedCards, UnnamedCardsAdmin)

admin.site.register(References, ReferencesAdmin)

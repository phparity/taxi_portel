from django.contrib import admin
from .models import *
from django.forms import TimeInput
from django.forms import TextInput, Textarea
from django.conf import settings
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
# from django.contrib.gis import admin as gis_admin

admin.site.site_header = "Taxi Portal Administration"
admin.site.site_title = "Taxi Portal Admin"
admin.site.index_title = "Welcome to the Taxi Portal Admin Panel"

    
# Register your models here.
class AirlinesAdmin(admin.ModelAdmin):
    list_display=('IATA_CODE','NAME','ICAO_CODE','LOGO','WEBSITE',)
    # readonly_fields = ('image_path',) 
    
class AirportsAdmin(admin.ModelAdmin):
    list_display=('AIRPORT_SHORT_CODE','AIRPORT_NAME',)   
 
    
class TransferAdmin(admin.ModelAdmin):
    list_display=('FROM','TO','Adults','Children','Infant','Tour_Type')
    
class FastTrackBookingAdmin(admin.ModelAdmin):
    list_display= ('AIRPORT',)
    
class TourTripBookingAdmin(admin.ModelAdmin):
    liat_display = ('City_Name',)


class DestinationPlacesAdmin(admin.ModelAdmin):
    list_display = ('WEBSITE',)

class SupplierManagementAdmin(admin.ModelAdmin):
    list_display = ('Company_Name','WEBSITE', 'Contact_Person_Name','Country_Code','Mobile_Number','Email','Address')
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }


# here Previous_Working_Company_Details ne Driver management jode darsavvav mate aam karel che
class Previous_Working_Company_DetailsItemInline(admin.TabularInline):
    model = Previous_Working_Company_Details

class DriverManagementAdmin(admin.ModelAdmin):
    inlines = [Previous_Working_Company_DetailsItemInline]
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }


class CustomerManagementAdmin(admin.ModelAdmin):
    list_display = ('First_Name','Email','Mobile_Number','National_Unique_ID_Number')
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }


class FastTrack_AddOns_TypeAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    
class FastTrack_AddOnsAdmin(admin.ModelAdmin):
    list_display = ('type','Title','Inbound_Price','Outbound_Price','Image')
    
# ahiya pan be model jodel che
class Service_FeaturesItemInline(admin.TabularInline):
    model = Service_Features

class FastTrack_ServiceAdmin(admin.ModelAdmin):
    inlines = [Service_FeaturesItemInline]

admin.site.register(Airlines,AirlinesAdmin)
admin.site.register(Airports,AirportsAdmin)
admin.site.register(Transfer,TransferAdmin)
admin.site.register(FastTrackBooking,FastTrackBookingAdmin)
admin.site.register(TourTripBooking,TourTripBookingAdmin)
admin.site.register(DestinationPlaces,DestinationPlacesAdmin)
admin.site.register(SupplierManagement,SupplierManagementAdmin)
admin.site.register(DriverManagement, DriverManagementAdmin)
admin.site.register(CustomerManagement,CustomerManagementAdmin)
admin.site.register(FastTrack_AddOns,FastTrack_AddOnsAdmin)
admin.site.register(FastTrack_AddOns_Type,FastTrack_AddOns_TypeAdmin)
admin.site.register(FastTrack_Service,FastTrack_ServiceAdmin)


# Tour Management

class Tour_TypesAdmin(admin.ModelAdmin):
    list_display = ('Tour_Type_Title',)
    
admin.site.register(Tour_Types,Tour_TypesAdmin)

class Tour_Service_TypesAdmin(admin.ModelAdmin):
    list_display =('Tour_Service_Type_Title','Tour_Service_Type_Icon')
    
admin.site.register(Tour_Service_Types,Tour_Service_TypesAdmin)

class Tour_Activities_typesAdmin(admin.ModelAdmin):
    list_display = ('Tour_Activity_Title','Tour_Activity_Icon')
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }
    
admin.site.register(Tour_Activities_types,Tour_Activities_typesAdmin)

class Tour_Thematic_typesAdmin(admin.ModelAdmin):
    list_display = ('Tour_Thematic_Title','Tour_Thematic_Icon')

admin.site.register(Tour_Thematic_types,Tour_Thematic_typesAdmin)


class Tour_Segment_typesAdmin(admin.ModelAdmin):
    list_display = ('Tour_Segment_Title','Tour_Segment_Icon')
    
admin.site.register(Tour_Segment_types,Tour_Segment_typesAdmin)


class Package_Featues_IncludeInline(admin.TabularInline):
    model = Package_Featues_Include
class Activity_1Inline(admin.TabularInline):
    model = Activity_1
class Activity_2Inline(admin.TabularInline):
    model = Activity_2
class Activity_3Inline(admin.TabularInline):
    model = Activity_3
class Activity_4Inline(admin.TabularInline):
    model = Activity_4



class Tour_packagesAdmin(admin.ModelAdmin):
    inlines = [Package_Featues_IncludeInline,Activity_1Inline,Activity_2Inline,Activity_3Inline,Activity_4Inline]
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }
    
    class Media:
            css = {
                'all': ('https://www.jonthornton.com/jquery-timepicker/jquery.timepicker.css',)
            }
            js = (
                "https://code.jquery.com/jquery-3.5.1.min.js",
                "https://www.jonthornton.com/jquery-timepicker/jquery.timepicker.js",
                'js/admin/location_picker1.js',
                
            )

admin.site.register(Tour_packages,Tour_packagesAdmin)

# class Tour_OptionAdmin(admin.ModelAdmin):
#     list_display=('Title','Transfers','Duration')
    
# admin.site.register(Tour_Option,Tour_OptionAdmin)
# @admin.register(Tour_Option)
# class Tour_OptionAdmin(admin.ModelAdmin):
#     change_form_template = 'admin/change_form.html'


class TourOptionAdmin(admin.ModelAdmin):
    model = Tour_Option

    class Media:
        js = ('js/admin/tour_option_admin.js',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        obj = self.get_object(request, object_id)

        # Add custom JavaScript variables to the extra_context dictionary
        extra_context['price_per'] = obj.Price_Per

        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }

admin.site.register(Tour_Option, TourOptionAdmin)



# admin.site.register(Tour_Option, Tour_OptionAdmin)

class Pickup_LocationAdmin(admin.ModelAdmin):
    list_display =("Location","Fees")
    
admin.site.register(Pickup_Location,Pickup_LocationAdmin)

class Vehicle_AddOns_TypesAdmin(admin.ModelAdmin):
    list_display=("AddOns_type",)
    
admin.site.register(Vehicle_AddOns_Types,Vehicle_AddOns_TypesAdmin)

class Vehicle_AddOnsAdmin(admin.ModelAdmin):
    list_display =('Type','Name','Inbound_Price','Outbound_Price','Image')
    
admin.site.register(Vehicle_AddOns,Vehicle_AddOnsAdmin)

class Vehicle_TypeAdmin(admin.ModelAdmin):
    list_display =("Vehicle_Type",)

admin.site.register(Vehicle_Type,Vehicle_TypeAdmin)

class FleetAdmin(admin.ModelAdmin):
    list_display = ('Meta_URL','model_Name','Vehicle_Types')
    formfield_overrides = {
    models.IntegerField: {'widget': TextInput(attrs={'size': '80'})},
    }
    
admin.site.register(Fleet,FleetAdmin)


class VendorsAdmin(admin.ModelAdmin):
    list_display = ('Company_Name','Logo')

admin.site.register(Vendors,VendorsAdmin)


# class CuoponAdmin(admin.ModelAdmin):
#     list_display =('Code','Type')
    

class CouponAdmin(admin.ModelAdmin):
    list_display =('Code','Type')
    model = Coupon

    class Media:
        js = ('js/admin/coupon.js',)


admin.site.register(Coupon,CouponAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display =('Short_Name','Country_name','Currency_Code','Currency_Sign','Phon_Code','Phone_Number_Length')

admin.site.register(Country,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display =('State_Name','Country_Name')
    
admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('State_Name','City_Name')
    
admin.site.register(City,CityAdmin)


# class ZoneAdminForm(forms.ModelForm):
#     class Meta:
#         model = Zone
#         fields = '__all__'
#         widgets = {
#             'coordinates': map_widgets.GoogleMapsAddressWidget,
#         }

# class ZoneAdmin(admin.ModelAdmin):
#     form = ZoneAdminForm

# admin.site.register(Zone, ZoneAdmin)



### Extra Field #######

class RoleAdmin(admin.ModelAdmin):
    list_display=('Name',)
admin.site.register(Role,RoleAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','role')
admin.site.register(UserProfile,UserProfileAdmin)

from django.conf import settings


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        api ='AIzaSyBeQUngByPnQY_2khrrGcD1guFKO9krDuk'
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'js/admin/location_picker.js',
                # 'https://maps.googleapis.com/maps/api/js?key={}&libraries=drawing,callback=initMap'.format(settings.GOOGLE_MAPS_API_KEY),   #&gt;
                # 'https://developers.google.com/maps/documentation/javascript/examples/drawing-tools'
                'https://maps.googleapis.com/maps/api/js?key={}&libraries=drawing&callback=initMap'.format(settings.GOOGLE_MAPS_API_KEY),
                
                # 'js/admin/draw.js',
            )
            
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name','color')        

      
##############################################################
# @admin.register(AA_BankChoices)
# class AA_BankChoicesAdmin(admin.ModelAdmin):
#    list_display = ('bank_name',)
 
# @admin.register(AA_Supplier)   
# class AA_SupplierAdmin(admin.ModelAdmin):
#     list_display =('supplier_id','supplier_name','supplier_type')
   
# @admin.register(AA_Role)
# class AA_RoleAdmin(admin.ModelAdmin):
#     list_display =('name',)
    
# @admin.register(AA_UserProfile)
# class AA_UserProfileAdmin(admin.ModelAdmin):
#     list_display=('user','role')
    
# @admin.register(AA_Customer)
# class AA_CustomerAdmin(admin.ModelAdmin):
#     list_display=('first_name','email','account_status')    
    
    
class BankdetailAdmin(admin.ModelAdmin):
    list_display = ('bank_name',)

admin.site.register(Bankdetail,BankdetailAdmin)



class FeatureChoicesAdmin(admin.ModelAdmin):
    list_display = ('feature_name',)
    
admin.site.register(FeatureChoices,FeatureChoicesAdmin)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display= ('first_name','account_type','account_status','email')
  
@admin.register(AddOn)   
class AddOnAdmin(admin.ModelAdmin):
    list_display =('name','addon_type')
    
    

class TourPackageNAdmin(admin.ModelAdmin):
    list_display = ('Tour_name','tour_package_id')
    class Media:
            css = {
                'all': ('https://www.jonthornton.com/jquery-timepicker/jquery.timepicker.css',)
            }
            js = (
                "https://code.jquery.com/jquery-3.5.1.min.js",
                "https://www.jonthornton.com/jquery-timepicker/jquery.timepicker.js",
                'js/admin/location_picker1.js',
                
            )
    
admin.site.register(TourPackageN,TourPackageNAdmin)



class DispatcherAdmin(admin.ModelAdmin):
    list_display =('user',)
admin.site.register(Dispatcher,DispatcherAdmin)



class VIPServiceAdmin(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(VIPService,VIPServiceAdmin)


class TripAdmin(admin.ModelAdmin):
    list_display =('status','driver')
admin.site.register(Trip,TripAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('user_profile','transaction_type','amount')
admin.site.register(Transaction,TransactionAdmin)

class TripBiddingAdmin(admin.ModelAdmin):
    list_display=('trip','supplier','bid_amount')
admin.site.register(TripBidding,TripBiddingAdmin)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display= ('customer','trip')

@admin.register(Reward)    
class RewardAdmin(admin.ModelAdmin):
    list_display=('user','points')
    
@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display=('user','affiliate_code','commission_rate')
    
class ReferralAdmin(admin.ModelAdmin):
    list_display=('referrer','referred','reward')
admin.site.register(Referral,ReferralAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=('user','service_type','rating')
admin.site.register(Review,ReviewAdmin)


# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
#     }
# admin.site.register(Rental,RentalAdmin)
    
    
# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#           'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
#     }

# import json 
# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

# class RentalAdmin(admin.ModelAdmin): formfield_overrides = {
#     map_fields.AddressField: { 'widget':
#     map_widgets.GoogleMapsAddressWidget(attrs={
#       'data-autocomplete-options': json.dumps({ 'types': ['geocode',
#       'establishment'], 'componentRestrictions': {
#                   'country': 'us'
#               }
#           })
#       })
#     },
# }

# admin.site.register(Rental,RentalAdmin)
# from django.contrib import admin
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {
#           'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
#     }
# from django.contrib import admin
# from django.contrib.gis.db import models
# from location_field.admin import LocationFieldWidget


# class MyModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": LocationFieldWidget}
#     }

# admin.site.register(MyModel, MyModelAdmin)


# from googlemaps import 
from django_google_maps.widgets import GoogleMapsAddressWidget

class LocationAdminForm(forms.ModelForm):
    location = forms.CharField(widget=GoogleMapsAddressWidget())

    class Meta:
        model = Location
        fields = '__all__'

class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm

admin.site.register(Location, LocationAdmin)


from django.contrib import admin
from django import forms
from django.urls import reverse_lazy
from django.utils.html import format_html
from django.conf import settings
from django.forms.widgets import TextInput












class MapZoneForm(forms.ModelForm):
    polygon = forms.CharField(widget=TextInput(attrs={'class': 'vLargeTextField'}))


    class Media:
        js = (
            'https://maps.googleapis.com/maps/api/js?key={}&libraries=drawing&callback=initMap'.format(settings.GOOGLE_MAPS_API_KEY),
            # reverse_lazy('admin:mapzone_polyeditor_js'),
            'js/admin/polyeditor.js',
        )
    
    class Meta:
        model = MapZone
        fields = ('name',)
        

   
        


class MapZoneAdmin(admin.ModelAdmin):
 
    list_display = ('name','id')
    change_form_template = 'admin/app1/mapzone_change_form.html'

admin.site.register(MapZone, MapZoneAdmin)


class ZonePricingAdmin(admin.ModelAdmin):
    
    list_display= ('zone',)

admin.site.register(ZonePricing,ZonePricingAdmin)




# from django_otp.admin import OTPAdminSite
# from django.contrib.auth.models import User
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

# class OTPAdmin(OTPAdminSite):
#     pass

# admin_site = OTPAdmin(name='OTPAdmin')
# admin_site.register(User)
# admin_site.register(TOTPDevice, TOTPDeviceAdmin)


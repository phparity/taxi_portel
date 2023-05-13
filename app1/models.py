from django.db import models
import os
from datetime import datetime
from django.urls import reverse
from django.core.exceptions import ValidationError
from PIL import Image
from django.core.validators import EmailValidator
from fontawesome_5.fields import IconField
from datetime import timedelta
from ckeditor.fields import RichTextField 
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

# from django_google_maps.fields import GoogleMapField
# from django_google_maps.fields import PointField
# from django_google_maps import fields as map_fields
# from django.contrib.gis.db import models
# Create your models here.


#Bank models
class Bankdetail(models.Model):
  bank_name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.bank_name

class Airlines(models.Model):
    IATA_CODE = models.CharField(max_length=10)
    NAME = models.CharField(max_length=50)
    ICAO_CODE = models.CharField(max_length=10)
    LOGO = models.ImageField(upload_to='images/air_logo')
    WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                        ))
    
    # def image_path(self):
    #     return reverse('admin:view_name', args=[str(self.LOGO)])
    # image_path.admin_order_field = 'LOGO'
    # image_path.short_description = 'images path'
    
    def __str__(self):
      return self.NAME
    
class Airports(models.Model):
  WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                        ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                        ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                        ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                      ))
  AIRPORT_NAME = models.CharField(max_length=100)
  AIRPORT_SHORT_CODE = models.CharField(max_length=10)
  Country = models.CharField(max_length=100)
  City = models.CharField(max_length=100, help_text="City where the airport is located")
  Address = models.TextField(help_text="Full address of the airport", blank=True,null=True)
  terminal = models.CharField(max_length=50, help_text="Terminal information", blank=True,null=True)
  gates = models.PositiveIntegerField(help_text="Number of gates at the airport")
  airline_list = models.ManyToManyField(Airlines)
 
  def __str__(self):
    return f"{self.AIRPORT_SHORT_CODE} - {self.City}, {self.Country}"




#Booking Management 
# Transfer
    
class Transfer(models.Model):
  FROM = models.CharField(max_length=100, help_text='Enter your Source point Here')
  TO = models.CharField(max_length=100, help_text='Enter your Destination Point Here')
  Adults = models.IntegerField(default=0)
  Children = models.IntegerField(default=0)
  Infant = models.IntegerField(default=0)
  Tour_Type = models.CharField(max_length=100, choices=(('One Way','One way'),('Round Trip','Round Trip')))
  
class FastTrackBooking(models.Model):
  AIRPORT = models.CharField(max_length=100)
  
class TourTripBooking(models.Model):
  City_Name = models.CharField(max_length=100)
  
  
#Add New Destination Place

class DestinationPlaces(models.Model):
  WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                        ))
  Meta_Title = models.CharField(max_length=150)
  Meta_Keyword = models.CharField(max_length=150)
  Meta_Description = models.CharField(max_length=300)
  Country_Name = models.CharField(max_length=100)
  Destination_Place_Title = models.CharField(max_length=100)
  Image = models.ImageField(upload_to='images/destination_place')
  def clean(self):
        super().clean()
        if self.Image:
            img = Image.open(self.Image)
            width, height = img.size
            if width < 410 or height < 260 :
                raise ValidationError('Photo size must be greater than 410x260 pixels in width and height.')
  Description = models.CharField(max_length=1500)



  
  
  
  
#Supplier Management

class SupplierManagement(models.Model):
  WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                    ))
  Company_Name = models.CharField(max_length=100)
  Contact_Person_Name = models.CharField(max_length=100)
  Country_Code = models.CharField(max_length=10,help_text='Code like US = +1, IN = +91' 'Visit <a href="https://countrycode.org/">Find Your Code</a> for more information.')
  Mobile_Number = models.IntegerField()
  Supplier_ID = models.CharField(max_length=20)
  general_manager_first_name = models.CharField(max_length=100)
  general_manager_last_name = models.CharField(max_length=100)
  reservation_manager_first_name = models.CharField(max_length=100)
  reservation_manager_last_name = models.CharField(max_length=100)
  booking_email = models.EmailField()
  billing_email = models.EmailField()
  billing_circle = models.CharField(max_length=100)
  Email = models.EmailField(
        validators=[EmailValidator(message='Please enter a valid email address.')],
    )
  Address = models.CharField(max_length=300)
  password = models.CharField(max_length=128)
  confirm_password = models.CharField(max_length=128)
  

  def clean(self):
      # Call the parent class's clean() method to perform initial validation
      super().clean()

      # Check if password and confirm_password match
      if self.password != self.confirm_password:
          raise ValidationError("Password and confirm password do not match.")

  def save(self, *args, **kwargs):
      # Call the clean() method before saving to validate password and confirm_password
      self.clean()
      super().save(*args, **kwargs)
      
  bank_Name = models.ForeignKey(Bankdetail, on_delete=models.CASCADE)
  bank_account_holder_name = models.CharField(max_length=100)  
  account_number = models.IntegerField()
  swift_bic = models.CharField(max_length=100)
  
  def __str__(self):
    return self.Company_Name
  
   
   
#extra suvidha
class FeatureChoices(models.Model):
  feature_name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.feature_name
   
   
     
# Driver Management
      
class DriverManagement(models.Model):
  driver_id = models.AutoField(primary_key=True)
  WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                    ))
  First_Name = models.CharField(max_length=50)
  Last_Name = models.CharField(max_length=50)
  Country_Code = models.CharField(max_length=10,help_text='Code like US = +1, IN = +91' 'Visit <a href="https://countrycode.org/">Find Your Code</a> for more information.')
  Mobile_Number = models.IntegerField()
  Email_Address = models.EmailField(
        validators=[EmailValidator(message='Please enter a valid email address.')],
    )
  National_Unique_ID_Number = models.CharField(max_length=50)
  Driving_License_Number = models.CharField(max_length=50)
  Expiry_of_Driving_Licencse = models.DateField(help_text="YYYY:MM:DD")
  Address = models.CharField(max_length=300)
  Driver_Photo = models.ImageField(upload_to='images/Driver_details')
  Driving_Licence_Copy = models.ImageField(upload_to='images/Driver_details')
  supplier = models.ForeignKey(SupplierManagement, on_delete=models.CASCADE, blank=True)
  operational_zone = models.CharField(max_length=100)
  bank = models.ForeignKey(Bankdetail, on_delete=models.CASCADE)
  bank_account_holder_name = models.CharField(max_length=100)
  account_number = models.IntegerField()
  swift_bic = models.CharField(max_length=100) 
  is_available = models.CharField(default=True, max_length=20, choices=(('True',"available"),('False',"unavailable")))

  
class Previous_Working_Company_Details(models.Model):
  driver_comid = models.ForeignKey(DriverManagement, on_delete=models.CASCADE)
  Company_Name = models.CharField(max_length=50, default='None')
  Company_Contact = models.IntegerField(help_text='without Country code', default=0)
  
############################# extr field #########################

class Role(models.Model):
  Name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.Name


# Affiliate model
class Affiliate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliate_code = models.CharField(max_length=10, unique=True)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.1)  # 10% commission

    def __str__(self):
        return f"{self.user.username} - Affiliate"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    affiliate = models.ForeignKey(Affiliate, null=True, blank=True, on_delete=models.SET_NULL)
    referrer = models.ForeignKey(User, null=True, blank=True, related_name='referrals', on_delete=models.SET_NULL)
    referral_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    
    def __str__(self):
      return str(self.user)
    


class CustomerManagement(models.Model):
  ACCOUNT_STATUS_CHOICES = models.CharField(max_length=100,choices=(('active', 'Active'),('unactive', 'Unactive'),('suspended', 'Suspended')),default='unactive')
  First_Name = models.CharField(max_length=50)
  Last_Name = models.CharField(max_length=50)
  Email = models.EmailField(
        validators=[EmailValidator(message='Please enter a valid email address.')],
    )
  password = models.CharField(max_length=128)
  confirm_password = models.CharField(max_length=128)
  

  def clean(self):
      # Call the parent class's clean() method to perform initial validation
      super().clean()

      # Check if password and confirm_password match
      if self.password != self.confirm_password:
          raise ValidationError("Password and confirm password do not match.")

  def save(self, *args, **kwargs):
      # Call the clean() method before saving to validate password and confirm_password
      self.clean()
      super().save(*args, **kwargs)
  National_Unique_ID_Number = models.CharField(max_length=50)
  Country_Code = models.CharField(max_length=10,help_text='Code like US = +1, IN = +91' 'Visit <a href="https://countrycode.org/">Find Your Code</a> for more information.')
  Mobile_Number = models.IntegerField(help_text="Enter mobile Number ")
  Gender = models.CharField(max_length=10, choices=(('male','Male'),('female','Female')))
  Age =  models.IntegerField()
  Address_One = models.CharField(max_length=300)
  Address_Two = models.CharField(max_length=300)
  Nearest_Famous_Place = models.CharField(max_length=200)
  Country = models.CharField(max_length=20)
  State = models.CharField(max_length=20)
  City = models.CharField(max_length=20)
  referral_code = models.CharField(max_length=100, blank=True)
  upload_id = models.ImageField(upload_to='images/AA_customer_ids/', blank=True, null=True)
  
  def __str__(self):
      return self.First_Name
  
  
class Countries(models.Model):
  sortname = models.CharField(max_length=20)
  country_name = models.CharField(max_length=50)
  phonecode = models.CharField(max_length=5)


# class State(models.Model):
#   country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
  


class AddOn(models.Model):
  addon_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  SERVICE_CHOICES = (
      ('transfer', 'Transfer'),
      ('airport_vip', 'Airport VIP Service'),
      ('tour', 'Tour'),
      ('access_disabled', 'Access for Disabled'),
  )
  addon_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name

  

#fasttrack management


class FastTrack_AddOns_Type(models.Model):
  Name = models.CharField(max_length=80)
  
class FastTrack_AddOns(models.Model):
  # type = models.ForeignKey(FastTrack_AddOns_Type, on_delete=models.CASCADE)
  type = models.ForeignKey(AddOn, on_delete=models.CASCADE, limit_choices_to={'addon_type': 'airport_vip'})
  Title = models.CharField(max_length=100)
  Image = models.ImageField(upload_to='images/FastTrack_AddOns')
  Inbound_Price = models.IntegerField()
  Outbound_Price = models.IntegerField()
  Description = models.CharField(max_length=400)
  
class FastTrack_Service(models.Model):
  Airport = models.ForeignKey(Airports, on_delete=models.CASCADE)
  Type = models.CharField(max_length=50, choices=(('ARRIVAL','ARRIVAL'),('DEPARTURE','DEPARTURE')))
  Image = models.ImageField(upload_to='images/FastTrack_Service')
  Title = models.CharField(max_length=100)
  Per_Adults_Price = models.IntegerField()
  Per_Child_Price = models.IntegerField()
  Per_Infant_Price = models.IntegerField()
  Per_Pets_Price = models.IntegerField()
  Taxes_and_Fees = models.IntegerField()
  
  
class Service_Features(models.Model):
  Service_Featuresids = models.ForeignKey(FastTrack_Service, on_delete=models.CASCADE)
  Features_Icon = IconField(max_length=30, null=True, blank=True)
  Features_Title = models.CharField(max_length=350)
  


#Tour management


class Tour_Types(models.Model):
  Tour_Type_Title = models.CharField(max_length=100, primary_key=True)
  WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                    ))
  Meta_Title = models.CharField(max_length=150)
  Meta_Keyword = models.CharField(max_length=150)
  Meta_Description = models.CharField(max_length=300)
  
class Tour_Service_Types(models.Model):
  Tour_Service_Type_Title = models.CharField(max_length=150, primary_key=True)
  Tour_Service_Type_Icon = IconField(max_length=30)
  
  def __str__(self):
    return self.Tour_Service_Type_Title
  
class Tour_Activities_types(models.Model):
  Tour_Activity_Title = models.CharField(max_length=150, primary_key=True)
  Tour_Activity_Icon = IconField(max_length=30)
  
  def __str__(self):
    return self.Tour_Activity_Title 
  
class Tour_Thematic_types(models.Model):
  Tour_Thematic_Title = models.CharField(max_length=150, primary_key=True)
  Tour_Thematic_Icon = IconField(max_length=30)
  
  def __str__(self):
    return self.Tour_Thematic_Title
  
# class Tour_Thematic_types(models.Model):
#   Tour_Service_Title = models.CharField(max_length=150)
#   Tour_Service_Icon = IconField(max_length=30)
  
class Tour_Segment_types(models.Model):
  Tour_Segment_Title = models.CharField(max_length=150, primary_key=True)
  Tour_Segment_Icon = IconField(max_length=30)
  
  def __str__(self):
    return self.Tour_Segment_Title
  


class Tour_packages(models.Model):
  Tour_id = models.AutoField(primary_key=True)
  WEBSITE = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                    ))
  Meta_Title = models.CharField(max_length=150)
  Meta_Keyword = models.CharField(max_length=150)
  Meta_Description = models.CharField(max_length=300)
  Package_Title = models.CharField(max_length=150)
  Tour_Type = models.ForeignKey(Tour_Types,on_delete=models.CASCADE)
  Tour_Service = models.ForeignKey(Tour_Service_Types,on_delete=models.CASCADE)
  Tour_Activities = models.ForeignKey(Tour_Activities_types,on_delete=models.CASCADE)
  Tour_Thematic = models.ForeignKey(Tour_Thematic_types,on_delete=models.CASCADE)
  City_Name = models.CharField(max_length=50)
  Total_Duration = models.DurationField(help_text='add HH:MM:SS formet')

  Main_Image = models.ImageField(upload_to='images/Tour_packages',help_text="Image must 1366x406 Pixel")
  def clean(self):
        super().clean()
        if self.Main_Image:
            img = Image.open(self.Main_Image)
            width, height = img.size
            if width < 1366 or height < 406 :
                raise ValidationError('Photo size must be greater than 1366x406 pixels in width and height.')
              
  Secondary_Image = models.ImageField(upload_to='images/Tour_packages',help_text="Image must 465x264 Pixel")
  def clean(self):
        super().clean()
        if self.Secondary_Image:
            img = Image.open(self.Secondary_Image)
            width, height = img.size
            if width < 465 or height < 264 :
                raise ValidationError('Photo size must be greater than 465x264 pixels in width and height.')
      
  Third_Image = models.ImageField(upload_to='images/Tour_packages',help_text="Image must 235x143 Pixel")
  def clean(self):
        super().clean()
        if self.Third_Image:
            img = Image.open(self.Third_Image)
            width, height = img.size
            if width < 465 or height < 264 :
                raise ValidationError('Photo size must be greater than 235x143 pixels in width and height.')
              
  Fourth_Image = models.ImageField(upload_to='images/Tour_packages',help_text="Image must 235x143 Pixel")
  def clean(self):
          super().clean()
          if self.Fourth_Image:
              img = Image.open(self.Fourth_Image)
              width, height = img.size
              if width < 465 or height < 264 :
                  raise ValidationError('Photo size must be greater than 235x143 pixels in width and height.')
  
  Logo_Image = models.ImageField(upload_to='images/Tour_packages')
  Tour_Main_Features = models.CharField(max_length=300 ,help_text='In Sort for ex.(Flexible Reservation)')
  Tour_Main_Features_Description = models.CharField(max_length=300 ,help_text='In Sort for ex.(What is a flexible reservation? If your plans change, you can cancel the activity.))')
  Pick_up_time = models.CharField(max_length=50)
  Duration = models.CharField(max_length=50)
  Departure_Day = models.CharField(max_length=50)
  Type_of_guide = models.CharField(max_length=50)
  Return_point = models.CharField(max_length=50)
  Tour_Package_Description_One = RichTextField()
  Tour_Package_Description_Two = RichTextField()
  Tour_Package_Additional_Information_One = RichTextField()
  Tour_Package_Additional_Information_Two = RichTextField()
  What_Includes = RichTextField()
  What_Is_Not_Included = RichTextField()
  Hygiene_and_safety_measures = RichTextField()
  Remarks_And_General_information = RichTextField()
  
  def __str__(self):
    return self.Meta_Title
  
class Package_Featues_Include(models.Model):
  Tour_feaid = models.ForeignKey(Tour_packages, on_delete=models.CASCADE)
  Tour_Features_Title = models.CharField(max_length=150, primary_key=True)
  Tour_Features_Icon = IconField(max_length=30)
  
class Activity_1(models.Model):
  Activity_1id = models.ForeignKey(Tour_packages, on_delete=models.CASCADE)
  Activity_Image =  models.ImageField(upload_to='images/Tour_packages',null=True, blank=True)
  Activity_Title = models.CharField(max_length=150,null=True, blank=True, help_text=("like : Modifiable date"))
  Activity_Description = models.CharField(max_length=350,null=True, blank=True)
  
class Activity_2(models.Model):
  Activity_2id = models.ForeignKey(Tour_packages, on_delete=models.CASCADE)
  Activity_Image =  models.ImageField(upload_to='images/Tour_packages',null=True, blank=True)
  Activity_Title = models.CharField(max_length=150,null=True, blank=True, help_text=("like : FREE Cancelation"))
  Activity_Description = models.CharField(max_length=350,null=True, blank=True)
  
class Activity_3(models.Model):
  Activity_3id = models.ForeignKey(Tour_packages, on_delete=models.CASCADE)
  Activity_Image =  models.ImageField(upload_to='images/Tour_packages',null=True, blank=True)
  Activity_Title = models.CharField(max_length=150,null=True, blank=True, help_text=("like : Safety Measure"))
  Activity_Description = models.CharField(max_length=350,null=True, blank=True)
 

 
class Activity_4(models.Model):
  Activity_4id = models.ForeignKey(Tour_packages, on_delete=models.CASCADE)
  Activity_Image =  models.ImageField(upload_to='images/Tour_packages',null=True, blank=True)
  Activity_Title = models.CharField(max_length=150,null=True, blank=True, help_text=("like : Best Price guarantee"))
  Activity_Description = models.CharField(max_length=350,null=True, blank=True)
  



class Tour_Option(models.Model):
  Tour_Package = models.ForeignKey(Tour_packages, on_delete=models.CASCADE)
  Title = models.CharField(max_length=200)
  Duration = models.DurationField()
  # Availability = models.CharField()
  MONDAY = 'MON'
  TUESDAY = 'TUE'
  WEDNESDAY = 'WED'
  THURSDAY = 'THU'
  FRIDAY = 'FRI'
  SATURDAY = 'SAT'
  SUNDAY = 'SUN'
  WEEKDAY_CHOICES = (
      (MONDAY, 'Monday'),
      (TUESDAY, 'Tuesday'),
      (WEDNESDAY, 'Wednesday'),
      (THURSDAY, 'Thursday'),
      (FRIDAY, 'Friday'),
      (SATURDAY, 'Saturday'),
      (SUNDAY, 'Sunday'),
  )

  # Fields for each day of the week
  monday = models.BooleanField(default=False)
  tuesday = models.BooleanField(default=False)
  wednesday = models.BooleanField(default=False)
  thursday = models.BooleanField(default=False)
  friday = models.BooleanField(default=False)
  saturday = models.BooleanField(default=False)
  sunday = models.BooleanField(default=False)

  def get_weekdays(self):
    weekdays = []
    if self.monday:
        weekdays.append(self.MONDAY)
    if self.tuesday:
        weekdays.append(self.TUESDAY)
    if self.wednesday:
        weekdays.append(self.WEDNESDAY)
    if self.thursday:
        weekdays.append(self.THURSDAY)
    if self.friday:
        weekdays.append(self.FRIDAY)
    if self.saturday:
        weekdays.append(self.SATURDAY)
    if self.sunday:
        weekdays.append(self.SUNDAY)
    return weekdays
  Transfers =models.CharField(max_length=100, choices=(('Round_Trip','Round_Trip'),('One_Way','One_Way')))
  Short_Description = models.CharField(max_length=500)
  Shift = models.CharField(max_length=100,choices=(('Morning','Morning'),('Afternoon','Afternoon'),('Evening','Evening')))
  Price_Per = models.CharField(max_length=50,choices=(('Per_Person','Per_Person'),('Per_Product','Per_Product')))
  Per_Adults_Price = models.IntegerField(blank=True, null=True)
  Per_Child_Price = models.IntegerField(blank=True, null=True)
  Per_Infant_Price = models.IntegerField(blank=True, null=True)

  Total_Product = models.IntegerField(default=1,blank=True, null=True)
  Product_Price = models.IntegerField(blank=True, null=True)
    
  Taxes_And_Fees = models.IntegerField(help_text="(In %)")
  
  def __str__(self):
    return self.Price_Per
  
# class Per_Product(models.Model):
#   Tour_Option = models.ForeignKey(Tour_Option, on_delete=models.CASCADE)
#   Total_Product = models.IntegerField(default=1)
#   Product_Price =  models.IntegerField()
  

# class per_person


class Pickup_Location(models.Model):
  Location = models.CharField(max_length=250)
  Fees = models.IntegerField()
 
 
#Vehicle Management 
  
class Vehicle_AddOns_Types(models.Model):
  AddOns_type = models.CharField(max_length=150, primary_key=True)
  Features_Icon = IconField(max_length=30)  
  
  def __str__(self):
    return self.AddOns_type
  
class  Vehicle_AddOns(models.Model):
  Type = models.ForeignKey(Vehicle_AddOns_Types, on_delete=models.CASCADE)
  Name = models.CharField(max_length=100)
  Description = models.CharField(max_length=300)
  Image = models.ImageField(upload_to='images/Vehicle_AddOns')
  Inbound_Price =models.IntegerField()
  Outbound_Price =models.IntegerField()
  
class Vehicle_Type(models.Model):
  Vehicle_Type = models.CharField(max_length=200)
  
  def __str__(self):
    return self.Vehicle_Type
  
class Fleet(models.Model):
  vehicle_id = models.AutoField(primary_key=True)
  Meta_URL = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                    ))
  Meta_Keyword = models.CharField(max_length=200)
  Meta_Description = models.CharField(max_length=350)
  Vehicle_Types = models.ForeignKey(Vehicle_Type,on_delete=models.CASCADE)
  model_Name = models.CharField(max_length=80)
  brand = models.CharField(max_length=100)
  year = models.PositiveIntegerField()
  plate = models.CharField(max_length=10)
  Max_Passenger = models.IntegerField()
  Max_Bag = models.IntegerField() 
  Max_Carry_Ons = models.IntegerField()
  Vehicle_Price = models.IntegerField()
  vehicle_record = models.TextField(null=True)
  features = models.ManyToManyField(FeatureChoices)
  Vehicle_Image =models.ImageField(upload_to='images/Vehicle_image')
  Vehicle_Image2 =models.ImageField(upload_to='images/Vehicle_image',blank=True)
  Vehicle_Image3 =models.ImageField(upload_to='images/Vehicle_image',blank=True)
  
  
# class Vehicle_Featues(models.Model):
#   VF_id = models.ForeignKey(Fleet,on_delete=models.CASCADE)
#   Features_Icon = IconField(max_length=30)
#   Features_Title = models.CharField(max_length=150)
#   Show_On_Feet =models.CharField(max_length=30, choices=(("Yes","Yes"),('No','No')))
  
  
#Zone Management

# class Zone(models.Model):
#   City_Name = models.CharField(max_length=150)
#   Zone_name = models.CharField(max_length=150)
#   # Map = models.PolygonField()

# Vendors management
class Vendors(models.Model):
  Meta_URL = models.CharField(max_length=100, choices=(('www.gocaribetour.com','www.gocaribetour.com'),
                                                          ('www.dominicanairportshuttle.com','www.dominicanairportshuttle.com'),
                                                          ('www.transferspuntacana.com','www.transferspuntacana.com'),
                                                          ('www.dominicanlimousine.com','www.dominicanlimousine.com')
                                                    ))
  Email = models.EmailField(
        validators=[EmailValidator(message='Please enter a valid email address.')],
    )
  password = models.CharField(max_length=128)
  confirm_password = models.CharField(max_length=128)

  def clean(self):
      # Call the parent class's clean() method to perform initial validation
      super().clean()

      # Check if password and confirm_password match
      if self.password != self.confirm_password:
          raise ValidationError("Password and confirm password do not match.")

  def save(self, *args, **kwargs):
      # Call the clean() method before saving to validate password and confirm_password
      self.clean()
      super().save(*args, **kwargs)
  Company_Name = models.CharField(max_length=100)
  Contact_Name = models.CharField(max_length=100)
  Operation_Contact_Info = models.CharField(max_length=100)
  Reservation_Contact_Info = models.CharField(max_length=100)
  Billing_Contact_Info = models.CharField(max_length=100)
  Logo = models.ImageField(upload_to='images/Vendors')
  Status = models.CharField(max_length=100, choices=(("Active","Active"),("Block","Block")))

# Coupon model
class Coupon(models.Model):
  Code = models.CharField(max_length=100)
  Type =  models.CharField(max_length=100, choices=(("Discount By Percentage","Discount By Percentage"),("Discount By Amount","Discount By Amount")))
  Percentage = models.PositiveIntegerField(blank=True,null =True)
  Quantity = models.CharField(max_length=100, choices=(('Unlimited','Unlimited'),('Limited','Limited')))
  Limit =  models.PositiveIntegerField(blank=True,null=True)
  Start_Date =models.DateField()
  End_Date = models.DateField()
  
  
  
#Settings

class Country(models.Model):
  Country_id = models.AutoField(primary_key=True)
  Country_name = models.CharField(max_length=100)
  Short_Name = models.CharField(max_length=100)
  Currency_Code = models.CharField(max_length=100)
  Currency_Sign = models.CharField(max_length=100)
  Phon_Code = models.IntegerField()
  Phone_Number_Length = models.IntegerField()
  
  def __str__(self):
    return self.Country_name
  
class State(models.Model):
  Country_Name = models.ForeignKey(Country,on_delete=models.CASCADE)
  State_Name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.State_Name
  
class City(models.Model):
  Country_Name = models.ForeignKey(Country,on_delete=models.CASCADE)
  State_Name = models.ForeignKey(State,on_delete=models.CASCADE)
  City_Name = models.CharField(max_length=100)
  
  
# zone management

class Zone(models.Model):
  City_name = models.CharField(max_length=100)
  Zone_Name = models.CharField(max_length=100)
  location = models.JSONField()
    # address = map_fields.AddressField(max_length=200)
    # Map = map_fields.GeoLocationField(max_length=100)
  def __str__(self):
        return self.Zone_Name
      

class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

# from django.contrib.gis.db import models

# class Location(models.Model):
#     name = models.CharField(max_length=255)
#     area = models.PolygonField()

class Status(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('bid', 'Bid'),
        ('assigned', 'Assigned'),
        ('unsigned', 'Unsigned'),
        ('client_non_show', 'Client non-show'),
        ('driver_non_show', 'Driver non-show'),
        ('on_location', 'On location'),
        ('customer_in_car', 'Customer in the car'),
        ('drugstore_stops', 'Drugstore stops'),
        ('medical_stops', 'Medical stops'),
        ('grocery_stops', 'Grocery stops'),
        ('meeted', 'Meeted'),
        ('greeted', 'Greeted'),
        ('picked_up', 'Picked Up'),
        ('assisted', 'Assisted'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    name = models.CharField(max_length=100, choices=STATUS_CHOICES)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Staff(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('biller', 'Biller'),
        ('dispatcher', 'Dispatcher'),
        ('admin', 'Admin'),
        ('superadmin', 'Superadmin'),
        ('supplier', 'Supplier'),
        ('driver', 'Driver'),
    )

    ACCOUNT_STATUS_CHOICES = (
        ('activate', 'Activate'),
        ('suspended', 'Suspended'),
    )

    staff_id_photo = models.ImageField(upload_to='images/staff_ids/')
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    referral_code = models.CharField(max_length=100, blank=True)
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='suspended')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class TourPackageN(models.Model):
  Tour_name = models.CharField(max_length=50, help_text="Give Name of tour")
  price_adult = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price for adults")
  price_children = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price for children")
  price_others = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price for others")
  infant_age = models.PositiveIntegerField(help_text="Age limit for infants")
  total_passengers = models.PositiveIntegerField(help_text="Total number of passengers")
  total_products = models.PositiveIntegerField(help_text="Total number of products")
  select_date = models.DateField(help_text="Selected date for the tour")
  select_shift = models.CharField(max_length=50, help_text="Selected shift for the tour")
  transfer_tour_option_id = models.PositiveIntegerField(help_text="Transfer tour option ID")
  tour_package_id = models.PositiveIntegerField(unique=True, help_text="Tour package ID")
  pick_up_location = models.CharField(max_length=200, help_text="Pick up location")
  pickup_source_lat = models.FloatField(help_text="Latitude of the pickup source",blank=True)
  pickup_source_long = models.FloatField(help_text="Longitude of the pickup source",blank=True)
  total_original_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total original price")
  created_at = models.DateTimeField(auto_now_add=True, help_text="Creation timestamp")
  updated_at = models.DateTimeField(auto_now=True, help_text="Update timestamp")
  description = models.TextField(help_text="Tour description")
  included = models.TextField(help_text="What is included in the tour")
  not_included = models.TextField(help_text="What is not included in the tour")
  remark = models.TextField(help_text="Remarks")
  general_information = models.TextField(help_text="General information")
  duration = models.DurationField(help_text="Tour duration")
  buy_with_peace_of_mind = models.TextField(help_text="Buy with peace of mind information")
  what_to_know_before_buying = models.TextField(help_text="What to know before buying")
  date_change_policies = models.TextField(help_text="Date change policies")
  cancellation_policy = models.TextField(help_text="Cancellation policy")
  who_could_not_do_this_activity = models.TextField(help_text="Who could not do this activity")
  before_attending = models.TextField(help_text="Before attending information")
  hygiene_and_safety_measures = models.TextField(help_text="Hygiene and safety measures")

  def __str__(self):
      return f"Tour Package ID: {self.tour_package_id} - Date: {self.select_date}"

  
# Dispatcher model
class Dispatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# VIP Service model
class VIPService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as necessary



class Trip(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    driver = models.ForeignKey(DriverManagement, on_delete=models.SET_NULL, null=True)
    winning_bid = models.OneToOneField('TripBidding', on_delete=models.SET_NULL, null=True,related_name='winning_trip')

    def assign_winning_bid(self):
        lowest_bid = self.tripbidding_set.order_by('bid_amount').first()
        if lowest_bid:
            self.winning_bid = lowest_bid
            self.save()
            return True
        return False

    # Add other fields as necessary

    def assign_driver(self):
        available_drivers = DriverManagement.objects.filter(is_available=True)
        if available_drivers.exists():
            # Choose the first available driver (you can implement more advanced logic here)
            chosen_driver = available_drivers.first()
            self.driver = chosen_driver
            self.status = 'active'
            chosen_driver.is_available = False
            chosen_driver.save()
            self.save()
            return True
        return False

class Transaction(models.Model):
    TRANSACTION_TYPES = (	
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
    )

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user} {self.transaction_type}: {self.amount}"



# Trip Bidding model
class TripBidding(models.Model):
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  supplier = models.ForeignKey(SupplierManagement, on_delete=models.CASCADE)
  bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
  is_winner = models.BooleanField(default=False)


# Booking model
class Booking(models.Model):
    customer = models.ForeignKey(CustomerManagement, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)


# Rewards model
class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    description = models.TextField()

# Referral model
class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrer')
    referred = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)

# Review model
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SERVICE_CHOICES = (
        ('transfer', 'Transfer'),
        ('vip_service', 'VIP Service'),
        ('tour', 'Tour'),
    )
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    service_id = models.IntegerField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review {self.review_id} - {self.service_type}"





###################################################################################################################################################
# new models


# class AA_Role(models.Model):
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#       return self.name
    
# class AA_UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.ForeignKey(AA_Role, on_delete=models.SET_NULL, null=True)

# class AA_Customer(models.Model):
#     ACCOUNT_STATUS_CHOICES = (
#         ('active', 'Active'),
#         ('unactive', 'Unactive'),
#         ('suspended', 'Suspended'),
#     )

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone = models.IntegerField()
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     referral_code = models.CharField(max_length=100, blank=True)
#     account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='unactive')
#     upload_id = models.ImageField(upload_to='images/AA_customer_ids/', blank=True, null=True)
    
    
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"






# #Bank models
# class Bank(models.Model):
#   bank_name = models.CharField(max_length=100)
  
#   def __str__(self):
#     return self.bank_name




# class AA_Supplier(models.Model):
#     supplier_id = models.CharField(max_length=100)
#     supplier_type = models.CharField(max_length=100)
#     supplier_name = models.CharField(max_length=100)
#     general_manager_first_name = models.CharField(max_length=100)
#     general_manager_last_name = models.CharField(max_length=100)
#     reservation_manager_first_name = models.CharField(max_length=100)
#     reservation_manager_last_name = models.CharField(max_length=100)
#     booking_email = models.EmailField()
#     billing_email = models.EmailField()
#     billing_circle = models.CharField(max_length=100)
#     website = models.URLField()
#     bank_account_holder_name = models.CharField(max_length=100)
#     account_number = models.IntegerField()
#     bank = models.ForeignKey(AA_BankChoices,on_delete=models.CASCADE)
#     swift_bic = models.CharField(max_length=100)

#     def __str__(self):
#         return self.supplier_name


# class AA_Status(models.Model):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('active', 'Active'),
#         ('bid', 'Bid'),
#         ('assigned', 'Assigned'),
#         ('unsigned', 'Unsigned'),
#         ('client_non_show', 'Client non-show'),
#         ('driver_non_show', 'Driver non-show'),
#         ('on_location', 'On location'),
#         ('customer_in_car', 'Customer in the car'),
#         ('drugstore_stops', 'Drugstore stops'),
#         ('medical_stops', 'Medical stops'),
#         ('grocery_stops', 'Grocery stops'),
#         ('meeted', 'Meeted'),
#         ('greeted', 'Greeted'),
#         ('picked_up', 'Picked Up'),
#         ('assisted', 'Assisted'),
#         ('completed', 'Completed'),
#         ('canceled', 'Canceled'),
#     )

#     name = models.CharField(max_length=100, choices=STATUS_CHOICES)
#     color = models.CharField(max_length=7)

#     def __str__(self):
#         return self.name

# class AA_Dispatcher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# class AA_Driver(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fleet = models.ForeignKey(Fleet, on_delete=models.SET_NULL, null=True)
#     is_available = models.BooleanField(default=True)


# class AA_Trip(models.Model):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('active', 'Active'),
#         ('completed', 'Completed'),
#         ('canceled', 'Canceled')
#     )
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     driver = models.ForeignKey(AA_Driver, on_delete=models.SET_NULL, null=True)
#     def assign_driver(self):
#         available_drivers = AA_Driver.objects.filter(is_available=True)
#         if available_drivers.exists():
#             # Choose the first available driver (you can implement more advanced logic here)
#             chosen_driver = available_drivers.first()
#             self.driver = chosen_driver
#             self.status = 'active'
#             chosen_driver.is_available = False
#             chosen_driver.save()
#             self.save()
#             return True
#         return False



# class AA_TripBidding(models.Model):
#     trip = models.ForeignKey(AA_Trip, on_delete=models.CASCADE)
#     supplier = models.ForeignKey(AA_Supplier, on_delete=models.CASCADE)
#     bid_amount = models.DecimalField(max_digits=10, decimal_places=2)


# class Fleet(models.Model):
#     CATEGORY_CHOICES = (
#         ('standard_sedan', 'STANDARD SEDAN'),
#         ('minivan', 'MINIVAN'),
#         ('executive_van', 'EXECUTIVE VAN'),
#         ('business_sedan', 'BUSINESS SEDAN'),
#         ('luxury_van', 'LUXURY VAN'),
#         ('vintage_cars', 'VINTAGE CARS'),
#         ('luxury_suv', 'LUXURY SUV'),
#         ('armored', 'ARMORED'),
#         ('handicap_van', 'HANDICAP VAN'),
#         ('classic_stretch_limousine', 'CLASSIC STRETCH LIMOUSINE'),
#         ('suv_stretch_limousine', 'SUV STRETCH LIMOUSINE'),
#         ('microbus', 'MICROBUS'),
#         ('party_bus', 'PARTY BUS'),
#         ('large_bus', 'LARGE BUS'),
#     )

#     FEATURE_CHOICES  = (
#         ('meet_greet', 'Meet & Greet'),
#         ('free_wifi', 'Free Wi-Fi'),
#         ('free_cancellation', 'Free Cancellation'),
#         ('no_undesired_stops', 'No undesired stops'),
#         ('taxes_included', 'Taxes Included'),
#         ('wait_time', '45 min. Wait time'),
#         ('non_smoking', 'Non-smoking'),
#         ('armored', 'Armored'),
#         ('sound_system', 'Sound System'),
#         ('drinks_included', 'Drinks Included'),
#         ('decoration_included', 'Decoration Included'),
#     )

#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     image1 = models.ImageField(upload_to='iamges/fleet_images/')
#     image2 = models.ImageField(upload_to='iamges/fleet_images/')
#     image3 = models.ImageField(upload_to='iamges/fleet_images/')
#     brand = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     year = models.PositiveIntegerField()
#     plate = models.CharField(max_length=10)
#     seater = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 101)])
#     bags = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 101)])
#     carry_ons = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 101)])
#     visible_online = models.BooleanField()
#     vehicle_record = models.TextField()
#     features = models.ManyToManyField('Feature')

#     def __str__(self):
#  

# from django.db import models
# from django_google_maps import fields as map_fields

# class Rental(models.Model):
#     address = map_fields.AddressField(max_length=200)
#     geolocation = map_fields.GeoLocationField(max_length=100)
    


class Location(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # location = models.PointField(default='POINT(0 0)', null=True, blank=True)

    def __str__(self):
        return self.name
  

      
class MapZone(models.Model):
    name = models.CharField(max_length=255)
    Polygon = models.TextField(max_length=1000)
    # polygon =  models.TextField()
    
    def __str__(self):
      return self.name
    
# class ZonePricing(models.Model):
#     zone = models.ForeignKey(MapZone, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     user_type = models.CharField(max_length=255, help_text="client, franchise, or driver")  # 'client', 'franchise', or 'driver'


class ZonePricing(models.Model):
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(MapZone, on_delete=models.CASCADE)
    client_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_price = models.DecimalField(max_digits=10, decimal_places=2)
    driver_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

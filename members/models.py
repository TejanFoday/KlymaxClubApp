import pycountry
from django.db import models

class Member(models.Model):
    join_date = models.DateField(auto_now_add=True)
    membership_status = models.CharField(max_length=100, default='Active')
    member_id = models.CharField(max_length=100, unique=True, editable=False)
    full_name = models.CharField(max_length=255, default='John Doe')
    nick_name = models.CharField(max_length=255, blank=True, default='')
    email_address = models.EmailField(max_length=255, unique=True,null=True, blank=True)  # Added Email Address field
    phone_number = models.CharField(max_length=30, default='000-000-0000')
    year_joining_klymax = models.IntegerField(default=2022)
    year_joining_foundation = models.IntegerField(default=2022)
    
    CONTINENT_CHOICES = [
        ('AF', 'Africa'),
        ('AN', 'Antarctica'),
        ('AS', 'Asia'),
        ('EU', 'Europe'),
        ('NA', 'North America'),
        ('OC', 'Oceania'),
        ('SA', 'South America'),
    ]
    continent = models.CharField(max_length=2, choices=CONTINENT_CHOICES, default='AF')
    COUNTRY_CHOICES = [(country.alpha_2, country.name) for country in pycountry.countries]
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='SL')
    state_district_city = models.CharField(max_length=100, default='Unknown')
    occupation = models.CharField(max_length=100, default='Unknown')
    field_of_study = models.CharField(max_length=100, default='Unknown')
    foundation_position = models.CharField(max_length=100, blank=True, default='')
    skills_expertise = models.TextField(default='')

    def save(self, *args, **kwargs):
        if not self.member_id:
            last_member = Member.objects.all().order_by('id').last()
            if last_member:
                last_id = int(last_member.member_id.split('-')[1])
                new_id = 'KBF-{0:03d}'.format(last_id + 1)
            else:
                new_id = 'KBF-021'
            self.member_id = new_id
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class CampusDon(models.Model):
    full_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=30, default='000-000-0000')
    current_year_in_college = models.IntegerField()
    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    year_joined_club = models.IntegerField()
    club_position = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.faculty} - {self.department}"

    class Meta:
        verbose_name = 'Campus Don'
        verbose_name_plural = 'Campus Dons'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='contents/')

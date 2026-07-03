from django.db import models

NATIONALITY_CHOICES = (
    ('ARG', 'Argentina'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('BEL', 'Belgium'),
    ('BRA', 'Brazil'),
    ('CAN', 'Canada'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('COL', 'Colombia'),
    ('CUB', 'Cuba'),
    ('DEU', 'Germany'),
    ('DNK', 'Denmark'),
    ('EGY', 'Egypt'),
    ('ESP', 'Spain'),
    ('FRA', 'France'),
    ('GBR', 'United Kingdom'),
    ('GRC', 'Greece'),
    ('IND', 'India'),
    ('IRL', 'Ireland'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JPN', 'Japan'),
    ('KOR', 'South Korea'),
    ('MEX', 'Mexico'),
    ('NLD', 'Netherlands'),
    ('NOR', 'Norway'),
    ('NZL', 'New Zealand'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('RUS', 'Russia'),
    ('SWE', 'Sweden'),
    ('TUR', 'Turkey'),
    ('UKR', 'Ukraine'),
    ('USA', 'United States'),
    ('URY', 'Uruguay'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
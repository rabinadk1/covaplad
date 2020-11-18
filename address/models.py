from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("name", "country"), name="province_unique_name_country"
            ),
        )

    def __str__(self):
        # return f"{self.name}, {self.country}"
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("name", "province"), name="district_unique_name_province"
            ),
        )

    def __str__(self):
        # return f"{self.name}, {self.province}"
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    is_rural = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "municipalities"

        constraints = (
            models.UniqueConstraint(
                fields=("name", "district"), name="municipality_unique_name_district"
            ),
        )

    def __str__(self):
        # return f"{self.name}, {self.district} ({self.type})"
        return f"{self.name} ({self.type})"

    @property
    def type(self) -> str:
        return "Rural" if self.is_rural else "Urban"


class Ward(models.Model):
    number = models.PositiveSmallIntegerField()
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("number", "municipality"),
                name="ward_unique_number_municiplaity",
            ),
        )

    def __str__(self):
        # mun_name, rest = str(self.municipality).split(",", 1)
        # return ",".join((f"{mun_name}-{self.number}", rest))
        return str(self.number)

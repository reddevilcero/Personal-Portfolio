from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _

# Create your models here.


class Learning(models.Model):

    name = models.CharField(_("name"), max_length=50)
    icon = models.ImageField(_("Icon"), upload_to="img/icons")
    skills = RichTextField(_('skills'), max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("learning")
        verbose_name_plural = _("learnings")

    def __str__(self):
        return self.name


class Organization(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    organization_url = models.URLField(_("Organization Website"),
                                       max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Certification(models.Model):

    name = models.CharField(_("name"), max_length=50)
    organization = models.ForeignKey("Organization",
                                     verbose_name=_("Organization"),
                                     on_delete=models.CASCADE, null=True)
    cert_img = models.ImageField(_("Certification"),
                                 upload_to="img/certifications")
    cert_related = models.CharField(_("Techonology studied"), max_length=50)

    class Meta:
        verbose_name = _("certification")
        verbose_name_plural = _("certifications")

    def __str__(self):
        return f"{self.name} - {self.organization.name}"


class Project(models.Model):

    name = models.CharField(_("name"), max_length=50)
    project_type = models.CharField(_("Type of project"), max_length=50,
                                    choices=[('commercial', 'Commercial'),
                                             ('personal', 'Personal'),
                                             ('volunteer', 'Volunteer'),
                                             ('practice', 'Practice')])
    technology = models.ManyToManyField("Learning",
                                        verbose_name=_("Techonology used"))
    website = models.URLField(_("Website"), max_length=200)
    gitHub = models.URLField(_("GitHub link"), max_length=200, null=True)
    screenshot = models.ImageField(_("Web screenshot"),
                                   upload_to="img/screenshots")
    description = models.TextField(_("Description"), null=True)

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")

    def __str__(self):
        return self.name

from django.db import models

from main.consts import ContactStatus


class TermsAndConditions(models.Model):
    """
    Model for the Terms and Conditions
    """

    terms = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Terms And Conditions created at {self.created_at}"

    class Meta:
        verbose_name = "Terms and Conditions"
        verbose_name_plural = "Terms and Conditions"


class PrivacyPolicy(models.Model):
    """
    Model for the Privacy Policy
    """

    policy = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Privacy Policy created at {self.created_at}"


class Contact(models.Model):
    """
    Model representing a user's contact request.
    """

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, default=ContactStatus.PENDING.value)
    resolved_date = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=50)
    admin_notes = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        """
        Return a string representation of the model.
        """
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ["-contact_date"]
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"

from django.db import models

class Todo(models.Model):
    """Model representing a TODO item."""
    
    title = models.CharField(
        max_length=200,
        help_text="Title of the TODO item"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description (optional)"
    )
    due_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Due date and time (optional)"
    )
    is_resolved = models.BooleanField(
        default=False,
        help_text="Mark as resolved/completed"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['is_resolved', '-created_at']
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=200)
    dot = models.IntegerField(default=0) # @TODO update to float
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# https://dolarhoje.com/ptax/
class DollarToday(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)


class FollowUpCard(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    notify = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return self.card.name

class Installments(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    current_installment = models.IntegerField(default=1)
    total_installments = models.IntegerField(default=2)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return self.card.name
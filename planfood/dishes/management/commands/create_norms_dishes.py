from django.core.management.base import BaseCommand

from planfood.common.models import Group
from planfood.dishes.models import Dish, Norm


class Command(BaseCommand):
    help = 'Creates empty norms for each dish'

    def handle(self, *args, **options):
        self.stdout.write('Starting...')

        dishes = Dish.objects.all()
        groups = Group.objects.all()

        for dish in dishes.iterator():
            for group in groups.iterator():
                for product in dish.products.iterator():
                    for age_category in group.age_categories.iterator():

                        has_norm = dish.norms.filter(
                            product=product, group=group, age_category=age_category
                        ).exists()

                        if not has_norm:
                            norm = Norm.objects.create(
                                dish=dish,
                                product=product,
                                group=group,
                                age_category=age_category,
                                value=0.0,
                            )
                            self.stdout.write(
                                '"{} - {} - {} - {} - {}" is added'.format(
                                    norm.dish.name,
                                    norm.product.name,
                                    norm.group.name,
                                    norm.age_category.name,
                                    norm.value,
                                )
                            )

        self.stdout.write('Finished.')

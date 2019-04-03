from django.core.management.base import BaseCommand

from planfood.common.models import Group, ProductCategory
from planfood.products.models import Norm


class Command(BaseCommand):
    help = 'Creates empty norms for each category of products'

    def handle(self, *args, **options):
        self.stdout.write('Starting...')

        product_categories = ProductCategory.objects.all()
        groups = Group.objects.all()

        for product_category in product_categories.iterator():
            for group in groups.iterator():
                for age_category in group.age_categories.iterator():

                    has_norm = product_category.product_norms.filter(
                        group=group, age_category=age_category
                    ).exists()

                    if not has_norm:
                        norm = Norm.objects.create(
                            product_category=product_category,
                            group=group,
                            age_category=age_category,
                            value=0.0,
                        )
                        self.stdout.write(
                            '"{} - {} - {} - {}" is added'.format(
                                norm.product_category.name,
                                norm.group.name,
                                norm.age_category.name,
                                norm.value,
                            )
                        )

        self.stdout.write('Finished.')

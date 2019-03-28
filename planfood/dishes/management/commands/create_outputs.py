from django.core.management.base import BaseCommand

from planfood.common.models import Group
from planfood.dishes.models import Dish, Output


class Command(BaseCommand):
    help = 'Creates empty output items for each dish'

    def handle(self, *args, **options):
        self.stdout.write('Starting...')

        dishes = Dish.objects.all()
        groups = Group.objects.all()

        for dish in dishes.iterator():
            for group in groups.iterator():
                for age_category in group.age_categories.iterator():

                    has_output = dish.outputs.filter(
                        group=group, age_category=age_category
                    ).exists()

                    if not has_output:
                        output = Output.objects.create(
                            dish=dish, group=group, age_category=age_category, value='0'
                        )
                        self.stdout.write(
                            '"{} - {} - {} - {}" is added'.format(
                                output.dish.name,
                                output.group.name,
                                output.age_category.name,
                                output.value,
                            )
                        )

        self.stdout.write('Finished.')

import pandas as pd
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from student.models import Student


class Command(BaseCommand):
    help = 'Import student from csv file'

    def handle(self, *args, **kwargs):

        # Define the path to the 'data' folder.
        data_dir = os.path.join(settings.BASE_DIR , 'Data')
        print(f"Looking for file at: {data_dir}")

        # Create the full path to the csv file.
        csv_file_path = os.path.join(data_dir ,'sample.csv')
        print(f"Looking for file at csv_file_path: {data_dir}")
        # C:\Users\Prathamesh\PycharmProjects\Django_Import_Excel_Project\Data\sample.csv
        try:
            # Load the CSV file into a DataFrame
            
            df = pd.read_csv(csv_file_path)

            # Fill missing values
            df['name'] = df['name'].fillna(value='Unknown')
            df['age'] = df['age'].ffill()
            df['city'] = df['city'].fillna(value='Unknown')

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('CSV file not found.'))

            return

        for _, row in df.iterrows():
            Student.objects.create(
                name = row['name'],
                age = row['age'],
                city = row['city']
            )

            
            
            self.stdout.write(self.style.SUCCESS(
                'Successfully imported students.'))
from django.core.exceptions import ValidationError
import os


def validate_file_size(file):
    max_size_kb = 10000  # max size of 3MB
    if file.size > max_size_kb * 1024: # file sizes are often measured in bytes(file.size is in bytess).
        raise ValidationError(f'Error!: File Size Should be less than {max_size_kb * 1024}MB')
    

def validate_file_extensions(file):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.mp4', '.pdf', '.docx', '.csv', 'xlsx']  # ex: supported extensions
    extension = os.path.splitext(file.name)[1] # split the extension from the path name
    
    if not extension.lower() in valid_extensions:
        raise ValidationError(f'Error!: Supported extensions are: {", ".join(valid_extensions)}')
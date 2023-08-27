from pydoc import doc
from django.core.exceptions import ValidationError 

def validate_file_size(file): 
  """
  This function checks if the file size is equal to 50 kb and raise A ValidationError if it is not.

  Args:
      file (integer): The file size  

  Raises:
      ValidationError: Error that's raise  
  """
  max_size_kb = 500 
   
  if file.size > max_size_kb * 1024: 
     raise ValidationError(f'Files cannot be larger than {max_size_kb} kb')
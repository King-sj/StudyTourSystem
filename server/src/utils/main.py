__all__ = ['generate_filename']
import random
import string
import os
def generate_filename(directory='', length=12, extension=''):
  """
  生成一个自定义长度和扩展名的随机文件名，并检查是否已存在
  返回的自由文件名+后缀(默认不含后缀，后缀形式应为('./txt')), dir仅用于检验
  """
  while True:
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for i in range(length))
    filename = random_string + extension
    file_path = os.path.join(directory, filename)
    if not os.path.exists(file_path):
      return filename
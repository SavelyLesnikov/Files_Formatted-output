file_name = 'msd.txt'
with open(file_name, 'r') as file:
    print(file.read())
# Оператор "with" автоматически закрывает файл, в отличие от ручного закрытия командой ".close()"

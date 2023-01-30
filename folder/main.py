from util import ImportedClass

def print_output(text):
    print(text)

if __name__ == '__main__':
    full_name = 'Gacoka Mbui'
    imported_class_instance = ImportedClass(full_name)
    titled_name = imported_class_instance.return_titled_name()
    print_output(titled_name)


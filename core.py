import sys, argparse
import io, re

version = '0.0.1'

def find_user(id_user, id_file):
    with io.open(id_file) as f:
        for line in f:
            if id_user in line:
                print (line, end="")
  
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog = 'Epson_Parser_log', 
            description = '''''',
            epilog = '''(c) Snowycat 2020. Автор программы, как всегда, не несет никакой ответственности ни за что.''',
            add_help = False
        )
    
    info_group = parser.add_argument_group (title = 'Параметры')
    info_group.add_argument ('-h', '--help', action = 'help', help = 'Справка')
    info_group.add_argument ('-v', '--version', action = 'version', help = 'Вывести номер версии', version = '%(prog)s {}'.format (version))
    
    comand_group = parser.add_argument_group(title = 'Команды')
    comand_group.add_argument ('-f', '--file', help = 'выбор файла или директории')
    #comand_group.add_argument ('-m', '--module',  dest = 'option', help = 'поиск по удачно залогинившимся пользователям ллибо просто по всему')
    comand_group.add_argument ('-u', '--user', help = 'поиск по человеку')

    namespace = parser.parse_args (sys.argv[1:])

    #print(parser.parse_args())
    #print(namespace.user)

    if namespace.user:
        find_user(namespace.user, namespace.file)
    else:
        print(parser.print_usage())





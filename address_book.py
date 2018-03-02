import argparse

file_path = './data.txt'
parser = argparse.ArgumentParser(description='CLI address book')
parser.add_argument('action', choices=['show', 'add'], default='add', help='add or display address book')
parser.add_argument('-n', '--name', help='Name of your friend')
parser.add_argument('-p', '--phone', help='Phone number of your friend', type=int)
args = parser.parse_args()
print(args)
if args.action == 'add':
    if args.name is None:
        parser.error("Name is required")
    if args.phone is None:
        parser.error('Phone is required')
    f = open(file_path, 'a')
    f.write("Name: %s\tPhone: %s\n" % (args.name, args.phone))
    print('%s saved!' % args.name)
else:  # show
    print(open(file_path, 'r').read())

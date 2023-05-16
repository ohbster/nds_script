import json
from datetime import datetime
#from humanfriendly import format_size, parse_size
import humanfriendly

def tsv_out(input_list=None):
    filename = f'''{datetime.now().strftime('%Y-%m%d-%H%M%S')}_results.tsv'''

    items = json.loads(input_list)
    #archive list
    if items['archive_list']:
        with open(filename,'a') as f:
            print('***Archive List***',file=f)
            for item in items['archive_list']:
                print(f'''{item['name']}\t{humanfriendly.format_size(item['size'],binary=True)}\t{item['items']}''',file=f)
    #empty/delete list
    if items['delete_list']:
        with open(filename,'a') as f:
            print('\n\n***Delete List***',file=f)
            for item in items['delete_list']:
                print(f'''{item['name']}\t{item['size']}''',file=f)
    if items["invalid_list"]:
        with open(filename,'a') as f:
            print('\n\n***Invalid Containers***',file=f)
            for item in items['invalid_list']:
                print(f'''{item['name']}''',file=f)
    if items["time_out_list"]:
        with open(filename,'a') as f:
            print('\n\n***Timed out Containers***',file=f)
            for item in items['time_out_list']:
                print(f'''{item['name']}''',file=f)

    #print (json.loads(input_list))
    return
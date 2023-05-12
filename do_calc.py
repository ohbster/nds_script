"""
This script will:
    1. Read a list of names
    2. Check if a container exists with the name
    3. Check if the container is empty (contains 0 bytes)
    4. If container is empty, return "N/A" for container size
    5. If container has data, return a sum as container size
   
    6. Return json with container name and file sizes
    7. Return json of invalid containers
Obijah <obijah.greaux@pwc.com>

"""

from azure.storage.blob import ContainerClient 
import json

def do_calc(token_credential=None,account_url=None,container_list=None):
    if (container_list is None) or (len(container_list) == 0):
        exit()

    archive_list = []
    delete_list = []
    invalid_list = []
    #1)Main Loop: check all container names
    for container_name in container_list:
        containerService = ContainerClient(
            account_url=account_url,
            container_name=container_name,
            credential=token_credential
        )
        #2)Skip invalid container names to avoid an error
        if not containerService.exists():
            print(f'invalid: container "{container_name}" - skipping')
            invalid_list.append(container_name)
            continue

        metadata = containerService.get_container_properties()
        print (f'Container Metadata: {metadata}')
        
        #Inner loop: check all blobs in container and sum size
        container_size = 0
        
        #for blob_name in containerService.list_blob_names():
        blob_names = containerService.list_blob_names()
    
        blob_count = 0
        for blob_name in blob_names:
            blob_count += 1
            
            #This section may be unnecessary
            #print (f"*Test* {container_name} blobName: {blob_name}")
            # if blob_name is None:
            #     print("Testing: blob_name==None")
            #     delete_list.append(
            #         {
            #             "name" : container_name,
            #             "size" : "N/A"
            #         }
            #     )
                    
            blobService = containerService.get_blob_client(blob_name)
            container_size += blobService.get_blob_properties().size
        #3) Check if container size > 0
        if (container_size == 0) or (blob_count == 0):
            #4)return "N/A for size"
            delete_list.append(
                {
                    "name": container_name,
                    "size": "N/A"
                }
            )
        else:
            #5)return sum
            archive_list.append(
                {
                    "name": container_name,
                    "size": container_size,
                    "items": blob_count
                }
            )
    result = {'archive_list': archive_list,
                'delete_list': delete_list,
                'invalid_list': invalid_list,
                #'response':'200'
                }

    result = json.dumps(result)
    return result
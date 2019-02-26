import asyncio
import os
import pprint

from azure.storage.blob import baseblobservice, BlockBlobService

azure_account_name = os.environ.get('AZURE_ACCOUNT_NAME')
azure_account_key = os.environ.get('ACCOUNT_KEY')

test_dict = {}
groups = []


def load_azure():
    block_blob_service = BlockBlobService(account_name=azure_account_name,
                                          account_key=azure_account_key)

    base_blob_service = baseblobservice.BaseBlobService(account_name=azure_account_name,
                                                        account_key=azure_account_key)

    containers = base_blob_service.list_containers()

    # Create a dictionary of all the groups that are available
    for c in containers:

        test_dict[c.name] = {}
        groups.append(c.name)
        blobs = base_blob_service.list_blobs(container_name=c.name, delimiter="/")

        for blob in blobs:
            member_name = blob.name[:-1]
            test_dict[c.name][member_name] = 0

    # Fill the picture count for each member
    for group in groups:
        print("     " + group + "...")
        for member in test_dict[group]:
            generator = block_blob_service.list_blobs(group, prefix=member)
            count = 0

            for blob in generator:
                count += 1

            test_dict[group][member] = count
        print("     done\n")

    # Print the dict out to the console
    pprint.pprint(test_dict)

    print("done loading azure")
    asyncio.sleep(1)

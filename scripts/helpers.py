# helper functions for generation! yippee
import os


def makeUFolder(pack_id):
    # create a folder for the user with the given pack_id
    try:
        os.makedirs(f'output/{pack_id}', exist_ok=True)
    except OSError as error:
        raise RuntimeError(f'Failed to create folder! {error}')
    if not os.path.exists(f'output/{pack_id}'):
        raise RuntimeError(f'Failed to create folder!')
    else:
        print(f'Folder created')
        return f'output/{pack_id}'


def removeUFolder(pack_id):
    # remove the folder for the user with the given pack_id
    try:
        os.rmdir(f'output/{pack_id}')
    except OSError as error:
        raise RuntimeError(f'Failed to remove folder! {error}')
    if os.path.exists(f'output/{pack_id}'):
        raise RuntimeError(f'Failed to remove folder!')
    else:
        print(f'Folder removed')
        return True


def uBasicFolderStruct(pack_id, namespace):
    # create the folder structure for the user with the given pack_id
    try:
        os.makedirs(f'output/{pack_id}/data', exist_ok=True)
        os.makedirs(f'output/{pack_id}/data/{namespace}', exist_ok=True)
    except OSError as error:
        raise RuntimeError(f'Failed to create folder structure! {error}')
    if not os.path.exists(f'output/{pack_id}/data/{namespace}/tags/functions'):
        raise RuntimeError(f'Failed to create folder structure!')
    else:
        print(f'Folder structure created')
        return f'output/{pack_id}/data/{namespace}/'


def genmeta(pack_id, description):
    with open(f'output/{pack_id}/pack.mcmeta', 'w') as file:
        try:
            file.write(f'''
                {{
                "pack": {{
                        "pack_format": 48,
                        "description": "{description}"
                    }}
                }}
            ''')
        except Exception as error:
            raise RuntimeError(f'Failed to write to file! {error}')

    # return the path to the generated pack.mcmeta file
    return f'output/{pack_id}/pack.mcmeta'


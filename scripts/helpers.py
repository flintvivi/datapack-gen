# helper functions! yippee
import os
import uuid

from flask import render_template, request

def makePackID():
    # generate a unique pack id
    return str(uuid.uuid4().hex)


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
    # create the basic folder structure for the user with the given pack_id
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


def uFuncFolderStruct(pack_id, namespace):
    # create the mcfunctions folder structure for the user with the given pack_id
    try:
        os.makedirs(f'output/{pack_id}/data/{namespace}/functions', exist_ok=True)
    except OSError as error:
        raise RuntimeError(f'Failed to create folder structure! {error}')
    if not os.path.exists(f'output/{pack_id}/data/{namespace}/functions'):
        raise RuntimeError(f'Failed to create folder structure!')
    else:
        print(f'Folder structure created')
        return f'output/{pack_id}/data/{namespace}/functions/'
    

def uTagFolderStruct(pack_id, namespace):
    # create the tag folder structure for the user with the given pack_id
    try:
        os.makedirs(f'output/{pack_id}/data/{namespace}/tags/functions', exist_ok=True)
    except OSError as error:
        raise RuntimeError(f'Failed to create folder structure! {error}')
    if not os.path.exists(f'output/{pack_id}/data/{namespace}/tags/functions'):
        raise RuntimeError(f'Failed to create folder structure!')
    else:
        print(f'Folder structure created')
        return f'output/{pack_id}/data/{namespace}/tags/functions/'
    

def uAdvFolderStruct(pack_id, namespace):
    # create the advancement folder structure for the user with the given pack_id
    try:
        os.makedirs(f'output/{pack_id}/data/{namespace}/advancements', exist_ok=True)
    except OSError as error:
        raise RuntimeError(f'Failed to create folder structure! {error}')
    if not os.path.exists(f'output/{pack_id}/data/{namespace}/advancements'):
        raise RuntimeError(f'Failed to create folder structure!')
    else:
        print(f'Folder structure created')
        return f'output/{pack_id}/data/{namespace}/advancements/'


def uRecipeFolderStruct(pack_id, namespace):
    # create the recipe folder structure for the user with the given pack_id
    try:
        os.makedirs(f'output/{pack_id}/data/{namespace}/recipes', exist_ok=True)
    except OSError as error:
        raise RuntimeError(f'Failed to create folder structure! {error}')
    if not os.path.exists(f'output/{pack_id}/data/{namespace}/recipes'):
        raise RuntimeError(f'Failed to create folder structure!')
    else:
        print(f'Folder structure created')
        return f'output/{pack_id}/data/{namespace}/recipes/'


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


def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s


def apology(message, code):
    # render message as an apology to user
    # modified function from cs50
    
    return render_template("apology.html", top=code, bottom=escape(message)), code


def check(page: str):
    # run checks on user input
    if not page:
        raise RuntimeError("check(): Missing page parameter")
    
    if page == "framework":
        namespace = request.form.get('namespace')
        dpname = request.form.get('dpname')
        authors = request.form.get('authors')

        # checks for null inputs
        for value, message in (
            (namespace, 'namespace is required'),
            (dpname, 'datapack name is required'),
            (authors, 'author(s) are required'),
        ):
            if not value:
                return apology(message, 400)
        
        # checks for invalid inputs
        if not all(isinstance(value, str) for value in (namespace, dpname, authors)):
            return apology('one or more inputs was invalid', 400)

        # checks for invalid characters in inputs
        invalid_chars = set('<>:"/\\|?*') # invalid characters for file/folder names
        if any(char in invalid_chars for char in (namespace, dpname, authors)):
            return apology('one or more inputs contains invalid characters', 400)

        return True

def blankPack(pack_id, namespace, dpname, authors):
    # create a blank datapack with the given parameters
    try:
        makeUFolder(pack_id)
        uBasicFolderStruct(pack_id, namespace)
        genmeta(pack_id, f'{dpname} by {authors}')
    except Exception as error:
        raise RuntimeError(f'Failed to create blank datapack! {error}')
    return True
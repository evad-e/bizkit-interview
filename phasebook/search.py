from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    ret = []
 
    if args.get('id') != None:
       ret.extend(filter(lambda USERS: USERS['id'] == args.get('id'), USERS))
    if args.get('name') != None:
       ret.extend(filter(lambda USERS: args.get('name').lower() in USERS['name'].lower(), USERS))
    if args.get('age') != None:
       age = int(args.get('age'))
       ret.extend(filter(lambda USERS: int(USERS['age']) <= age + 1 and int(USERS['age']) >= age - 1, USERS))
    if args.get('occupation') != None:
         ret.extend(filter(lambda USERS: args.get('occupation').lower() in USERS['occupation'].lower(), USERS))
    
    for i in range(len(ret)-1, 0, -1):
        if ret[i] in ret[:i]:
            del ret[i]

    return ret if args else USERS
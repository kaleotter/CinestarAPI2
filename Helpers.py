from sqlalchemy import inspect
from 


def object2Dict (self, obj):
    return {c.key: getattr(obj, c.key)
    for c in inspect(obj).mapper.column_attrs}



from models.main_model import db
from flask import request, url_for

class BaseModel(db.Model):
    __abstract__ = True  # This class will not be used to create a table

    @classmethod
    def get(cls, paginate, route):
        
        if paginate is None:
            items = cls.query.all()
            return [item.to_dict() for item in items]
        else:
            if route is None:
                raise NullRouteError("Route cannot be empty when pagination is active")
        
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', paginate, type=int)
            pagination = cls.query.paginate(page=page, per_page=per_page, error_out=False)
            items = pagination.items
            total = pagination.total
            pages = pagination.pages

            data = {
                'current_page': page,
                'data': [item.to_dict() for item in items],
                'first_page_url': url_for(f'{cls.__tablename__}.{route}', page=1, per_page=per_page, _external=True),
                'from': pagination.page * pagination.per_page - pagination.per_page + 1,
                'last_page': pages,
                'last_page_url': url_for(f'{cls.__tablename__}.{route}', page=pages, per_page=per_page, _external=True),
                'next_page_url': url_for(f'{cls.__tablename__}.{route}', page=page + 1, per_page=per_page, _external=True) if pagination.has_next else None,
                'path': request.base_url,
                'per_page': per_page,
                'prev_page_url': url_for(f'{cls.__tablename__}.{route}', page=page - 1, per_page=per_page, _external=True) if pagination.has_prev else None,
                'to': pagination.page * pagination.per_page if pagination.page * pagination.per_page < total else total,
                'total': total
            }

            return data
        
    @classmethod
    def first(cls, user_id):
        return cls.query.get(user_id)
    
    @classmethod
    def filter(cls, key, value):
        return cls.query.filter( key == value).all()
    
    @classmethod
    def oneByEmail(cls, email):
        return cls.query.filter( cls.email == email ).first()


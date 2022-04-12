# StoreFront

Ecommerce project for placing orders with unique features:
- product tagging
- product collections
- product promotions
- wish lists

## Stack:
- Python 3
- Django 4
- Django Rest Framework 3
- PyJWT
- Djoser

## Dummy data is included:
Just run seed_db.py to populate model instances. You may
encounter IntegrityError caused by duplicating key value unique constraint.
To solve this problem you should resync primary key fields:

```SELECT setval('tablename_id_seq', (SELECT MAX(id) FROM tablename)+1);```

## Endpoint samples
```
- GET/POST store/products/ - for getting all the products and creating new ones
- GET/POST /store/products/{id}/reviews/ - for getting product reviews and 
creating bound ones
- GET/POST store/collections/ - for getting all product collections
- POST store/carts/ - for creating a new cart
- GET/POST store/orders/ - for getting orders or creating new ones
- GET store/customers/ - for getting customers
- POST /auth/users/ - for creating new user
- POST auth/jwt/create/ - for receiving jwt-tokens
```

## Installation:
1. Clone the repository:
```
git clone https://github.com/Techinek/book_store_pro.git
```
2. Run docker (all the requirements will be installed automatically):
```
docker-compose up
```
3. Make migrations:
```
docker exec mosh_web_1 python manage.py makemigrations
docker exec mosh_web_1 python manage.py migrate
```
4. Populate dummy data:
```
docker exec mosh_web_1 python manage.py seed_db
```

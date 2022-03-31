# StoreFront

Ecommerce project for placing orders with unique features:
- product tagging
- product collections
- product promotions
- wish lists

## Dummy data is included:
Just run seed.sql to populate model instances. You may
encounter IntegrityError caused by duplicating key value unique constraint.
To solve this problem you should resync primary key fields:

```SELECT setval('tablename_id_seq', (SELECT MAX(id) FROM tablename)+1);```
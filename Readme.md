##Python flask basic api

This API has been configured to do the following
- mysql
- authentication for JWT token
- middleware for token validations
- auto routes registration (add only routes files and or controllerls)



- setup environment variable
```bash
cp .env.example .env
```

- (conditional) If venv folder is not available
```bash
python3 -m venv venv
```

- enable virtual environment
```bash
source venv/bin/activate
```


- install required dependencies
```bash
pip install -r requirements.txt
```

- run dev
```bash
python app.py
```


- turn off virtual environment
```bash
deactivate
```



---
- generate requirements.txt
```bash
pip freeze > requirements.txt
```


- generate secrets for .env 

 - for JWT secret
 ```bash
 python -c "import secrets; print(secrets.token_hex(32))"
 ```

 - for flask secret
 ```bash
 python -c "import secrets; print(secrets.token_hex(24))"
 ```
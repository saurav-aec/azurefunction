import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://172.17.0.1:8081/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'mshldb'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'document'),
    'tenant_id': os.environ.get('TENANT_ID', '[YOUR TENANT ID]'),
    'client_id': os.environ.get('CLIENT_ID', '[YOUR CLIENT ID]'),
    'client_secret': os.environ.get('CLIENT_SECRET', '[YOUR CLIENT SECRET]'),
}
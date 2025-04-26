from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb+srv://Aryan512:Aryan512@cluster0.lln5fwj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(uri)

db = client["expense-tracker-db"]

users_collection = db["users"]
category_collection = db["category"]
transaction_collection = db["transactions"]
budget_collection = db["budgets"]
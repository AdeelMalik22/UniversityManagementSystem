from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://myAdminUser:myStrongPassword@localhost:27017/?authSource=admin"
client = AsyncIOMotorClient(...)(MONGO_DETAILS)
mongodb = client["college"]

import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz.")
    # await db.drop_users()
    await db.create_table_users()
    print("Yaratildi.")

    print("Foydalanuvchilarni qo'shamiz.")

    await db.add_user("anvar", "sariqdev", 123456)
    await db.add_user("hghjghj", "jhgjhgjg", 1)
    await db.add_user("ghhgf", "rewrerwe", 2)
    await db.add_user("hjhjgj", "fgfgfghfgh", 3)
    await db.add_user("hgjhgjhg", "2jgjhgj", 4)

    print("Qo'shildi.")

    users = await db.select_all_user()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")


asyncio.run(test())
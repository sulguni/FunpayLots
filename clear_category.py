from FunPayAPI import Account, Runner, types, enums
import os

TOKEN = os.getenv("FP_TOKEN")
if TOKEN is None:
    print("token not set")
    exit()

acc = Account(TOKEN).get()

categories = list(map(int, input("Categories to delete: ").split()))
for category in categories:
    lots = acc.get_my_subcategory_lots(category)
    for lot in lots:
        print("Удаляем", lot.title)
        acc.delete_lot(int(lot.id))

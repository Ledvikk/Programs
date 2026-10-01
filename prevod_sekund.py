time = int(input("Zadejte čas v sekundách: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

if hours >= 24:
    hours = hours % 24
    days = time // 86400
    print(f"[{days} days, {hours:02d}:{minutes:02d}:{seconds:02d}]")
else:
    print(f"[{hours:02d}:{minutes:02d}:{seconds:02d}]")

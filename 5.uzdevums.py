import datetime

rn = datetime.datetime.now().hour

if 6 <= rn < 12:
    sv = "Labrīt!"
elif 12 <= rn < 18:
    sv = "Labdien!"
else:
    sv = "Labvakar!"

print(sv)

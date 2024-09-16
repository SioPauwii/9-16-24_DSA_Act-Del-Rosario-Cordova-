import datetime

currDateTime = datetime.datetime.now()

print(f'Current Date and Time:\n{currDateTime.strftime("%B")} {currDateTime.strftime("%d")}, {currDateTime.strftime("%Y")}')
print(f'{currDateTime.strftime("%I")}:{currDateTime.strftime("%M")} {currDateTime.strftime("%p")}')
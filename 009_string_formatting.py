name = 'my name'
subs = 9

# don't use +
msg = "Wow! " + name + " you have " + str(subs) + " subs!"
# use f""
msg = f"Wow! {name} you have {subs} subs!"



from string import Template
template = Template("The table ${tablename} has ${rows} rows")

result = template.substitute(tablename='ELEMENT', rows=4)
print(result)

data = {'tablename':'ELEMENT', 'rows': 4}
result = template.substitute(data)
print(result)

# result = template.substitute('ELEMENT', 4) # doesn't work
def fanktion():
  print('hello world')

#this will return error bcs the func has no argument
#fanktion('abc') 

def funktion(*args): #args is inform of tuple
  print('hello world ', args)

funktion()
funktion("wlee")
funktion("wlee", 123, "asdawd")

def finktion(*args, **kwargs): #args & kwargs is inform of tuple
  print('hello world ', args, kwargs)
  print(args[1])
  print(kwargs['key'])

finktion("wlee", 123, key=124, abc="argh")

# basicly args kwargs itu kaya argument collectors
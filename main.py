with open('recipe.txt') as f:
  cook_book = {}
  ingr_count=0
  line=f.readline()
  line=line.rstrip('\n')
  while line !='':
    if line == '\n':
      line=f.readline()
      line=line.rstrip('\n')
    cook_book[line]=[]
    global value
    value = cook_book[line]
    line=f.readline()
    line.rstrip('\n')
    ingr_count=int(line)
    i=0
    while i < (ingr_count):
      i+=1
      line=f.readline()
      line_one=line.split('| ')
      ingr_name=line_one[0].rstrip()
      ingr_quant=int(line_one[1])
      ingr_measure=line_one[2]
      ingr_measure=ingr_measure.rstrip()
      value.append({'ingredient_name': ingr_name,'quantity':ingr_quant,'measure': ingr_measure})
    line=f.readline()
print(cook_book)
print()
shop_list={}
def get_shop_list_by_dishes(dishes, person_count):
  for key, values in cook_book.items():
    if key in dishes:
      for ingredient in values:  
        shop_list[ingredient['ingredient_name']] = {'measure' : ingredient['measure'], 'quantity' : ingredient['quantity']*person_count}
  print(shop_list)

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)          

 


      

  





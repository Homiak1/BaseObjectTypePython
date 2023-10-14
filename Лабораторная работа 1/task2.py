# TODO Найдите количество книг, которое можно разместить на дискете
diskette_volume = 1.44
pages_count = 100
symbols_on_string = 25
strings_on_page = 50
symbol_cost = 4
total_symbols_count = pages_count * symbols_on_string * strings_on_page
volume = total_symbols_count * symbol_cost
volume_Mb = volume/1024/1024
books_count = int(diskette_volume//volume_Mb)
print("Количество книг, помещающихся на дискету:", books_count)

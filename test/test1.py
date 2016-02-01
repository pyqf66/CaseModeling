# -*- coding: utf-8 -*-
sublevel_id=[9,8,3,30]
toplevel_count_list=[1,2,20,27]
real_index_list=list()
for j in sublevel_id:
    real_index = int(j)
    toplevel_count_index = 0
    while ((real_index - toplevel_count_list[toplevel_count_index]) > 0):
        real_index = real_index - toplevel_count_list[toplevel_count_index]
        toplevel_count_index = toplevel_count_index + 1
    real_index_list.append(real_index)
print(real_index_list)

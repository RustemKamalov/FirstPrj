file_read = open("test.txt")
file_write = open("test_w.txt", "w")
lst_read = [line.rstrip() for line in file_read]
new_lst = lst_read[::-1]
line_write = '\n'.join(new_lst)
file_write.write(line_write)
file_write.close()
file_read.close()





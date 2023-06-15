l1 = [{'make':'Nokia','model':216,'color':'black'} , {'make':'Mi Max','model':'2','color':'Gold'} ,{'make':'Samsung','model':7,'color':'blue'}]

res = (lambda lst: sorted(lst, key = lambda x: int(x["model"]), reverse=True))(l1)
print(res)
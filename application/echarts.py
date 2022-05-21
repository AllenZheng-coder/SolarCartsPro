from fileinput import filename
from pyecharts.charts import Bar

def bar_chart(x_name, y_name, y_data, filename):
    bar = Bar()
    bar.add_xaxis(x_name)
    bar.add_xaxis(y_name, y_data)
    bar.render("./templates/{}.html".format(filename))
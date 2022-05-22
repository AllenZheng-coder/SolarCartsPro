import function
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts import options as opts

def bar_chart(x_name, y_axis, filename, widths, heights):
    bar = Bar(init_opts=opts.InitOpts(width=widths, height=heights))
    bar.add_xaxis(x_name)
    for y_name, y_data in y_axis.items():
        bar.add_yaxis(y_name, y_data)
    bar.render("./templates/{}.html".format(filename))


def line_chart(x_name, y_axis, filename):
    line = Line(init_opts=opts.InitOpts(width="300px", height="166px"))
    line.add_xaxis(x_name)
    for y_name, y_data in y_axis.items():
        line.add_yaxis(y_name, y_data)
    line.render("application/templates/{}.html".format(filename))

# def 

line_chart(["5.1","5.2","5.3","5.4","5.5"], {"降水量":[100,300,0,200,400],"紫外线":[12,34,56,76,30]},"test")
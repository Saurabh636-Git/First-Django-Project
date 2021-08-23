import uuid
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from .models import *


def gen_id():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code


def get_graph():
    buffer = BytesIO()
    print(buffer)
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    print(buffer.seek(0))
    image_png = buffer.getvalue()
    # After above function image is made.
    graph = base64.b64encode(image_png)
    # print(graph)
    graph = graph.decode('utf-8')
    # print(graph)
    buffer.close()
    return graph

def get_line_chart(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Sale of item')
    plt.plot(x,y)
    plt.xlabel('Date of Sales')
    plt.ylabel('Sales in Price')
    plt.tight_layout()
    graph = get_graph()
    return graph 

def get_bar_chart(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Sale of item')
    plt.bar(x,y)
    plt.xlabel('Date of Sales')
    plt.ylabel('Sales in Price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_pie_chart(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Sale of item')
    plt.pie(x=y, labels=x, autopct='%0.1f%%')
    plt.tight_layout()
    graph = get_graph()
    return graph

# img_trns = lambda request, pk:

def img_trns(list): 
    x = [x.date.strftime('%d %B %Y') for x in list]
    y = [y.total for y in list]
    x.sort()
    
    line_chart = get_line_chart(x, y)
    bar_chart = get_bar_chart(x,y)
    pie_chart = get_pie_chart(x,y)
    
    # context = {
    #     'x': x,
    #     'line_chart': line_chart,
    #     'bar_chart': bar_chart,
    #     'pie_chart': pie_chart,
    #     'item': item,
    # }
    return [line_chart, bar_chart, pie_chart]
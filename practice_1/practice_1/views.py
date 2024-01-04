from django.shortcuts import render
import datetime
def home(request):

    data={
        'id':1,
        'name': "Halal",
        'age': 20,
        'home': 'dhaka',
        'friends':["Rahim", 'Kala', 'varlar', 'Rohan'],
        'date': datetime.datetime.now(),
        'member':[
            {
                "name":"clark",
                "age":15,
            },
            {
                'name':"blunder",
                "age":20,
            },
            {
                "name":"jashim",
                "age":25
            }
        ],
    }

    return render(request, 'index.html',data)
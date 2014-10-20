
from django.views.decorators.csrf import csrf_exempt

from osf.models import Timeline
from osf.serializers import TimelineSerializer


#this is for the second part.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser

from osf.models import History
import datetime
from rest_framework.parsers import JSONParser
from django.db import connection
import json


def proper_creation_request(data):
    if 'wiki' not in data or not data['wiki']:
        return False
    if 'title' not in data or not data['title']:
        return False
    if 'author' not in data or not data['author']:
        return False
    if 'date' not in data or not data['author']:
        return False
    if 'project_id' not in data or not data['project_id']:
        return False
    return True


#NOTE: in hybrid, writes not optimized since you have to write to both db's.
#reads still have issue that you have to crawl through database (mongo). do not have to import entire collection but can do that in mongo regularly.
#reads better in thats
#in terms of scalability, mongo = better.

@csrf_exempt
@api_view(['POST'])
def create_new_project(request, format=None):
    print "new proj called"
    if request.method == 'POST':
        print str(request.DATA)

        p_id = int(request.DATA['project_id'])

        if not proper_creation_request(request.DATA):
            return Response("proper input not provided",status=status.HTTP_400_BAD_REQUEST)

        try:

            timeline = Timeline.objects.get(project_id=p_id)

           #if project with given project id exists, then throw error.
            return Response("project already exists",status=status.HTTP_400_BAD_REQUEST)
        except:
            #if error then project doesnt exist. this is good.
            pass
        properly_pg=False
        properly_mongo=False
        try:

            post_date = request.DATA['date'].split("-")
            d = datetime.datetime(month=int(post_date[0]), day=int(post_date[1]),year=int(post_date[2])) # 09-20-2014


            data = request.DATA.copy()
            data['date']=d
            data['project_id'] = int(request.DATA['project_id'])


            serializer = TimelineSerializer(data=data)



            if serializer.is_valid():
                serializer.save()
                properly_pg=True
            else:
                return Response("input data did not save in postgre", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("project unable to be created in postgre.",status=status.HTTP_400_BAD_REQUEST)
        try:
            h = History(date=d,
                        title=data['title'],
                        project_id=p_id,
                        time=data['time'],
                        author=data['author'])
            h.save()
            properly_mongo = True
        except:
            return Response("project unable to be created in mongo", status=status.HTTP_400_BAD_REQUEST)

        if properly_pg and properly_mongo:
            out = {p_id:"Project Created."}
            return Response(out, status=status.HTTP_201_CREATED)
        else:
            return Response("input data exists, but is not valid.", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



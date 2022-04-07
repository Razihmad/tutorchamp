from django_chatter.models import Room, Message
from django_chatter.views import ChatRoomView
from django.contrib.auth.models import User
from django_chatter.utils import create_room

def chat_context(request):

    context = {}
    if not request.user.is_authenticated:
        return context

    rooms_list = Room.objects.filter(members=request.user).order_by('-date_modified')
    
    if rooms_list.exists():
        latest_room_uuid = rooms_list[0].id
    else:
        user = User.objects.get(username=request.user)
        latest_room_uuid = create_room([user]).id
        staff = User.objects.filter(groups__name='Students Help')
        room = create_room(staff)
        room.members.add(user)
        room.save()

    crv = ChatRoomView()
    crv.request = request
    context = crv.get_context_data(uuid=latest_room_uuid)
    context['head_message'] = "You can talk here {}".format(latest_room_uuid)
    return context
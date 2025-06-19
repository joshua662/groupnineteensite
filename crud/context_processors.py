from .models import Notification

def notification_count(request):
    """Context processor to provide unread notification count to all templates"""
    if hasattr(request, 'session') and 'student_id' in request.session:
        try:
            unread_count = Notification.objects.filter(
                student_id=request.session['student_id'], 
                is_read=False
            ).count()
            return {'unread_notifications_count': unread_count}
        except:
            return {'unread_notifications_count': 0}
    return {'unread_notifications_count': 0}
 
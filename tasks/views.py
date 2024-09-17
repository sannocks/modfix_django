from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages
from django.core.mail import send_mail

@login_required
def task_list(request):
    """
    View to list tasks for staff. Staff can filter tasks by status.
    """
    tasks = Task.objects.filter(staff_member=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.time_spent = request.POST.get('time_spent')
        task.save()

        if task.status == 'completed':
            # Send a success message in-app
            messages.success(request, f"Task for {task.client.user.username} has been completed.")
            
            # Send email notification to client
            send_mail(
                subject="Your task has been completed",
                message=f"Hello {task.client.user.username},\n\nYour task for {task.content_block.block_type} has been completed.",
                from_email='your_email@example.com',
                recipient_list=[task.client.user.email],
                fail_silently=False,
            )

        return redirect('task_list')

    return render(request, 'tasks/update_task_status.html', {'task': task})

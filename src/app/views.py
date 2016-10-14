import os

from django.shortcuts import render
import dockercloud


def index(request):
    service_name = os.environ.get('DOCKERCLOUD_SERVICE_HOSTNAME')
    containers_count = 0
    if service_name:
        try:
            service = dockercloud.Service.list(name=service_name)[0]
        except Exception as e:
            print e
        else:
            containers_count = service.running_num_containers
    context = {
        'app_env': os.environ.get('APP_ENV'),
        'container': os.environ.get('DOCKERCLOUD_CONTAINER_HOSTNAME'),
        'containers_count': containers_count,
        'service': service_name,
        'stack': os.environ.get('DOCKERCLOUD_STACK_NAME')
    }
    return render(request, 'app/index.html', context=context)

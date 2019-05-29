from rest_framework import permissions, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response

from rest_framework_json_api.renderers import JSONRenderer

from ..libs.marshmallow_jsonschema import JSONSchema
from ..models import Schedule, parse_schedule_trigger, FailedToParseScheduleException

ADMIN_RENDERER_CLASSES = (
    JSONRenderer,
    BrowsableAPIRenderer,
)


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    plugin_id = serializers.IntegerField()

    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['plugin']

    class JSONAPIMeta:
        resource_name = 'schedule'

    def validate(self, data):
        try:
            parse_schedule_trigger(data['method'], data['method_config'])
        except FailedToParseScheduleException as e:
            raise serializers.ValidationError('Failed to parse schedule: %s' % (e.args[0], ))

        return data


class ScheduleModelView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    renderer_classes = ADMIN_RENDERER_CLASSES
    permission_classes = (permissions.IsAdminUser, )
    pagination_class = None
    filterset_fields = ('plugin', )

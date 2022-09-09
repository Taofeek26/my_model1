from rest_framework import serializers
from endpoints.models import Endpoint
from endpoints.models import MLAlgorithm
from endpoints.models import MLAlgorithmStatus
from endpoints.models import MLRequest


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = ('id', 'name', 'owner', 'created_at')
        fields = read_only_fields

class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlagorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlagorithm = mlagorithm).latest('created_at').status

    class Meta:
        model = MLAlgorithm
        read_only_fields = ('id', 'name', 'description', 'code', 'version', 'owner', 'created_at',
                            'parent_endpoint', 'current_status')
        field = read_only_fields

class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "created_by", "created_at","parent_mlalgorithm")

class MLRequestSerializer(serializers.ModelSerializer):
    model = MLRequest
    read_only_fields = ('id', 'input_data', 'full_response', 'response', 'created_at', 'parent_mlagorithm')
    fields = ('id', 'input_data', 'full_response', 'response', 'created_at', 'parent_mlagorithm')
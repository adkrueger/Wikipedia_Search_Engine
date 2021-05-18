from rest_framework import serializers

class WikiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        values = None

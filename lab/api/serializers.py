from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField(max_length=30)
   description = serializers.CharField(required=False)
   city = serializers.CharField(max_length=40, required=False)
   address = serializers.FloatField(required=False)

   def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'),
                                        description=validated_data.get('description'),
                                        city=validated_data.get('city'), 
                                        address=validated_data.get('address'))
        return company


   def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class VacancySerializer(serializers.ModelSerializer):
#     It will automatically generate a set of fields for you, based on the model.
#     It will automatically generate validators for the serializer, such as unique_together validators.
#     It includes simple default implementations of .create() and .update().
   # company = serializers.IntegerField(write_only=True)
    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'description', 'salary']

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.salary = validated_data.get('salary', instance.salary)
    #     instance.save()
    #     return instance
from rest_framework import serializers
from . import models


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = ('pk', 'photo', 'name', 'address', 'description')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = ('start_date', 'end_date', 'room', 'user')

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("finish must occur after start")
        reservation_query = models.Reservation.objects.filter(room=data['room'])
        for reservation in reservation_query:
            if data['start_date'] <= reservation.end_date and reservation.start_date <= data['end_date']:
                raise serializers.ValidationError(
                    'Room is already reserved from ' + str(
                        reservation.start_date) +
                    ' to ' + str(reservation.end_date)
                    + ', please change date')
        return data

    def create(self, validated_data):
        return models.Reservation.objects.create(**validated_data)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('name', 'photo', 'description', 'pk')

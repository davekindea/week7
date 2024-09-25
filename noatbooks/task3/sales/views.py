from django.shortcuts import render


import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SalesDataSerializer
import os
from django.conf import settings

# Load the trained model
model_path = os.path.join(settings.BASE_DIR, 'C:/Users/user/OneDrive/Desktop/Week4/noatbooks', 'model_24-09-2024-23-52-53.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)


class SalesPredictionView(APIView):
    def post(self, request):
        serializer = SalesDataSerializer(data=request.data)
        if serializer.is_valid():
            sales_array = np.array(serializer.validated_data['Sales']).reshape(-1, 1)

       
            scaler = MinMaxScaler(feature_range=(-1, 1))
            scaled_data = scaler.fit_transform(sales_array)

            
            window_size = 10  
            input_data = []
            for i in range(len(scaled_data) - window_size):
                input_data.append(scaled_data[i:i + window_size])

            input_data = np.array(input_data).reshape(len(input_data), window_size, 1)

            # Make predictions
            predictions = model.predict(input_data)
            predictions = scaler.inverse_transform(predictions)  # Scale back to original values

            return Response({'predictions': predictions.flatten().tolist()})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


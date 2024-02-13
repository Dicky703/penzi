from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, Users
from .serializers import PenziMessageSerializer

class PenziMessageView(generics.CreateAPIView):
    serializer_class = PenziMessageSerializer # adding a serializer class

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        penzi_message = serializer.save()

        message_from = serializer.validated_data.get('message_from')
        message_to = serializer.validated_data.get('message_to')
        message_content = serializer.validated_data.get('message_content')

        response_message = self.generate_response_message(message_content, message_from, message_to)
        
        # Saving the response message content to the response_content column of penzi_message
        penzi_message.response_content = response_message
        penzi_message.save()

        return Response({'message': response_message})

       

    def generate_response_message(self, message_content, message_from, message_to):
        ladies = [
            {"name": "Lina Moraa", "age": 29, "msisdn": "0722010203"},
            {"name": "Dorine Gakii", "age": 26, "msisdn": "0701223344"},
            {"name": "Aisha Bahati", "age": 27, "msisdn": "0700112233"}
         ]
        if message_content.startswith('penzi'):
            response_message = "Welcome to our dating service with 6000 potential dating partners! To register SMS start#name#age#gender#county#town to 22141. E.g., start#John Doe#26#Male#Nakuru#Naivasha"
            
        elif message_content.startswith('start'):
            split_content = message_content.split("#")
            if len(split_content) < 6:
                response_message = "Less details provided"
            else:
                name = split_content[1]
                response_message = f'Your profile has been created successfully {name}. SMS details#levelOfEducation#profession#maritalStatus#religion#ethnicity to 22141 E.g. details#diploma#driver#single#christian#mijikenda.'
        elif message_content.startswith('details'):
            split_content = message_content.split('#')
            if len(split_content) < 6:
                response_message = "You were registered for dating with your initial details. To search for a MPENZI, SMS match#age#town to 22141 and meet the person of your dreams.E.g., match#23-25#Nairobi"
            else:
                response_message = 'This is the last stage of registration. SMS a brief description of yourself to 22141 starting with the word MYSELF. E.g., MYSELF chocolate, lovely, sexy etc.'

         
        elif message_content.startswith('MYSELF'):
            split_content = message_content.split(',')
            if len(split_content) < 3:
                response_message = 'SMS a brief description of yourself to 22141 starting with the word MYSELF. E.g., MYSELF chocolate, lovely, sexy etc.' 
            else:
                response_message = 'You are now registered for dating. To search for a MPENZI, SMS match#age#town to 22141 and meet the person of your dreams.E.g., match#23-25#Kisumu'
        elif message_content.startswith('Match'):
            split_content = message_content.split('#')
            if len(split_content) < 3:
                response_message = 'To search for a MPENZI, SMS match#age#town to 22141 and meet the person of your dreams. E.g., match#23-25#Kisumu'
            else:
                response_message = f'We have 32 ladies who match your choice! We will send you details of 3 of them shortly{ladies}. To get more details about a lady, SMS her number e.g., 0722010203 to 22141'            
        else:
             response_message = "Please send a message starting with the word 'penzi' to 22141."

            

        return response_message

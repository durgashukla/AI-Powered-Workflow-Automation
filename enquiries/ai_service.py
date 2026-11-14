
import json
from groq import Groq
from django.conf import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


def analyze_enquiry(message):

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": """
                You are an AI business enquiry analyzer.

                Analyze the customer's enquiry and extract:

                1. category
                2. budget
                3. location
                4. priority
                5. requirements
                6. missing_information
                7. ai_summary
                8. suggested_response

                Category must be one of:
                website, mobile, ai, marketing,
                ecommerce, custom, other.

                Priority must be one of:
                low, medium, high.

                If budget or location is not mentioned,
                return an empty string.

                Requirements must be a list of strings.

                Return only valid JSON with these exact keys.
                """
            },

            {
                "role": "user",
                "content": message
            }
        ],

        response_format={"type": "json_object"}
    )

    result = response.choices[0].message.content

    return json.loads(result)
